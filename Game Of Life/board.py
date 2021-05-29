import numpy as np
import random
import pygame as pg


class Board:
    def __init__(self, altura, ancho, escala):
        self.escala = escala
        self.col = int(altura/escala)
        self.filas = int(ancho/escala)
        self.size = (self.filas, self.col)
        self.matriz = np.ndarray(self.size)

    def ResetArray(self):
        for i in range(self.filas):
            for j in range(self.col):
                self.matriz[i][j] = 0

    def createArray(self):
        for i in range(self.filas):
            for j in range(self.col):
                self.matriz[i][j] = random.randint(0, 1)

    def suma_adj(self, i, j):
        ans = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                if(n != 0 or m != 0):
                    ans += self.matriz[(i+n+self.filas) %
                                       self.filas][(j+m+self.col) % self.col]
        return ans

    def algo(self, pantalla):
        for i in range(self.filas):
            for j in range(self.col):
                if self.matriz[i][j] == 1:
                    r = random.randint(50, 200)
                    g = random.randint(50, 200)
                    b = random.randint(50, 200)
                    pg.draw.rect(pantalla, (r, g, b), [
                                 i * self.escala, j * self.escala, self.escala, self.escala])
                else:
                    pg.draw.rect(pantalla, (0, 0, 0), [
                                 i * self.escala, j * self.escala, self.escala, self.escala])
        aux = np.ndarray(self.size)
        for i in range(self.filas):
            for j in range(self.col):
                celda = self.matriz[i][j]
                sum = self.suma_adj(i, j)
                aux[i][j] = celda
                if celda == 1 and sum < 2:
                    aux[i][j] = 0
                elif celda == 1 and (sum == 2 or sum == 3):
                    aux[i][j] = 1
                elif celda == 1 and sum > 3:
                    aux[i][j] = 0
                elif celda == 0 and sum == 3:
                    aux[i][j] = 1
        self.matriz = aux
