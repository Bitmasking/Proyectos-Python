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
uwux = ancho/(ancho/escala)
uwuy = alt/(ancho/escala)
tab = board.Board(alt, ancho, escala)
flag = 0
tab.ResetArray()
while main:
    ControladorTiempo.tick(speed)
    pantalla.fill((25, 25, 25))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            main = 0
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                print("RESET TODO")
                tab.ResetArray()
            if event.key == pg.K_p:
                print("PAUSA")
                flag = not flag
            if event.key == pg.K_x:
                print("Más")
                speed += 5
                speed = min(speed, 60)
            if event.key == pg.K_z:
                print("Menos")
                speed -= 5
                speed = max(speed, 1)
    mm = pg.mouse.get_pressed()
    if sum(mm) > 0:
        if not mm[1]:
            print("Mouse Pressed")
            mmx, mmy = pg.mouse.get_pos()
            tab.draw(int(np.floor(mmx/(escala))),
                     int(np.floor(mmy/(escala))))

    tab.algo(pantalla, flag)
    pg.display.update()

pg.quit()
