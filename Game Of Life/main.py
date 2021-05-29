import pygame as pg
import board
import random
import numpy as np

pg.init()
main = 1
pg.display.set_caption("El Juego De la Vida")
ancho, alt = 1080//2, 1920//2
pantalla = pg.display.set_mode((ancho, alt))
ControladorTiempo = pg.time.Clock()
speed = escala = 10
tab = board.Board(alt, ancho, escala)
tab.createArray()
while main:
    ControladorTiempo.tick(speed)
    pantalla.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            main = 0
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                print("RESET TODO")
                tab.ResetArray()
                tab.createArray()
            if event.key == pg.K_x:
                print("Más")
                speed += 5
                speed = min(speed, 60)
            if event.key == pg.K_z:
                print("Menos")
                speed -= 5
                speed = max(speed, 1)
    tab.algo(pantalla)
    pg.display.update()

pg.quit()
