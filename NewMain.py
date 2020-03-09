import pygame as pg
from Settings import *


pg.init()

screen = pg.display.set_mode((Width, Height))

pg.display.set_caption(Titel)

clock = pg.time.Clock()

def redrawGameWindow():
    screen.blit(bg, (0,0))
    man.draw(screen)
    pg.display.update()
#MainLoop
man = Player(300, 410, 64, 64)
run = True
while run:
    clock.tick(Fps)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pg.K_RIGHT] and man.x < Width - man.Pwidth - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if keys[pg.K_UP] and man.y > man.vel:
        man.y -= man.vel
    if keys[pg.K_DOWN] and man.y < Height - man.Pheight - man.vel:
        man.y += man.vel
    if keys[pg.K_ESCAPE]:
        run = False


    redrawGameWindow()

pg.quit()