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

import pygame
from pygame.sprite import Sprite
from Spritesheet import SpriteSheet
from timer import Timer


class Mario(Sprite):
    def __init__(self, screen, walk_right, walk_left, break_brick, invincible):
        super().__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.walk_right = walk_right
        self.walk_left = walk_left

        self.mario_right = Timer(frames=self.walk_right)
        self.mario_left = Timer(frames=self.walk_left)

        # get the rect of the image
        self.right_image = self.mario_right.imagerect()
        self.left_image = self.mario_left.imagerect()
        self.rect = self.right_image.get_rect()

        self.rect.x = self.screen_rect.x + 150
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.center = float(self.rect.centerx)

        # flags for movement and abilities
        self.jump_speed = 0
        self.moving_right = False
        self.moving_left = False
        self.facing_right = True
        self.facing_left = False
        self.is_jumping = False
        self.break_brick = break_brick
        self.invincible = invincible

        #ken implementataion
        self.floor = False
        self.brick = False
        self.obstacleL = False
        self.obstacleR = False

    def blitme(self):
        if self.facing_right:
            self.screen.blit(self.right_image, self.rect)
        elif self.facing_left:
            self.screen.blit(self.left_image, self.rect)

    def update(self):
        self.gravity()

        # animations for moving right and left: excludes last image in list (jump image)
        if self.moving_right and self.rect.right < self.screen_rect.right and not self.is_jumping:
            self.center += 5
            if self.mario_right.frame_index() != self.mario_right.lastframe:
                self.right_image = self.walk_right[self.mario_right.frame_index()]

        elif self.moving_left and self.rect.left > 0 and not self.is_jumping:
            self.center -= 5
            if self.mario_left.frame_index() != self.mario_left.lastframe:
                self.left_image = self.walk_left[self.mario_left.frame_index()]

        # if not moving, display standing frame
        elif not self.moving_right and self.facing_right and not self.is_jumping:
            self.right_image = self.walk_right[0]
        elif not self.moving_left and self.facing_left and not self.is_jumping:
            self.left_image = self.walk_left[0]

        # animation to handle "jump" case
        elif self.is_jumping and self.facing_right and self.moving_right:
            self.center += 5
            self.right_image = self.walk_right[-1]
        elif self.is_jumping and self.facing_left and self.moving_left:
            self.center -= 5
            self.left_image = self.walk_left[-1]

        self.rect.y += self.jump_speed

        # Update the rect object from self.center
        self.rect.centerx = self.center

    def jump(self):
        """ Function to handle when mario jumps """
        if self.rect.bottom >= self.screen_rect.bottom:
            self.jump_speed = -7

    def gravity(self):
        """ Function to calculate and handle gravity """
        if self.jump_speed == 0:
            self.jump_speed = 50
        else:
            self.jump_speed += .45

        # mario has landed on surface
        if self.rect.y >= self.screen_rect.bottom - self.rect.height and self.jump_speed >= 0:
            self.jump_speed = 0
            self.rect.y = self.screen_rect.bottom - self.rect.height
            self.is_jumping = False


class LittleMario(Mario):
    def __init__(self, screen):
        # list to hold all walking animations for right and left
        self.walk_right = []
        self.walk_left = []
        self.break_brick = False
        self.invincible = False

        # load right-facing images
        sprite_sheet = SpriteSheet("images/mario.png")
        image = pygame.transform.scale(sprite_sheet.get_image(210, 0, 15, 16), (32, 32))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(240, 0, 15, 16), (32, 32))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(270, 0, 15, 16), (32, 32))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(300, 0, 15, 16), (32, 32))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(360, 0, 15, 16), (32, 32))
        self.walk_right.append(image)

        # load left-facing images
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(210, 0, 15, 17), (32, 32)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(240, 0, 15, 17), (32, 32)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(270, 0, 15, 17), (32, 32)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(300, 0, 15, 17), (32, 32)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(360, 0, 15, 17), (32, 32)),
                                      True, False)
        self.walk_left.append(image)

        super().__init__(screen=screen, walk_right=self.walk_right, walk_left=self.walk_left,
                         break_brick=self.break_brick, invincible=self.invincible)


class SuperMario(Mario):
    def __init__(self, screen):
        self.walk_right = []
        self.walk_left = []

        # ability flags
        self.break_brick = True
        self.invincible = False

        # load right-facing images
        sprite_sheet = SpriteSheet("images/mario.png")
        image = pygame.transform.scale(sprite_sheet.get_image(210, 52, 16, 32), (32, 64))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(240, 52, 16, 32), (32, 64))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(270, 52, 16, 32), (32, 64))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(300, 52, 16, 32), (32, 64))
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(360, 52, 16, 32), (32, 64))
        self.walk_right.append(image)

        # load left-facing images
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(210, 52, 16, 32), (32, 64)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(240, 52, 16, 32), (32, 64)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(270, 52, 16, 32), (32, 64)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(300, 52, 16, 32), (32, 64)),
                                      True, False)
        self.walk_left.append(image)
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(360, 52, 16, 32), (32, 64)),
                                      True, False)
        self.walk_left.append(image)

        super().__init__(screen=screen, walk_right=self.walk_right, walk_left=self.walk_left,
                         break_brick=self.break_brick, invincible=self.invincible)

