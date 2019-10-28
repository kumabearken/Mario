"""import pygame
import constants
import game_functions as gf
from mario import LittleMario, SuperMario
from enemies import Goomba
from items import Item, Mushroom, Flower
from scoreboard import Scoreboard
from stats import GameStats
from pygame.sprite import Group


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    screen.fill(constants.bg_color)
    pygame.display.set_caption("Super Mario Bros")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(constants=constants)
    sb = Scoreboard(constants=constants, screen=screen, stats=stats)

    mario = LittleMario(screen=screen)
   # super_mario = SuperMario(screen=screen)
    goomba = Goomba(screen=screen)
    enemies = [goomba]
    mushroom = Mushroom(screen=screen)
    flower = Flower(screen=screen)
    items = [mushroom, flower]
    fireballs = Group()

    while True:
        gf.check_events(screen=screen, mario=mario, fireballs=fireballs)
        gf.update_mario(screen=screen, mario=mario, enemies=enemies, items=items)
        gf.update_enemies(enemies=enemies)
        gf.update_items(items=items)
        gf.update_fireballs(fireballs=fireballs)
        gf.update_screen(screen=screen, sb=sb, mario=mario, enemies=enemies, items=items, fireballs=fireballs)


if __name__ == "__main__":
    main()
"""

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
#flower = Flower(screen=screen)
items = [mushroom]
fireballs = Group()

while True:
    gf.check_events(screen = screen, mario = mario, fireballs=fireballs)
    gf.updateLevel(level=level, mario =mario)
    gf.update_mario(mario=mario, screen=screen, enemies=enemies, items=items)
    gf.update_enemies(enemies=enemies)
    gf.update_items(items=items)
    gf.update_fireballs(fireballs=fireballs)
    gf.check_collisiontype(mario=mario, level=level, LEVELS=LEVELS)
    gf.check_mario_offstage(mario=mario, level=level, LEVELS = LEVELS)
    gf.update_screen(screen=screen, mario=mario, level=level, sb=sb, enemies=enemies, items=items, fireballs=fireballs)

