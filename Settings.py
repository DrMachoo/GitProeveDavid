#game settings
import pygame as pg
from Sprites import *


class Player(object):
    def __init__(self, x, y, Pwidth, Pheight):
        self.x = x
        self.y = y
        self.Pwidth = Pwidth
        self.Pheight = Pheight
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0


    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x, self.y) )
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount // 3], (self.x, self.y) )
            self.walkCount += 1
        else:
            screen.blit(char, (self.x, self.y) )


Width = 1200
Height = 800
Fps = 60
vel = 10
Titel = ("MWDJ’s BowRain")

#Farver
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)


# Ikke slet please :)
# greater than >
# less than <