import numpy as np
from src.tetris.pieza import Pieza
from src.tetris.tetris import Tetris

def blocks_below(shape, i_position, j_position, grid):
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

def create_final_state(grid, shape, i_position, j_position):
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

def score_all_possible_moves(current_state:np.ndarray, current_shape:Pieza) -> list: #Current state: 20x10
    # Analyze all possible moves
    possible_moves = []
    # First check all possible rotations
    for rotacion in range(4):
        # Rotate to this rotation
        rotated_shape, first_col = current_shape.getpiecerotation(rotacion)
        #print(rotated_shape)
        # Now check all possible positions for this rotation
        for j_position in range(0, len(current_state[0]) - len(rotated_shape[0]) + 1):
            i_position = len(rotated_shape)
            while not blocks_below(rotated_shape, i_position, j_position, current_state):
                # Make the block go down until it stops
                i_position += 1
            # Create possible grid with this new position
            possible_final_state = create_final_state(
                current_state, rotated_shape, i_position, j_position)
            print("-------------------")
            for i in range(len(possible_final_state)):
                for j in range(len(possible_final_state[i])):
                    print(possible_final_state[i][j], end=" ")
                print()
            print("-------------------")

if __name__=="__main__":
   
    grid=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]]
    current_shape = Pieza(
        zone=np.array([
            [1, 1, 0, 0],
            [0, 1, 1, 0],]
        ))
    print("""
        Bumpiness: {}
        Complete lines: {}
        Holes: {}
        Aggregate height: {}
        """.format(Tetris.bumpiness(grid), Tetris.complete_lines(grid), Tetris.holes(grid), Tetris.aggregate_height(grid)))
    score_all_possible_moves(np.array(grid), current_shape)