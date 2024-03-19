from src.video.video import threshold_image, resize_image, to_matrix
from src.video.boardcapture import WindowCapture as b_Cap
from src.video.nextcapture import WindowCapture as n_Cap
from src.tetris.tetris import Tetris
import cv2 as cv
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
        cv.imshow('Board', board)
        cv.moveWindow('Board', 1000, 200)
        board = resize_image(board, 10, 22)
        board = to_matrix(board)
        game =  Tetris(board)
        # game.print_board()
        # print("")
        
        actual_piece = game.get_current_tetramino_type()
        aggregate_height = game.aggregate_height()
        holes = game.holes()
        bumpiness = game.bumpiness()
        
        if (actual_piece != None):
            print("The current tetramino is: {}".format(actual_piece))
            print("The current aggregate height is: {}".format(aggregate_height))
            print("The current number of holes is: {}".format(holes))
            print("The current bumpiness is: {}".format(bumpiness))

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

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break