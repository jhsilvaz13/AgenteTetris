def can_place_piece(board, piece, row, col):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                actual_row = row + i
                if actual_row >= len(board) or col + j < 0 or col + j >= len(board[0]) or board[actual_row][col + j] == 1:
                    return False
    return True

def place_piece(board, piece, row, col):
    new_board = [row[:] for row in board]
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                new_board[row + i][col + j] = 1
    return new_board

def get_possible_board_states(board, piece):
    possible_board_states = []
    for col in range(len(board[0]) - len(piece[0]) + 1):
        min_lowest_row = float('inf')
        for j in range(len(piece[0])):
            for i in range(len(piece)):
                if piece[i][j] == 1:
                    actual_row = 0
                    while actual_row + 1 < len(board) and board[actual_row + 1][col + j] == 0:
                        actual_row += 1
                    min_lowest_row = min(min_lowest_row, actual_row)
        for row in range(len(board) - len(piece) + 1):
            if row > min_lowest_row:
                break
            if can_place_piece(board, piece, row, col):
                new_board = place_piece(board, piece, row, col)
                possible_board_states.append(new_board)
    return possible_board_states

# Example usage:
board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0]
]

piece = [
    [1, 0],
    [1, 1],
    [0, 1]
]

possible_board_states = get_possible_board_states(board, piece)
for i, state in enumerate(possible_board_states):
    print("Possible board state", i+1)
    for row in state:
        print(row)
    print()