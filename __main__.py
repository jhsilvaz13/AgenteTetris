"""
Esta clase solo es de prueba para tomar el ss del
tablero de tetris y convertirlo en una matriz 22x10
"""

import numpy as np
from src.video.boardcapture import WindowCapture
import time
import cv2 as cv
from src.matrix.matrix import Matrix
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG)
time.sleep(3)

board = WindowCapture()
board = board.get_screenshot()
0

"""
Convertir la imagen a escala de grises 
y aplicar thresholding para obtener la matriz
después de reducir la imagen a 22x10.
"""
board_gray =np.dot(board[...,:3], [0.2989, 0.5870, 0.1140])
board_gray = board_gray.astype(np.uint8)
# Aplicar thresholding
ret, thresh2 = cv.threshold(board_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# Cambiar el tamaño de la imagen
thresh2 = cv.resize(thresh2, (10, 22))
"""
Crear la matriz 22x10
"""
# Crear la matriz
matrix = Matrix(thresh2)
matrix.print_board()
logging.info("The matrix size is: {}".format(board_gray.shape))

# Guardar la matriz en un archivo de texto
np.savetxt("board_th.txt", thresh2, fmt="%3d")