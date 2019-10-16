import pygame
from pygame.sprite import Sprite
from spritesheet import *
from Timer import Timer

class Mario(Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.left = False
        self.right = False    

    def blitme(self):
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.screen.blit(self.image, self.rect)

    def update(self):
        if(self.left):
            self.rect.x -= 1
        if(self.right):
            self.rect.x += 1
            self.image = self.images[self.t.frame_index()]
            print(self.t.frame_index())

class LittleMario(Mario):
    def __init__(self,screen):
        super().__init__(screen=screen)
        self.ss = spritesheet('Images/mario.png')
        self.images=[]
        self.images = self.ss.images_at(((210,0,16,16), (240,0,16,16), (270,0,16,16),(300,0,16,16)), colorkey=None)
        #self.image = self.ss.image_at((210,0,16,16))
        #self.image = pygame.image.load('Images/a.png')
        self.t = Timer(self.images)
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.rect.x = 100
        self.rect.y = 100
