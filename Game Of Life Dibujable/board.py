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
        self.r = np.ndarray(self.size)
        self.g = np.ndarray(self.size)
        self.b = np.ndarray(self.size)
        self.offset = 1

    def ResetArray(self):
        for i in range(self.filas):
            for j in range(self.col):
                self.matriz[i][j] = 0
                self.r[i][j] = 100
                self.g[i][j] = 100
                self.b[i][j] = 100

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

    def draw(self, x, y):
        self.matriz[x][y] = not self.matriz[x][y]

    def algo(self, pantalla, flag):
        for i in range(self.filas):
            for j in range(self.col):
                if self.matriz[i][j] == 1:
                    if flag != 0:
                        self.r[i][j] = random.randint(50, 200)
                        self.g[i][j] = random.randint(50, 200)
                        self.b[i][j] = random.randint(50, 200)
                    pg.draw.rect(pantalla, (self.r[i][j], self.g[i][j], self.b[i][j]), [
                                 i * self.escala, j * self.escala, self.escala-self.offset, self.escala-self.offset])
                else:
                    pg.draw.rect(pantalla, (0, 0, 0), [
                                 i * self.escala, j * self.escala, self.escala-self.offset, self.escala-self.offset])
        if flag:
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
