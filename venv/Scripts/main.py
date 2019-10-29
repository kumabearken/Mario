import pygame as pyg
import GameFunctions as gf
from Mario import *
import os
import sys
import time
from  Levels import *
import Constants
from Enemies import *
from Items import *
from Scoreboard import Scoreboard
from Stats import GameStats
from pygame.sprite import Group
LEVELS = ['LevelSettings1.txt','LevelSettings1-1.txt']

pyg.init()
screen = pyg.display.set_mode((960,470),pyg.RESIZABLE)
pygame.display.set_caption("Super Mario Bros")

# Create an instance to store game statistics and create scoreboard
stats = GameStats(constants=Constants)
sb = Scoreboard(constants=Constants, screen=screen, stats=stats)

# Create Mario, enemy, items, fireball objects
mario = LittleMario(screen)
level = Level(screen)
level.create_rects(LEVELS[0])
goomba = Goomba(screen=screen)
enemies = [goomba]
mushroom = Mushroom(screen=screen)
flower = Flower(screen=screen)
items = [flower, mushroom]
fireballs = Group()

while True:
    gf.check_events(screen = screen, mario = mario, fireballs=fireballs)
    gf.updateLevel(level=level, mario =mario)
    gf.update_mario(mario=mario, screen=screen, enemies=enemies, items=items)
    gf.update_enemies(enemies=enemies)
    gf.update_items(items=items)
    gf.update_fireballs(fireballs=fireballs, level=level, enemies=enemies)
    gf.check_collisiontype(mario=mario, level=level, LEVELS=LEVELS, fireballs=fireballs)
    gf.check_mario_offstage(mario=mario, level=level, LEVELS = LEVELS)
    gf.update_screen(screen=screen, mario=mario, level=level, sb=sb, enemies=enemies, items=items, fireballs=fireballs)

