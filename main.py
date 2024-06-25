from src.video.video import threshold_image, resize_image, to_matrix
from src.video.boardcapture import WindowCapture as b_Cap
from src.video.nextcapture import WindowCapture as n_Cap
from src.tetris.tetris import Tetris
import cv2 as cv

if __name__ == "__main__":
    boardcap = b_Cap()
    while(True):
        # get an updated image of the game
        # Esto captura el tablero del juego
        board = boardcap.get_screenshot()
        cv.waitKey(1)
        board = threshold_image(board)
        cv.imshow("Board", board)
        cv.moveWindow("Board", 1100, 400)
        board = resize_image(board, 10, 22)
        board = to_matrix(board)
        game =  Tetris(board)
        game.process_current_state()  