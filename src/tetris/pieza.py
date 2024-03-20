#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import abejas_tetris.tetris 
from .tipo_pieza import *
import numpy as np

class Pieza:
    """ Representa una pieza dentro del tablero. """
    def __init__(self, zone:np.ndarray):
        """
        Parameters
        ----------
        zone : np.ndarray
            Es la zona donde se puede buscar la pieza.4
            Corresponde a la mitad superior del tablero.
            Esta es de tamaño 2x10.
        """

        self._zone: np.ndarray = zone
        self._tipo: Tipo = None
        self._orientacion = 0
        self.create_piece()
        

    def create_piece(self):
        """
        Extraer de la zona el tipo de pieza que corresponde.
        Dependiendo de la zona se puede saber que tipo de pieza es.
        """
        if self._zone[0][0:4].all() == 1:
            # self._tipo = Tipo.I
            self._tipo = Tipo.Linea
            return
        elif self._zone[0][1:3].all() == 1 and self._zone[1][0:2].all() == 1:
            # self._tipo = Tipo.RS
            self._tipo = Tipo.S
            return
        elif self._zone[0][0:2].all() == 1 and self._zone[1][1:3].all() == 1:
            # self._tipo = Tipo.LS
            self._tipo = Tipo.Z
            return
        elif self._zone[0][1] == 1 and self._zone[1][0:3].all() == 1:
            self._tipo = Tipo.T
            return
        elif self._zone[0][2] == 1 and self._zone[1][0:3].all() == 1:
            # self._tipo = Tipo.RG
            self._tipo = Tipo.LDER
        elif self._zone[0][0] == 1 and self._zone[1][1:3].all() == 1:
            # self._tipo = Tipo.LG
            self._tipo = Tipo.LIZ
            return
        elif self._zone[0][1:3].all() == 1 and self._zone[1][1:3].all() == 1:
            self._tipo = Tipo.Sq
        else:
            self._tipo = None
            return

    def rotate(self):
        """
        Rota la pieza.
        """


    def getpiecerotation(self, currentrot) -> tuple:
        self._orientacion = currentrot
        if (self._tipo == Tipo.Linea):
            ficha, firsti = self.getlinearotation(currentrot)
            return ficha, firsti
        
        if (self._tipo == Tipo.S):
            ficha, firsti= self.getSrotation(currentrot)
            return ficha, firsti
        
        if (self._tipo == Tipo.Z):
            ficha, firsti = self.getZrotation(currentrot)
            return ficha, firsti
        
        if (self._tipo == Tipo.T):
            ficha, firsti = self.getTrotation(currentrot)
            return ficha, firsti
        
        if (self._tipo == Tipo.LDER):
            ficha, firsti = self.getLDERrotation(currentrot)
            return ficha, firsti
        
        if (self._tipo == Tipo.LIZ):
            ficha, firsti = self.getLIZrotation(currentrot)
            return ficha, firsti
        
        if (self._tipo == Tipo.S):
            firsti = 4
            ficha = np.array([[1, 1], 
                              [1, 1]])
            return ficha, firsti
    
    # LINEA ROTACIONES
    def getlinearotation(self, currentrot):
        if (currentrot == 0): # 0 Degrees
            firsti = 3
            ficha = np.array([1,1,1,1])
            return ficha, firsti
        
        elif (currentrot == 1): # 90 Degrees
            firsti = 5
            ficha = np.array([[1], 
                              [1],
                              [1],
                              [1]])
            return ficha, firsti
        
        elif (currentrot == 2): # 180 Degrees
            firsti = 3
            ficha = np.array([1,1,1,1])
            return ficha, firsti
        
        elif (currentrot == 3): # 270 Degrees
            firsti = 4
            ficha = np.array([[1], 
                              [1],
                              [1],
                              [1]])
            return ficha, firsti
    
    # S ROTACIONES
    def getSrotation(self, currentrot):
        if (currentrot == 0): # 0 Degrees
            firsti = 3
            ficha = np.array([[0,1,1], 
                              [1,1,0]])
            return ficha, firsti
        
        elif (currentrot == 1): # 90 Degrees
            firsti = 4
            ficha = np.array([[1,0], 
                              [1,1],
                              [0,1]])
            return ficha, firsti
        
        elif (currentrot == 2): # 180 Degrees
            firsti = 3
            ficha = np.array([[0,1,1], 
                              [1,1,0]])
            return ficha, firsti
        
        elif (currentrot == 3): # 270 Degrees
            firsti = 3
            ficha = np.array([[1,0], 
                              [1,1],
                              [0,1]])
            return ficha, firsti
        
    # Z ROTACIONES
    def getZrotation(self, currentrot):
        if (currentrot == 0): # 0 Degrees
            firsti = 3
            ficha = np.array([[1,1,0], 
                              [0,1,1]])
            return ficha, firsti
        
        elif (currentrot == 1): # 90 Degrees
            
            firsti = 4
            ficha = np.array([[0,1], 
                              [1,1],
                              [1,0]])
            return ficha, firsti
        
        elif (currentrot == 2): # 180 Degrees
            firsti = 3
            ficha = np.array([[1,1,0], 
                              [0,1,1]])
            return ficha, firsti
        
        elif (currentrot == 3): # 270 Degrees
            firsti = 3
            ficha = np.array([[0,1], 
                              [1,1],
                              [1,0]])
            return ficha, firsti
        
    # T ROTACIONES
    def getTrotation(self, currentrot):
        if (currentrot == 0): # 0 Degrees
            firsti = 3
            ficha = np.array([[0,1,0], 
                              [1,1,1]])
            return ficha, firsti
        
        elif (currentrot == 1): # 90 Degrees
            firsti = 4
            ficha = np.array([[1,0], 
                              [1,1],
                              [1,0]])
            return ficha, firsti
        
        elif (currentrot == 2): # 180 Degrees
            firsti = 3
            ficha = np.array([[1,1,1], 
                              [0,1,0]])
            return ficha, firsti
        
        elif (currentrot == 3): # 270 Degrees
            firsti = 3
            ficha = np.array([[0,1], 
                              [1,1],
                              [0,1]])
            return ficha, firsti
        
    # LDER ROTACIONES
    def getLDERrotation(self, currentrot):
        if (currentrot == 0): # 0 Degrees
            firsti = 3
            ficha = np.array([[0,0,1], 
                              [1,1,1]])
            return ficha, firsti
        
        elif (currentrot == 1): # 90 Degrees
            firsti = 4
            ficha = np.array([[1,0], 
                              [1,0],
                              [1,1]])
            return ficha, firsti
        
        elif (currentrot == 2): # 180 Degrees
            firsti = 3
            ficha = np.array([[1,1,1], 
                              [1,0,0]])
            return ficha, firsti
        
        elif (currentrot == 3): # 270 Degrees
            firsti = 3
            ficha = np.array([[1,1], 
                              [0,1],
                              [0,1]])
            return ficha, firsti
        
    # LIZ ROTACIONES
    def getLIZrotation(self, currentrot):
        if (currentrot == 0): # 0 Degrees
            firsti = 3
            ficha = np.array([[1,0,0], 
                              [1,1,1]])
            return ficha, firsti
        
        elif (currentrot == 1): # 90 Degrees
            firsti = 4
            ficha = np.array([[1,1], 
                              [1,0],
                              [1,0]])
            return ficha, firsti
        
        elif (currentrot == 2): # 180 Degrees
            firsti = 3
            ficha = np.array([[1,1,1], 
                              [0,0,1]])
            return ficha, firsti
        
        elif (currentrot == 3): # 270 Degrees
            firsti = 3
            ficha = np.array([[0,1], 
                              [0,1],
                              [1,1]])
            return ficha, firsti
                       
    def get_zone(self) -> np.ndarray:
        """
        Regresa la zona de la pieza.
        """
        return self._zone
    
    def get_tipo(self) -> Tipo:
        """
        Regresa el tipo de la pieza.
        """
        return self._tipo.name

    def get_orientacion(self):
        """
        Regresa la orientación de la pieza de forma X = (n*90)mod360
        """
        return self._orientacion

    def set_orientacion(self, orientacion):
        """
        Asigna una orientación a la pieza
        
        Parameters
        ----------
        orientacion : int
                Es el número modulo 360.
        """
        self._orientacion = orientacion

    def set_puntos(self, casillas):
        """
        Asigna los puntos al objeto clonando las casillas.
        
        Parameters
        ----------
        casillas : list(Casilla)
                Es una lista de casillas.
        """
        self._casillas[0] = casillas[0].clona()
        self._casillas[1] = casillas[1].clona()
        self._casillas[2] = casillas[2].clona()
        self._casillas[3] = casillas[3].clona()

    def get_casillas_self(self):
        """
        Regresa las casillas que tiene el objeto.
        """
        return self._casillas

    def get_puntos(self):
        """
        Regresa puntos que representan la posición de la pieza.
        """
        p1 = self._casillas[0].get_punto().clona()
        p2 = self._casillas[1].get_punto().clona()
        p3 = self._casillas[2].get_punto().clona()
        p4 = self._casillas[3].get_punto().clona()
        return [p1, p2, p3, p4]

    def mueve_derecha(self):
        """
        Mueve las casillas de la pieza hacia la derecha.
        """
        for i in self._casillas:
            punto = i.get_punto()
            punto.set_x(punto.get_x() + 1)

    def mueve_izquierda(self):
        """
        Mueve las casillas de la pieza hacia la izquierda.
        """
        for i in self._casillas:
            punto = i.get_punto()
            punto.set_x(punto.get_x() - 1)

    def baja(self):
        """
        Mueve las casillas de la pieza hacia abajo.
        Parameters
        ----------
        """
        for i in self._casillas:
            punto = i.get_punto()
            punto.set_y(punto.get_y() + 1)

    # Este método sólo se usa por las abejas observadoras
    # para regresar a un estado previo.
    def sube(self):
        """
        Mueve las casillas de la pieza hacia arriba.
        """
        for i in self._casillas:
            punto = i.get_punto()
            punto.set_y(punto.get_y() - 1)

    def fija(self):
        """
        Cambia el estado de todas las casillas.
        """
        return self._fijo

    def casillas(self):
        """
        Regresa las casillas de la pieza.
        """
        return self._casillas

    def get_tipo(self):
        """
        Regresa el tipo de la pieza.
        """
        return self._tipo

    # Funciones auxiliares:

    def __get_casillas(self):
        return get_casillas(self._tipo, self._posicion)
