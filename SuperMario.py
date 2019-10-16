import pygame as pyg
import GameFunctions as gf
from Mario import *
import os
import sys
import time

pyg.init()
screen = pyg.display.set_mode((460,460),pyg.RESIZABLE)

mario = LittleMario(screen)

while True:
    gf.check_events(screen = screen, mario = mario)
    gf.updateMario(mario=mario)
    gf.updateScreen(screen = screen, mario = mario)
    time.sleep(.05)
