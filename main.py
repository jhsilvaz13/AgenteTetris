from src.video.video import threshold_image, resize_image, to_matrix
from src.video.boardcapture import WindowCapture as b_Cap
if __name__ == "__main__":
    boardcap = b_Cap()
    while(True):
        # get an updated image of the game
        """
        hold = holdcap.get_screenshot()
        hold = threshold_image(hold)
        hold = resize_image(hold, 10, 22)
        hold = to_matrix(hold)
        hold.print_board()
        """
        board = boardcap.get_screenshot()
        board = threshold_image(board)
        board = resize_image(board, 10, 22)
        board = to_matrix(board)
        board.print_board()
        """
        next = nextcap.get_screenshot()
        next = threshold_image(next)
        next = resize_image(next, 10, 22)
        next = to_matrix(next)
        next.print_board()
        """