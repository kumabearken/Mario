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

LEVELS = ['LevelSettings1.txt', 'LevelSettings1-1.txt', 'LevelSettings2.txt']

pyg.init()
screen = pyg.display.set_mode((960,470),pyg.RESIZABLE)
pygame.display.set_caption("Super Mario Bros")
pyg.mixer.music.load('music/main_theme.ogg')
music_playing = False

# used for countdown timer each level
clock = 1000

# Create an instance to store game statistics and create scoreboard
stats = GameStats(constants=Constants)
sb = Scoreboard(constants=Constants, screen=screen, stats=stats)

mario = LittleMario(screen)
level = Level(screen)
level.create_rects(LEVELS[0])
goomba = Goomba(screen=screen)
goomba2 = Goomba(screen=screen)
goomba3 = Goomba(screen=screen)
goomba4 = Goomba(screen=screen)
goomba5 = Goomba(screen=screen)
goomba6 = Goomba(screen=screen)
goomba2.x = 1100
goomba3.x = 1500
goomba4.x = 1550
goomba5.x = 1750
goomba6.x = 1800
enemies = [goomba, goomba2, goomba3, goomba4, goomba5, goomba6]
koopa = RegularKoopa(screen=screen)
koopa2 = RegularKoopa(screen=screen)
koopa.middle_x = 700
koopa2.middle_x = 1000
koopas = [koopa, koopa2]
items = []
fireballs = Group()

while True:
    if not music_playing:
        pyg.mixer.music.play(-1, 0.0)
        music_playing = True
    if stats.time_left <= 0:
        sys.exit()
    gf.update_timer(clock=clock, constants=Constants, stats=stats, sb=sb)
    gf.check_events(screen=screen, mario=mario, fireballs=fireballs)
    gf.updateLevel(level=level, mario=mario)
    gf.update_koopas(koopas=koopas, level=level)
    gf.update_mario(mario=mario, screen=screen, enemies=enemies, items=items, stats=stats,
                    sb=sb, level=level, LEVELS=LEVELS)
    gf.update_item(items=items, level=level)
    gf.update_fireballs(fireballs=fireballs, level=level, enemies=enemies, stats=stats, sb=sb)
    gf.update_enemies(enemies=enemies, level=level)
    gf.check_collisiontype(mario=mario, level=level, LEVELS=LEVELS, items=items, screen=screen,
                           fireballs=fireballs)
    gf.check_collisiontype_goomba(level=level, enemies=enemies)
    gf.check_collisiontype_koopa(level=level, koopas=koopas)
    gf.edge_koopa_collision(koopas=koopas)
    gf.edge_goomba_collision(enemies=enemies)
    gf.check_koopa_enemy_collision(enemies=enemies, koopas=koopas)
    gf.check_mario_offstage(mario=mario, level=level, LEVELS=LEVELS)
    gf.update_screen(screen=screen, mario=mario, level=level, items=items, fireballs=fireballs,
                     enemies=enemies, sb=sb)

