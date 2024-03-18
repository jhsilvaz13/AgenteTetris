import cv2 as cv
import numpy as np
from src.video.boardcapture import WindowCapture as h_Cap
from src.video.boardcapture import WindowCapture as b_Cap
from src.video.boardcapture import WindowCapture as n_Cap
from src.matrix.matrix import Matrix
import time

def resize_image(image:np.ndarray, width:int, height:int) -> np.ndarray:
    """
    Cambia el tamaño de la imagen a la altura y ancho especificados
    esto para facilitar la conversion de la imagen a una matriz 22x10
    """
    return cv.resize(image, (width, height))

def threshold_image(image: np.ndarray) -> np.ndarray:
    # converrit la imagen a escala de grises
    gray = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    gray = gray.astype(np.uint8)
    # aplicar binary thresholding a la imagen
    _, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return thresh

def to_matrix(image) -> Matrix:
    return Matrix(image)

    

def start():
    holdcap = h_Cap()
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
print('Done.')
