from src.video.video import threshold_image, resize_image, to_matrix
from src.video.boardcapture import WindowCapture as b_Cap
from src.video.nextcapture import WindowCapture as n_Cap
from src.tetris.tetris import Tetris
import cv2 as cv
import time

if __name__ == "__main__":
    boardcap = b_Cap()
    nextcap = n_Cap()
    while(True):
        # get an updated image of the game
        """
        hold = holdcap.get_screenshot()
        hold = threshold_image(hold)
        hold = resize_image(hold, 10, 22)
        hold = to_matrix(hold)
        hold.print_board()
        """

         # Esto captura el tablero del juego
        board = boardcap.get_screenshot()
        board = threshold_image(board)
        board = resize_image(board, 10, 22)
        board = to_matrix(board)

        game =  Tetris(board)
        game.process_current_state()
        
        """
        # Esto captura la siguiente pieza(solo 1 la más proxima)
        next = nextcap.get_screenshot()
        next = threshold_image(next)
        #UNCOMMENT: to see the next piece
        #cv.imshow('next', next)
        #cv.waitKey(0)
        next = resize_image(next,height=3, width=5)
        next = to_matrix(next,height=3, width=5)
        next.print_board()
        """
        """
         if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        """