import pygame
import time
from pygame.sprite import Sprite
from Spritesheet import SpriteSheet
from timer import Timer


class Mario(Sprite):
    def __init__(self, screen, walk_right, walk_left):
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
        self.crouching = False
        self.break_brick = False
        self.invincible = False

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
            if self.mario_right.frame_index() < self.mario_right.lastframe - 1:
                self.right_image = self.walk_right[self.mario_right.frame_index()]

        elif self.moving_left and self.rect.left > 0 and not self.is_jumping:
            self.center -= 5
            if self.mario_left.frame_index() < self.mario_left.lastframe - 1:
                self.left_image = self.walk_left[self.mario_left.frame_index()]

        # if not moving, display standing frame
        elif not self.moving_right and self.facing_right and not self.is_jumping:
            self.right_image = self.walk_right[0]
        elif not self.moving_left and self.facing_left and not self.is_jumping:
            self.left_image = self.walk_left[0]

        # animation to handle "jump" case
        elif self.is_jumping and self.facing_right:
            if self.moving_right:
                self.center += 5
            self.right_image = self.walk_right[-2]
        elif self.is_jumping and self.facing_left:
            if self.moving_left:
                self.center -= 5
            self.left_image = self.walk_left[-2]

        self.rect.y += self.jump_speed

        # display crouching image
        if self.crouching and self.break_brick:
            self.crouch()

        # Update the rect object from self.center
        self.rect.centerx = self.center

    def crouch(self):
        """ # store objects exact position
                    self.x = float(self.rect.centerx)"""
        # get crouch image rect and set bottom to be bottom of screen
        if self.facing_right:
            image = self.walk_right[-1]
            self.rect = image.get_rect()
            self.rect.bottom = self.screen_rect.bottom
            self.right_image = image
        elif self.facing_left:
            image = self.walk_left[-1]
            self.rect = image.get_rect()
            self.rect.bottom = self.screen_rect.bottom
            self.left_image = image

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

    def become_big(self):
        """ Function to make Mario Big if interacted with mushroom """
        big_mario = SuperMario(screen=self.screen)
        self.break_brick = True
        # set the frames to that of big mario
        self.walk_right = big_mario.walk_right
        self.walk_left = big_mario.walk_left

        # get the rect of the new image
        self.image = self.walk_right[0]
        self.rect = self.image.get_rect()

        # place in same spot as powerup
        self.rect.x = self.center
        self.rect.bottom = self.screen_rect.bottom

    def become_small(self):
        """ Function to make Mario small if interact with enemy"""
        little_mario = LittleMario(screen=self.screen)
        self.break_brick = False
        # set the frames to that of little mario
        self.walk_right = little_mario.walk_right
        self.walk_left = little_mario.walk_left

        # get the rect of the new image
        self.image = self.walk_right[0]
        self.rect = self.image.get_rect()

        # place in same spot as powerup
        self.rect.x = self.center
        self.rect.bottom = self.screen_rect.bottom
        self.invincible = True

    def death_animation(self):
        """ Function to run mario death animation """
        print("rip mario")

    def reset_level(self):
        """ Function to reset Mario's position upon new level"""
        #time.sleep(1.0)
        self.rect.x = self.screen_rect.x + 150
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

class LittleMario(Mario):
    """ Class to define little/default Mario """
    def __init__(self, screen):
        # list to hold all walking animations for right and left
        self.walk_right = []
        self.walk_left = []

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
        image = pygame.transform.scale(sprite_sheet.get_image(360, 0, 15, 16), (32, 32)) # jump
        self.walk_right.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(390, 16, 15, 14), (32, 32)) # dead
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
        image = pygame.transform.scale(sprite_sheet.get_image(390, 16, 15, 14), (32, 32))  # dead
        self.walk_left.append(image)

        super().__init__(screen=screen, walk_right=self.walk_right, walk_left=self.walk_left)


class SuperMario(Mario):
    """ Class to define Super Mario """
    def __init__(self, screen):
        self.walk_right = []
        self.walk_left = []

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
        # jump image walk_right[-2]
        image = pygame.transform.scale(sprite_sheet.get_image(360, 52, 16, 32), (32, 64))
        self.walk_right.append(image)
        # crouch image walk_right[-1]
        image = pygame.transform.scale(sprite_sheet.get_image(390, 52, 16, 27), (32, 54))
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
        # jump image walk_left[-2]
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(360, 52, 16, 32), (32, 64)),
                                      True, False)
        self.walk_left.append(image)
        # crouch image walk_right[-1]
        image = pygame.transform.flip(pygame.transform.scale(sprite_sheet.get_image(390, 52, 16, 27), (32, 54)),
                                      True, False)
        self.walk_left.append(image)

        super().__init__(screen=screen, walk_right=self.walk_right, walk_left=self.walk_left)

