import numpy as np
from src.tetris.tablero import Board
from src.tetris.pieza import Pieza
from src.tetris.tipo_pieza import Tipo
import pyautogui
import time

class Tetris:
    """ Representa un juego de tetris con todos sus componentes."""
    def __init__(self, matrix:np.ndarray=None, next:np.ndarray=None, hold:np.ndarray=None):
        """
        Parameters
        ----------
        tablero : Tablero 
                Es un tablero por si el objeto es clonado. 22x10
        """
        self.consagg = -0.458507 # -0.510066        
        self.conslines =  0.429457 # 0.760666       
        self.consholes = -0.454487 # -0.35663            
        self.consbump = -0.169442 # -0.184483       
        self.score = None
        self.current_selected_move = None
        self.possible_moves_scored = None
        self.highest_score = None
        
        if matrix is None:
            exception = Exception("No se puede crear un juego sin un tablero")
            raise exception
        self._tablero = Board(matrix)

    def print_board(self) -> None:
        """
        Imprime el tablero en consola.
        """
        print(self._tablero.get_matrix())
        return None
    
    def aggregate_height(self, grid:np.ndarray) -> int:
        # Calculate aggregate height
        aggregate_height = 0
        for column in range(10):
            found_first_one = False
            for row in range(0, 20):
                if grid[row][column] and not found_first_one:
                    found_first_one = True
                    aggregate_height += len(grid) - row
        return aggregate_height
    
    def holes(self, grid:np.ndarray) -> int:
        # Calculate number of holes
        holes = 0
        for column in range(10):
            found_first_one = False
            for row in range(0, 20):
                if grid[row][column] and not found_first_one:
                    found_first_one = True
                if found_first_one and grid[row][column] == 0:
                    holes += 1
        return holes
    
    def bumpiness(self, grid:np.ndarray) -> int:
        # Calculate bumpiness
        bumpiness = 0
        previous_height = 0
        for column in range(10):
            found_first_one = False
            for row in range(0, 20):
                if grid[row][column] and not found_first_one:
                    found_first_one = True
                    height = len(grid) - row
                    if column > 0:
                        bumpiness += abs(height - previous_height)
                    previous_height = height
            if not found_first_one:
                if column > 0:
                    bumpiness += previous_height
                previous_height = 0
        return bumpiness
    
    def complete_lines(self, grid:np.ndarray):
        # Calculate number complete lines
        complete_lines = 0
        for i in range(20):
            full_row = all(grid[i][j] for j in range(len(grid[i])))
            if full_row:
                complete_lines += 1
        return complete_lines
    
    def get_current_tetramino(self) -> Pieza:
        """
        Regresa la pieza actual.
        """
        return Pieza(self._tablero.get_zone_tetramino())
    
    def get_current_tetramino_type(self) -> Tipo:
        """
        Regresa el tipo de la pieza actual.
        """
        return Pieza(self._tablero.get_zone_tetramino()).get_tipo()
    
    def get_tablero(self) -> np.ndarray:
        """
        Regresa el tablero del juego.
        """
        return self._tablero.get_matrix()
    
    def blocks_below(self, shape, i_position, j_position, grid):
        # Check if there are blocks below or if it can keep going down
        # First check if it reached the end of the world
        if i_position + len(shape) + 1 > len(grid):
            return True
        # Now check collision with bottom possible pieces
        for j in range(len(shape[0])):
            column_bottom_piece = 0
            for i in range(len(shape)):
                if shape[i][j]:
                    column_bottom_piece = i
            # Check square below bottom piece square of the column
            if grid[i_position + column_bottom_piece + 1][j_position + j]:
                return True
        return False

    def create_final_state(self, grid, shape, i_position, j_position):
        # Add new possible piece position to grid to score this state
        new_full_grid = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[i])):
                if i >= i_position and i < i_position + len(shape) and \
                        j >= j_position and j < j_position + len(shape[0]) and \
                        shape[i - i_position][j - j_position]:
                    new_row.append(1)
                else:
                    new_row.append(grid[i][j])
            new_full_grid.append(new_row)
        return new_full_grid
    
    def score_state(self, grid: np.ndarray):
        # Use formula to score this possible grid
        aggregate_height = self.aggregate_height(grid)
        complete_lines = self.complete_lines(grid)
        holes = self.holes(grid)
        bumpiness = self.bumpiness(grid)
        state_score = (self.consagg * aggregate_height) + (self.conslines * complete_lines) + \
                      (self.consholes * holes) + (self.consbump * bumpiness)
        return state_score
    
    def score_all_possible_moves(self, current_state:np.ndarray,) -> list: #Current state: 20x10
        # Analyze all possible moves
        current_shape = self.get_current_tetramino()
        possible_moves = []
        # First check all possible rotations
        for rotacion in range(4):
            # Rotate to this rotation
            rotated_shape, first_col, last_col = current_shape.getpiecerotation(rotacion)
            #print(rotated_shape)
            # Now check all possible positions for this rotation
            for j_position in range(0, len(current_state[0]) - len(rotated_shape[0]) + 1):
                i_position = len(rotated_shape)
                while not self.blocks_below(rotated_shape, i_position, j_position, current_state):
                    # Make the block go down until it stops
                    i_position += 1
                # Create possible grid with this new position
                possible_final_state = self.create_final_state(
                    current_state, rotated_shape, i_position, j_position)
                # Score this position
                possible_final_state_score = self.score_state(possible_final_state)

                possible_moves.append({"rotation_mode": rotacion, "j_first": first_col,
                                       "j_last": last_col, "j": j_position, 
                                       "score": possible_final_state_score})
                
        return possible_moves
    
    def process_current_state(self): #20x10
        current_state = self.get_tablero()[2:22,:]
        # Check if there's a new piece in the board
        if self.get_current_tetramino_type() != None:
            # Analyze all possible moves and score them
            self.possible_moves_scored = self.score_all_possible_moves(current_state)
            # Pick best one
            self.highest_score = self.possible_moves_scored[0]["score"]
            self.current_selected_move = self.possible_moves_scored[0]
            self.current_selected_move = max(self.possible_moves_scored, key=lambda move: move["score"])
            self.highest_score = self.current_selected_move["score"]
            # Call function in order to actually move
            self.move()

    # Move to the selected move    
    def move(self):
        rotaciones = self.current_selected_move["rotation_mode"]
        j_final = self.current_selected_move["j"]
        j_inicializ = self.current_selected_move["j_first"]
        j_inicialde = self.current_selected_move["j_last"]
        resta = j_final - j_inicializ
        derecha = j_inicialde + resta
        nmovs = abs(resta)
        
        # Check if can do full move to the sides instantly
        if j_final == 0:
            if rotaciones == 3:
                pyautogui.press('altright')
            else:
                for i in range(rotaciones):
                    # First rotate to the selected rotation
                    pyautogui.press('up')
            pyautogui.keyDown('left')
            time.sleep(0.0005)
            pyautogui.keyUp('left')
            pyautogui.press('space')
            return # no need to check the rest of the code
        
        elif j_final == 9:
            if rotaciones == 3:
                pyautogui.press('w')
            else:
                for i in range(rotaciones):
                    # First rotate to the selected rotation
                    pyautogui.press('up')
            pyautogui.keyDown('right')
            time.sleep(0.0005)
            pyautogui.keyUp('right') 
            pyautogui.press('space')
            return # no need to check the rest of the code
        
        if resta == 0:
            if rotaciones == 3:
                pyautogui.press('altright')
            else:
                for i in range(rotaciones):
                    # First rotate to the selected rotation
                    pyautogui.press('up')
            pyautogui.press('space')
            
        else:
            if rotaciones == 3:
                pyautogui.press('altright')
            else:
                for i in range(rotaciones):
                    # First rotate to the selected rotation
                    pyautogui.press('up')
            if resta > 0:
                if derecha == 9:
                    pyautogui.keyDown('right')
                    time.sleep(0.0005)
                    pyautogui.keyUp('right')
                else:
                    if nmovs == 4:
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                    elif nmovs == 3:
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                    elif nmovs == 2:
                        pyautogui.press('right')
                        pyautogui.press('right')
                    else:
                        pyautogui.press('right')
                    # for i in range(resta):
                    #     pyautogui.press('right')                    
            else:
                if nmovs == 3:
                    pyautogui.press('left')
                    pyautogui.press('left')
                    pyautogui.press('left')
                elif nmovs == 2:
                    pyautogui.press('left')
                    pyautogui.press('left')
                else:
                    pyautogui.press('left')
                # for i in range(-resta):
                #     pyautogui.press('left')
            pyautogui.press('space')