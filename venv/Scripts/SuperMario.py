import pygame as pyg
import GameFunctions as gf
from Mario import *
import os
import sys
import time
from  Levels import *
pyg.init()
screen = pyg.display.set_mode((960,470),pyg.RESIZABLE)

mario = LittleMario(screen)
level = Level(screen)
level.create_rects()

while True:
    gf.check_events(screen = screen, mario = mario)
    gf.updateMario(mario=mario)
    gf.updateLevel(level=level, mario =mario)
    gf.check_collisiontype(mario=mario, level=level)
    gf.updateScreen(screen = screen, mario = mario, level = level)

