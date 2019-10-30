import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from Timer import Timer
from Levels import *


class Enemy(Sprite):
    def __init__(self, screen, walk_list, squashed_list):
        super(Enemy, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # list to hold animation images
        self.walk_list = walk_list
        self.squashed_list = squashed_list

        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list)

        # get the rect of the image
        self.image = self.animation.imagerect()
        self.rect = self.image.get_rect()
        self.squashed_image = self.animation.imagerect()
        self.rect = self.squashed_image.get_rect()

        self.sur = pygame.Surface((32,32))

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        # movement flags
        self.death_jump = 0
        self.moving_left = True
        self.moving_right = False
        self.direction = -1

        #collision flags
        self.floor = False
        self.brick = False
        self.obstacleL = False
        self.obstacleR = False

        # death flag
        self.died = False
        self.squashed = False

    def blitme(self):
        if self.died:
            self.sur = self.image
            self.screen.blit(pygame.transform.flip(self.image, False, True), self.rect)
        if not self.died and not self.squashed:
            self.sur = self.image
            self.screen.blit(self.image, self.rect)
        if self.squashed:
            self.sur = self.squashed_image
            self.screen.blit(self.squashed_image, self.rect)

    def update(self, level):
        self.x += (2 * self.direction)
        self.rect.x = self.x
        # self.image = self.walk_list[self.animation.frame_index()]

        if level.move:
            level.SPEED = 20
            self.rect.left -= (SPEED + self.direction)

        else:

            if not self.died and not self.squashed:
                self.image = self.walk_list[self.animation.frame_index()]
                if self.direction > 0:
                    if self.obstacleR:
                        self.direction *= -1
                        self.moving_left = True
                        self.moving_right = False
                        print("going left")
                elif self.direction < 0:
                    if self.obstacleL:
                        self.direction *= -1
                        self.moving_left = False
                        self.moving_right = True
                        print("going right")

            if self.died:
                self.direction = 0
                self.image = self.walk_list[self.animation.frame_index()]
                if self.rect.bottom >= self.screen_rect.bottom:
                    self.death_jump = -7
                    # self.rect.y += self.death_jump
                    if self.death_jump != 0:
                        self.death_jump += 8
                        print("goes here")
                        self.rect.y += self.death_jump

            if self.squashed:
                self.direction = 0
                self.squashed_image = self.squashed_list[self.animation.frame_index()]

                # self.rect.y += self.death_jump


class Goomba(Enemy):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("images/enemies.png")
        self.goombas = []
        self.goombas_squashed = []
        image = pygame.transform.scale(sprite_sheet.get_image(0, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(30, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        squashed_image = pygame.transform.scale(sprite_sheet.get_image(60, 4, 16, 16), (32, 32))
        self.goombas_squashed.append(squashed_image)
        squashed_image = pygame.transform.scale(sprite_sheet.get_image(60, 4, 16, 16), (32, 32))
        self.goombas_squashed.append(squashed_image)
        # next image for squished goomba
        """image = pygame.transform.scale(sprite_sheet.get_image(60, 5, 16, 16), (30, 30))
        self.goombas.append(image)"""
        super().__init__(screen=screen, walk_list=self.goombas, squashed_list=self.goombas_squashed)
