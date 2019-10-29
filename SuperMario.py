import pygame as pyg
import GameFunctions as gf
from Mario import *
import os
import sys
import time
from  Levels import *
import Constants
from Items import *
from pygame.sprite import Group
from Koopa import *
from Enemies import *
from Scoreboard import Scoreboard
from Stats import GameStats

LEVELS = ['LevelSettings1.txt','LevelSettings1-1.txt','LevelSettings2.txt']



pyg.init()
screen = pyg.display.set_mode((960,470),pyg.RESIZABLE)
pygame.display.set_caption("Super Mario Bros")

# Create an instance to store game statistics and create scoreboard
stats = GameStats(constants=Constants)
sb = Scoreboard(constants=Constants, screen=screen, stats=stats)

mario = LittleMario(screen)
level = Level(screen)
level.create_rects(LEVELS[0])
items = []
enemies = []
fireballs = Group()

while True:
    gf.check_events(screen = screen, mario = mario, fireballs=fireballs)
    gf.updateLevel(level=level, mario =mario)
    gf.update_mario(mario=mario,screen=screen,enemies=enemies,items=items)
    gf.update_item(items=items, level=level)
    gf.update_fireballs(fireballs=fireballs, level=level, enemies=enemies)
    gf.update_enemies(enemies=enemies,level=level)
    #gf.check_mario_item_collision(screen=screen, mario=mario, items=items)
    gf.check_collisiontype(mario=mario, level=level, LEVELS=LEVELS, items=items, screen=screen, fireballs=fireballs)
    gf.check_mario_offstage(mario=mario, level=level, LEVELS = LEVELS)
    gf.update_screen(screen = screen, mario = mario, level = level, items=items, fireballs=fireballs, enemies=enemies,sb=sb)

