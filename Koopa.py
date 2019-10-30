import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from Timer import Timer
from Levels import *


class Koopa(Sprite):
    def __init__(self, screen, walk_list_left, walk_list_right, shell_list):
        super(Koopa, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # list to hold animation images
        self.walk_list_left = walk_list_left
        self.walk_list_right = walk_list_right
        self.shell_list = shell_list
        # self.x = self.rect.x
        # self.y = self.rect.y
        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list_left)
        self.animation = Timer(frames=self.walk_list_right)
        self.animation = Timer(frames=self.shell_list)

        # get the rect of the image
        self.imageLeft = self.animation.imagerect()
        self.imageRight = self.animation.imagerect()
        self.imageShell = self.animation.imagerect()
        self.rect = self.imageLeft.get_rect()
        self.rect = self.imageRight.get_rect()
        self.rect = self.imageShell.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.middle_x = float(self.rect.centerx)

        # movement flags
        self.moving_left = True
        self.moving_right = False
        self.direction = -2

        # shell flag
        self.shell_mode = False
        self.shell_mode_moving = False

        #collision flags
        self.floor = False
        self.brick = False
        self.obstacleL = False
        self.obstacleR = False

    def blitme(self):
        if self.moving_left:
            self.sur = self.imageLeft
            print(self.sur)
            print("moving left")
            self.screen.blit(self.imageLeft, self.rect)
        if self.moving_right:
            self.sur = self.imageRight
            self.screen.blit(self.imageRight, self.rect)
        # TODO: handle blitme when the koopa is in shell mode
        if self.shell_mode:
            self.sur = self.imageShell
            self.screen.blit(self.imageShell, self.rect)
        if self.shell_mode_moving:
            self.sur = self.imageShell
            self.screen.blit(self.imageShell, self.rect)

    def update(self, level):

        self.middle_x += (1 * self.direction)
        # (2 * self.direction)
        self.rect.x = self.middle_x

        if level.move:
            self.rect.left -= (SPEED + self.direction)
        else:

            if self.direction > 0:
                if self.obstacleR:
                    self.sur = self.imageLeft
                    self.direction *= -1
                    self.moving_left = True
                    self.moving_right = False
            elif self.direction < 0:
                if self.obstacleL:
                    self.sur = self.imageRight
                    self.direction *= -1
                    self.moving_right = True
                    self.moving_left = False

            if self.obstacleR and self.shell_mode_moving:
                self.sur = self.imageShell
                self.direction *= - 1
            if self.obstacleL and self.shell_mode_moving:
                self.sur = self.imageShell
                self.direction *= 1
            if self.moving_left:
                self.imageLeft = self.walk_list_left[self.animation.frame_index()]
            if self.moving_right:
                self.imageRight = self.walk_list_right[self.animation.frame_index()]
            # TODO: handle movement when turtle is in shell mode
            if self.shell_mode:
                self.moving_right = False
                self.moving_left = False
                self.direction = 0
                self.imageShell = self.shell_list[self.animation.frame_index()]
                print("static")
            elif self.shell_mode_moving:
                self.moving_right = False
                self.moving_left = False
                if self.direction == 2:
                    if self.obstacleR:
                        self.direction *= -1
                elif self.direction == -2:
                    if self.obstacleL:
                        self.direction *= -1
                self.imageShell = self.shell_list[self.animation.frame_index()]
                print("moving")


class RegularKoopa(Koopa):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("Images/enemies.png")
        self.koopas_left = []
        self.koopas_right = []
        self.koopas_shell = []
        imageRight = pygame.transform.scale(sprite_sheet.get_image(210, 0, 19, 25), (32, 32))
        self.koopas_right.append(imageRight)
        imageRight = pygame.transform.scale(sprite_sheet.get_image(240, 0, 19, 25), (32, 32))
        self.koopas_right.append(imageRight)
        imageLeft = pygame.transform.scale(sprite_sheet.get_image(179, 0, 19, 25), (32, 32))
        self.koopas_left.append(imageLeft)
        imageLeft = pygame.transform.scale(sprite_sheet.get_image(149, 0, 19, 25), (32, 32))
        self.koopas_left.append(imageLeft)
        imageShell = pygame.transform.scale(sprite_sheet.get_image(360, 0, 19, 25), (32, 32))
        self.koopas_shell.append(imageShell)
        imageShell = pygame.transform.scale(sprite_sheet.get_image(360, 0, 19, 25), (32, 32))
        self.koopas_shell.append(imageShell)
        super().__init__(screen=screen, walk_list_left=self.koopas_left, walk_list_right=self.koopas_right, shell_list=self.koopas_shell)