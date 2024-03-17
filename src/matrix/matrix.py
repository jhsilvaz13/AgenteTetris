"""
Esta clase toma un np.array y lo convierte en una matriz 10x20
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
        self.matrix = np.zeros((20,10), dtype=int)
        self.__matrix_reduction()

    def __calculate_avg_frame(self, np_array: np.ndarray, pos_x: int, pos_y: int) -> int:
        """
        Esta función calcula el promedio de los pixeles de un cuadrado.
        Retorna 1 si el promedio es mayor a 0.9(cuadro usado), 0 si el promedio es menor a 0.1 (cuadro vacío)
        y -1 si el promedio está entre 0.1 y 0.9 (cuadro proximo a utilzar).
        """
        print(np_array)
        sum = 0
        for i in range(0, np_array.shape[0]):
            for j in range(0, np_array.shape[1]):
                sum+=np_array[i][j]
        
        average = sum/(np_array.shape[0]*np_array.shape[1]*255)
        print("The average of the frame {} is: {}".format((pos_x, pos_y), average))
        if average > 0.65:
            return 1
        elif average < 0.26:
            return 0
        else:
            return -1

    def __matrix_reduction(self) -> np.ndarray:
        """
        Esta función toma la imagen que se paso en el constructor y lo convierte en una matriz 
        10x20 con:
        - 1 si la casilla esta ocupada
        - 0 si la casilla esta vacía
        - -1 si la casilla esta próxima a ser ocupada
        Representa el tablero de tetris.
        La imagen debe ser en escala de grises.
        """
        mult_i=0 # representa la coordenada x en la matriz 20X10 de la agrupación de pixeles de la imagen
        mult_j=0 # representa la coordenada y en la matriz 20X10 de la agrupación de pixeles de la imagen
        height_lim= self.image.shape[0]//20
        width_lim = self.image.shape[1]//10

        logging.info("The height limit is: {}".format(height_lim))
        logging.info("The width limit is: {}".format(width_lim))

        # en total se deben determinar 200 casillas de width_lim x height_lim pixeles
        casilla=np.zeros((height_lim, width_lim), dtype=int) #aca se almacenanan los pixeles de cada casilla
        while mult_i < self.matrix.shape[0]:
            mult_j=0
            while mult_j < self.matrix.shape[1]:
                for i in range(0, height_lim):
                    for j in range(0, width_lim):
                        casilla[i][j] = self.image[mult_i*i][mult_j*j]
                        value=self.__calculate_avg_frame(casilla, mult_i, mult_j)
                        self.matrix[mult_i][mult_j]=value
                mult_j+=1
            mult_i+=1

    def print_board(self) -> str:
        print(self.matrix)