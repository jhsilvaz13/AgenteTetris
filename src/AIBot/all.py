import numpy as np
from ..tetris.pieza import Pieza

current_shape: Pieza = None

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
def score_all_possible_moves(current_state:np.ndarray) -> list: #Current state: 20x10
    # Analyze all possible moves
    possible_moves = []
    # First check all possible rotations
    for rotacion in range(4):
        # Rotate to this rotation
        rotated_shape = current_shape.getpiecerotation(rotacion)[0]
        first_col = current_shape.getfirstcol()[1]
        # Now check all possible positions for this rotation
        for j_position in range(0, len(current_state[0]) - len(rotated_shape[0]) + 1):
            i_position = len(current_state[:,0])
            while not blocks_below(rotated_shape, i_position, j_position, current_state):
                # Make the block go down until it stops
                i_position += 1
            # Create possible grid with this new position
            possible_final_state = create_final_state(
                current_state, rotated_shape, i_position, j_position)
            print(possible_final_state)

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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    current_shape = Pieza(
        zone=np.array([
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],]
        ))
    score_all_possible_moves(np.array(grid))