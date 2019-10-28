import pygame as pyg
import GameFunctions as gf
from Mario import *
import os
import sys
import time
from  Levels import *
import constants
LEVELS = ['LevelSettings1.txt','LevelSettings1-1.txt']



pyg.init()
screen = pyg.display.set_mode((960,470),pyg.RESIZABLE)
screen.fill(constants.bg_color)

mario = LittleMario(screen)
level = Level(screen)
level.create_rects(LEVELS[0])
#goomba = Goomba(screen=screen)
#enemies = [goomba]

while True:
    gf.check_events(screen = screen, mario = mario)
    gf.updateLevel(level=level, mario =mario)
    gf.update_mario(mario=mario)
    gf.check_collisiontype(mario=mario, level=level, LEVELS=LEVELS)
    gf.check_mario_offstage(mario=mario, level=level, LEVELS = LEVELS)
    print(mario.rect)
    gf.update_screen(screen = screen, mario = mario, level = level)

