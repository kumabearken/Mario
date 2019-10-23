import pygame as pyg
import GameFunctions as gf
from Mario import *
from Koopa import *
import os
import sys
import time


def run_game():

    pyg.init()
    screen = pyg.display.set_mode((460,460),pyg.RESIZABLE)

    mario = LittleMario(screen)
    koopa = NormalKoopa(screen)

    while True:
        gf.check_events(screen = screen, mario = mario)
        gf.updateMario(mario=mario)
        gf.updateKoopa(koopa=koopa)
        gf.checkCollideKoopa(screen=screen, koopa=koopa)
        gf.updateScreen(screen = screen, mario = mario, koopa = koopa)
        time.sleep(.05)

run_game()