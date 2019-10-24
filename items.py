import pygame
from pygame.sprite import Sprite
from Spritesheet import SpriteSheet


class Item(Sprite):
    def __init__(self, screen, image):
        super(Item, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # get the rect image
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx - 200
        self.rect.bottom = self.screen_rect.bottom

        self.direction = 1

        # store objects exact position
        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # CHANGE MOVEMENT (TESTING FOR MUSHROOM)
        self.center += (2 * self.direction)
        self.rect.x = self.center

        if self.rect.right >= self.screen_rect.right:
            self.direction *= -1
        elif self.rect.left <= 0:
            self.direction *= -1


class Mushroom(Item):
    def __init__(self, screen):
        spritesheet = SpriteSheet("images/items.png")

        # get the rect of the image
        self.image = pygame.transform.scale(spritesheet.get_image(184, 34, 16, 16), (24, 24))
        super().__init__(screen=screen, image=self.image)

