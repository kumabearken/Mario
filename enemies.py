import pygame
from pygame.sprite import Sprite
from Spritesheet import SpriteSheet
from timer import Timer


class Enemy(Sprite):
    def __init__(self, screen, walk_list):
        super(Enemy, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # list to hold animation images
        self.walk_list = walk_list

        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list)

        # get the rect of the image
        self.image = self.animation.imagerect()
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.x = float(self.rect.centerx)

        # movement flags
        self.moving_left = False
        self.moving_right = False
        self.direction = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (2 * self.direction)
        self.rect.x = self.x
        self.image = self.walk_list[self.animation.frame_index()]

        if self.rect.right >= self.screen_rect.centerx + 150:
            self.direction *= -1
        elif self.rect.left <= self.screen_rect.centerx - 150:
            self.direction *= -1


class Goomba(Enemy):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("images/enemies.png")
        self.goombas = []
        image = pygame.transform.scale(sprite_sheet.get_image(0, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(30, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        # next image for squished goomba
        """image = pygame.transform.scale(sprite_sheet.get_image(60, 5, 16, 16), (30, 30))
        self.goombas.append(image)"""
        super().__init__(screen=screen, walk_list=self.goombas)

