import pygame
from spritesheet import SpriteSheet
from Timer import Timer
REAL = True

class Brick():
    def __init__(self, width, height, x, y):
        self.sur = pygame.Surface((width, height))
        self.rect = self.sur.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sprite_sheet = pygame.image.load("Images/custom.png")

class Pipe(Brick):
    def __init__(self,width, height, x,y,item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((0,0,0))
        self.breakable= False
        self.items = item
        self.interactable = False

class InteractableH(Brick):
    def __init__(self, width, height, x, y,item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((100, 100, 100))
        self.breakable = False
        self.items = item
        self.interactable = True

class InteractableV(Brick):
    def __init__(self, width, height, x, y, item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((100, 100, 100))
        self.breakable = False
        self.items = item
        self.interactable = True

class Basic(Brick):
    def __init__(self, width, height, x, y, item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur = pygame.Surface((16, 16))
        self.sur.blit(self.sprite_sheet, (0, 0), (48, 0, 16, 16))
        self.sur = pygame.transform.scale2x(self.sur)
        self.breakable = True
        self.items = item

class Question(Brick):
    def __init__(self, width, height, x, y, item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur = pygame.Surface((16,16))
        self.sur.blit(self.sprite_sheet,(0,0), (0,0,16,16))
        self.sur = pygame.transform.scale2x(self.sur)
        self.breakable = False
        self.active =True
        self.items = item

class Floor(Brick):
    def __init__(self,width, height, x,y, item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((188,182,168))
        self.breakable= False
        self.items = item
        self.interactable = False

class Flag(Brick):
    def __init__(self,width, height, x,y,item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((0,182,168))
        self.breakable = False
        self.items = item
        self.interactable = False