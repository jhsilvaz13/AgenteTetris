# Brain
# Analyses current game state and provides best move using params
import numpy as np
from src.tetris.tetris import Tetris
from src.tetris.pieza import Pieza

class Brain:
    def __init__(self, tetris: Tetris):
        # Initialize brain with params
        self.previous_piece_index = None
        self.previous_move = None
        self.consagg = -0.458507
        self.conslines = 0.429457
        self.consholes = -0.454487
        self.consbump = -0.169442
        self.score = None
        self.current_selected_move = None
        self.possible_moves_scored = None
        self.highest_score = None
        self.current_state: Tetris = tetris
        self.current_shape: Pieza = None
        self.current_board:np.ndarray = tetris.get_tablero()[2:-1,:]#20x10
        self.process_current_state()

    def process_current_state(self):
        # Receives current state to predict best move
        new_move = None
        self.current_shape = self.current_state.get_current_tetramino()
        # Check if there's a new piece in the board
        if self.current_state.get_current_tetramino_type() != None:
            self.current_shape = self.current_state.get_current_tetramino()
            # Analyze all possible moves and score them
            self.possible_moves_scored = self.score_all_possible_moves()
            # Pick best one
            self.highest_score = self.possible_moves_scored[0]["score"]
            self.current_selected_move = self.possible_moves_scored[0]
            for move in self.possible_moves_scored:
                if move["score"] > self.highest_score:
                    self.highest_score = move["score"]
                    # Use that as the next general trajectory
                    self.current_selected_move = move
        # Pick move in movement frame from current trajectory
        new_move = self.select_move_from_current_selected_move(self.current_state)
        #self.previous_piece_index = current_state["shape_index"]
        return new_move

    def score_all_possible_moves(self):
        # Analyze all possible moves
        possible_moves = []
        # First check all possible rotations
        for rotation_mode in range(4):
            #  la funcion getpiecerotation es de la clase Pieza
            # retorna una matriz con la pieza rotada y la posicion de 
            # la primera columna de la pieza
            print(self.current_shape.getpiecerotation(rotation_mode))
            rotated_shape = self.current_shape.getpiecerotation(rotation_mode)[0]
            first_col = self.current_shape.getfirstcol()[1]
            # Now check all possible positions for this rotation
            for j_position in range(0, 10 - len(rotated_shape[0]) + 1):
                i_position = first_col
                while not self.blocks_below(rotated_shape, i_position, j_position, (self.current_board)):
                    # Make the block go down until it stops
                    i_position += 1
                # Create possible grid with this new position
                possible_final_state = self.create_final_state(
                    self.current_board, rotated_shape, i_position, j_position)
                # Score this position
                possible_final_state_score = self.score_state(possible_final_state)
                possible_moves.append({"rotation_mode": rotation_mode,
                                       "i": i_position, "j": j_position,
                                       "score": possible_final_state_score})
        return possible_moves

    def rotate_shape(self, shape, rotation_mode):
        # Makes shape rotate
        old_shape = shape
        new_shape = shape
        for _rotation in range(rotation_mode):
            new_shape = []
            for j in range(len(old_shape[0])):
                new_row = []
                for i in range(len(old_shape)):
                    new_row.append(old_shape[len(old_shape) - 1 - i][j])
                new_shape.append(new_row)
            old_shape = new_shape
        return new_shape

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
        aggregate_height = grid.aggregate_height()
        """
        TO DO: Implement the rest of the scoring functions
        """
        #complete_lines = grid.complete_lines()
        complete_lines = 0
        holes = grid.holes()
        bumpiness = grid.bumpiness()
        state_score = self.consagg * aggregate_height + self.conslines * complete_lines + \
                      self.consholes * holes + self.consbump * bumpiness
        return state_score

    def complete_lines(self, grid):
        # Calculate number complete lines
        complete_lines = 0
        for i in range(len(grid)):
            full_row = all(grid[i][j] for j in range(len(grid[i])))
            if full_row:
                complete_lines += 1
        return complete_lines

    def select_move_from_current_selected_move(self, state):
        # Pick next move for piece to go along current trajectory
        # If it can rotate and it's required for the trajectory, then rotate
        #if state["shape_rotation"] != self.current_selected_move["rotation_mode"]:
        if self.current_shape.get_orientacion() != self.current_selected_move["rotation_mode"]:
            #if self.shape_can_rotate(state["shape"], state["grid"],
            #                        state["shape_i"], state["shape_j"]):
            
            if self.shape_can_rotate(self.current_shape.getpiecerotation()[0], self.current_board,
                                    20, 10):
                return 1
        # Else, if it's not on top of where the next move is, then go that way
        if 20 < self.current_selected_move["j"]:
            return 2
        if 10 > self.current_selected_move["j"]:
            return 3
        return 4

    def shape_can_rotate(self, shape, grid, i_position, j_position):
        # Check possible collisions for piece to rotate
        possible_new_shape = self.rotate_shape(shape, 1)
        for i in range(len(possible_new_shape)):
            for j in range(len(possible_new_shape[i])):
                if i + i_position >= len(grid) or j + j_position >= len(grid[0]) or \
                        (possible_new_shape[i][j] and \
                         grid[i + i_position][j + j_position]):
                    return False
        return True

