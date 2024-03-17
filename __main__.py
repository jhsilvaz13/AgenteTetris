"""
Esta clase solo es de prueba para tomar el ss del
tablero de tetris y convertirlo en una matriz 10x20.

"""

import numpy as np
from src.video.boardcapture import WindowCapture
import time
import cv2 as cv
from src.matrix.matrix import Matrix
import logging

logging.basicConfig(level=logging.DEBUG)

time.sleep(3)

board = WindowCapture()
board = board.get_screenshot()
0
"""
Guardamos la captura de pantalla en un archivo .txt
"""

# Convertir la imagen a escala de grises
board_gray =np.dot(board[...,:3], [0.2989, 0.5870, 0.1140])
board_gray = board_gray.astype(np.uint8)
print(board_gray.shape)

for i in range(board_gray.shape[0]):
    for j in range(board_gray.shape[1]):
        if board_gray[i][j] > 10:
            board_gray[i][j] = 255
    print()
# Aplicar thresholding
ret, thresh2 = cv.threshold(board_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)



# Crear la matriz

matrix = Matrix(thresh2)
matrix.__str__()
logging.info("The matrix size is: {}".format(board_gray.shape))

# Guardar la matriz en un archivo de texto
np.savetxt("board_th.txt", thresh2, fmt="%3d")
np.savetxt("board_gray.txt", board_gray, fmt="%3d")