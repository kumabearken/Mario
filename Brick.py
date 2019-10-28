import pygame
REAL = False

class Brick():
    def __init__(self, width, height, x, y):
        self.sur = pygame.Surface((width, height))
        self.rect = self.sur.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pipe(Brick):
    def __init__(self,width, height, x,y,item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((50,50,50))
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
        self.sur.fill((150,150,150))
        self.breakable = True
        self.items = item

class Question(Brick):
    def __init__(self, width, height, x, y, item):
        super().__init__(width, height, x, y)
        if REAL:
            self.sur.set_alpha(0)
        self.sur.fill((200,200,200))
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