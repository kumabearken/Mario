import pygame
import Constants
from spritesheet import SpriteSheet
from Timer import Timer
from pygame.sprite import Sprite


class Fireball(Sprite):
    def __init__(self, screen, mario):
        super(Fireball, self).__init__()

        self.screen = screen
        self.fireballs = []
        self.mario = mario

        # load fireball images
        spritesheet = SpriteSheet("images/misc-8.png")
        image = pygame.transform.scale(spritesheet.get_image(26, 150, 8, 8), (16, 16))
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(41, 150, 8, 8), (16, 16))
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(26, 165, 8, 8), (16, 16))
        self.fireballs.append(image)
        image = pygame.transform.scale(spritesheet.get_image(41, 165, 8, 8), (16, 16))
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

        if mario.facing_right:
            self.x_direction = 1
        elif mario.facing_left:
            self.x_direction = -1
        self.y_velocity = -0.75

    def update(self):
        """ Move the fireball across the screen """
        # Update the decimal position of the bullet
        self.x += self.speed_factor * self.x_direction

        if self.rect.top <= self.mario.rect.y or self.rect.bottom >= Constants.WINDOW_HEIGHT:
            self.y_velocity *= -1

        self.y += self.speed_factor * self.y_velocity

        # Update the rect position
        self.rect.x = self.x
        self.rect.y = self.y

        # cycle through animation list
        self.image = self.fireballs[self.animation.frame_index()]

    def draw_fireball(self):
        """ Draw fireball to the screen """
        self.screen.blit(self.image, self.rect)

