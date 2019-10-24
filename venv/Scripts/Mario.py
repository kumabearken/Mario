import pygame
from pygame.sprite import Sprite
from spritesheet import *
from Timer import Timer

class Mario(Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.left = False
        self.right = False
        self.floor = False
        self.brick = False
        self.obstacleL = False
        self.obstacleR = False

    def blitme(self):
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.screen.blit(self.image, self.rect)

    def update(self):
        if not self.floor:
            self.rect.y += GRAVITY
            print("gravity")
        if self.rect.x <= 480:
            if(self.left and not self.obstacleL):
                self.rect.x -= 5
            if(self.right and not self.obstacleR):
                self.rect.x += 5
                self.image = self.images[self.t.frame_index()]
                print(self.t.frame_index())
        else:
            if(self.left and not self.obstacleL):
                self.rect.x -= 5
            if(self.right and not self.obstacleR):
                self.image = self.images[self.t.frame_index()]
                print(self.t.frame_index())
        self.floor = False
        self.obstacleR = False
        self.obstacleL = False

class LittleMario(Mario):
    def __init__(self,screen):
        super().__init__(screen=screen)
        self.ss = spritesheet('Images/mario.png')
        self.images=[]
        self.images = self.ss.images_at(((210,0,16,16), (240,0,16,16), (270,0,16,16),(300,0,16,16)), colorkey=None)
        self.t = Timer(self.images)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
