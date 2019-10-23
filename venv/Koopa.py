import pygame
from pygame.sprite import Sprite
from spritesheet import *
from Timer import Timer

class Koopa(Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.left = True
        self.right = False

    def check_collision(self,screen):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            self.left = True
        elif self.rect.left <= 0:
            self.right = True

    def blitme(self):
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.screen.blit(self.image, self.rect)

    def update(self):
        if(self.left) == True:
            self.rect.x -= 2
            self.image = self.imagesLeft[self.t.frame_index()]
            self.rect.x = self.rect.x
            print(self.t.frame_index())
        if(self.right) == True:
            self.rect.x += 3
            self.image = self.imagesRight[self.t.frame_index()]
            self.rect.x = self.rect.x
            print(self.t.frame_index())

class NormalKoopa(Koopa):
    def __init__(self,screen):
        super().__init__(screen=screen)
        '''handle moving right images'''
        self.ss = spritesheet('Images/enemies.png')
        self.imagesRight = []
        self.imagesRight = self.ss.images_at(((210,0,19,25), (240,0,19,25)), colorkey=None)
        self.t = Timer(self.imagesRight)
        self.image = self.imagesRight[0]
        self.rect = self.imagesRight[0].get_rect()

        '''handle moving left images'''
        self.ss = spritesheet('Images/enemies.png')
        self.imagesLeft = []
        self.imagesLeft = self.ss.images_at(((179,0,19,25), (149,0,19,25)), colorkey=None)
        self.t = Timer(self.imagesLeft)
        self.image = self.imagesLeft[0]
        self.rect = self.imagesLeft[0].get_rect()
        self.rect.x = 150
        self.rect.y = 150