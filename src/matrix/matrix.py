"""
Esta clase toma un np.array que representa la imagen
y lo convierte en una matriz 22x10
que representa el tablero de tetris.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

class Matrix:
    image: np.ndarray
    matrix: np.ndarray
    def __init__(self, image: np.ndarray):
        self.image = image
        self.matrix = np.zeros((22,10), dtype=int)
        self.__matrix_reduction()

    def __matrix_reduction(self) -> np.ndarray:
        """
        Esta función toma la imagen que se paso en el constructor y lo convierte en una matriz 
        22x10 con:
        - 1 si la casilla esta ocupada
        - 0 si la casilla esta vacía
        Representa el tablero de tetris, la imagen debe ser en escala de grises.
        El tamaño es 22 pues en las dos primeras filas se encuentra la ficha actual
        """
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                if self.image[i][j] == 255:
                    self.matrix[i][j] = 1

    def print_board(self) -> str:
        print(self.matrix)