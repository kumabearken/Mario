import pygame
import Constants
from spritesheet import SpriteSheet
from Timer import Timer
from pygame.sprite import Sprite
from Levels import *


class Fireball(Sprite):
    def __init__(self, screen, mario):
        super(Fireball, self).__init__()

        self.screen = screen
        self.fireballs = []
        self.mario = mario

        # load fireball images
        spritesheet = SpriteSheet("images/misc-8.png")
        image = pygame.transform.scale(spritesheet.get_image(26, 150, 8, 8), (16, 16)) # movement[0]
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(41, 150, 8, 8), (16, 16)) # movement[1]
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(26, 165, 8, 8), (16, 16)) # movement[2]
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(41, 165, 8, 8), (16, 16)) # movement[3]
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(364, 188, 8, 8), (16, 16)) # explosion[4]
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(392, 185, 12, 14), (24, 28)) # explosion[5]
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(420, 184, 16, 16), (32, 32)) #explosion[6]
        self.fireballs.append(image)

        self.animation = Timer(frames=self.fireballs)
        # get the rect of the image
        self.image = self.animation.imagerect()
        self.rect = self.image.get_rect()
        self.rect.centerx = mario.rect.centerx
        self.rect.y = mario.rect.centery

        # Store the fireballs's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor = Constants.fireball_speed

        self.y_position = self.rect.y

        if mario.facing_right:
            self.x_direction = 1
        elif mario.facing_left:
            self.x_direction = -1
        self.y_velocity = 0.75

        self.exploding = False

    def update(self, level, fireballs):
        """ Move the fireball across the screen """
        if level.move:
            self.rect.left -= SPEED


        if self.exploding:
            if 3 < self.animation.frame_index() < len(self.animation.frames):
                self.image = self.fireballs[self.animation.frame_index()]
            else:
                print("gone")
                self.exploding = False
                fireballs.remove(self)
        else:
            # cycle through animation list
            if self.animation.frame_index() < 4:
                self.image = self.fireballs[self.animation.frame_index()]

            # Update the decimal position of the bullet
            self.x += self.speed_factor * self.x_direction

            if self.rect.top <= self.y_position - 30:
                self.y_velocity *= -1
            self.y += self.speed_factor * self.y_velocity

            # Update the rect position
            self.rect.x = self.x
            self.rect.y = self.y

    def draw_fireball(self):
        """ Draw fireball to the screen """
        self.screen.blit(self.image, self.rect)

    def explode(self):
        self.exploding = True
        self.animation.frameindex = 4

