import numpy 
from src.matrix.matrix import Matrix

class Board:

    def __init__(self, matrix:numpy.ndarray, height:int=22, width:int=10):
        self._matrix: Matrix = matrix
        self.height:int = height
        self.width:int = width
    
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
                
    def get_zone_tetramino(self,) -> numpy.ndarray:
        """
        Retorna la zona de la matriz que corresponde a la pieza
        """
        return self._matrix.matrix[0:2,3:7]