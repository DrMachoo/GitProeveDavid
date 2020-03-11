import pygame as pg
from Settings import *
import math



pg.init()

screen = pg.display.set_mode((Width, Height))

pg.display.set_caption(Titel)

clock = pg.time.Clock()




def redrawGameWindow():
    screen.blit(bg, (0,0))
    man.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pg.display.update()




#MainLoop
man = Player(390, 290, 64, 64)




bullets = []
run = True
while run:
    clock.tick(Fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < Width and bullet.x > 0 and bullet.y < Height and bullet.y > 0:
            bullet.update()

        else:
            bullets.pop(bullets.index(bullet))


    keys = pg.key.get_pressed()




    if keys[pg.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False

    if keys[pg.K_RIGHT] and man.x < Width - man.Pwidth - man.vel:
        man.x += man.vel

    if keys[pg.K_DOWN] and man.y < Height - man.Pheight - man.vel:
        man.y += man.vel
    if keys[pg.K_ESCAPE]:
        run = False

    elif keys[pg.K_UP] and man.y > man.vel:
        man.y -= man.vel


    else:
        man.standing = True
        man.walkCount = 0




    if event.type == pg.MOUSEBUTTONDOWN:
        mpos = pg.mouse.get_pos()
        mx, my = pg.mouse.get_pos()
        ppos = [man.x, man.y]
        px = ppos[0]
        py = ppos[1]
        vecx = mx - px
        vecy = my - py
        vecc = math.sqrt((vecx * vecx) + (vecy * vecy))
        xspeeed = vecx / vecc
        yspeeed = vecy / vecc
        print(xspeeed, yspeeed)

        if len(bullets) < 1  :
            bullets.append(projectile(round(man.x + man.Pwidth //2), round(man.y + man.Pheight//2), 6, Black, xspeeed, yspeeed))


    redrawGameWindow()





pg.quit()
