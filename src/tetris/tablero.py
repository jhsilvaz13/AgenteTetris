import numpy 
from src.matrix.matrix import Matrix

class Board:
    _matrix: Matrix #representa el tablero del juego 22x10
    height = 22
    width = 10

    def __init__(self, matrix:numpy.ndarray, height:int=22, width:int=10):
        self._matrix = matrix
        self.height = height
        self.width = width
    
    def get_matrix(self) -> numpy.ndarray:
        return self._matrix.matrix
    
    def get_height(self) -> int:
        return self.height
    
    def get_width(self) -> int:
        return self.width
    
    def current_maximun_height(self) -> tuple:
        """
        Retorna la altura máxima en tuple(i,j) actual del tablero
        la altura maximma correspone a la altura de la 
        columna más alta
        """
        for i in range(self.height):
            for j in range(self.width):
                if self._matrix[i][j] == 1:
                    return tuple(i,j)
            