import cv2 as cv
import numpy as np
from src.matrix.matrix import Matrix

def resize_image(image:np.ndarray, width:int, height:int) -> np.ndarray:
    """
    Cambia el tamaño de la imagen a la altura y ancho especificados
    esto para facilitar la conversion de la imagen a una matriz 22x10
    """
    return cv.resize(image, (width, height))

def threshold_image(image: np.ndarray) -> np.ndarray:
    # converrit la imagen a escala de grises
    # gray = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = gray.astype(np.uint8)
    # aplicar binary thresholding a la imagen
    _, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return thresh

def to_matrix(image:np.ndarray, height:int=22, width:int=10) -> Matrix:
    return Matrix(image, height, width)