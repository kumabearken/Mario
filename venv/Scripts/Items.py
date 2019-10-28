import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from Timer import Timer


class Item(Sprite):
    def __init__(self, screen, image_list, center_start):
        super(Item, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image_list = image_list

        self.animation = Timer(frames=self.image_list)

        # get the rect image
        self.image = self.animation.imagerect()
        self.rect = self.image.get_rect()

        self.rect.centerx = center_start
        self.rect.y = 400

        self.direction = -1

        # store objects exact position
        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Mushroom(Item):
    def __init__(self, screen):
        spritesheet = SpriteSheet("images/items.png")
        self.mushroom = []

        # get the rect of the image
        image = pygame.transform.scale(spritesheet.get_image(184, 34, 16, 16), (24, 24))
        self.mushroom.append(image)
        super().__init__(screen=screen, image_list=self.mushroom, center_start=500)

    def update(self):
        # CHANGE MOVEMENT (TESTING FOR MUSHROOM)
        self.center += (2 * self.direction)
        self.rect.x = self.center

        if self.rect.right >= self.screen_rect.right:
            self.direction *= -1
        elif self.rect.left <= 0:
            self.direction *= -1


class Flower(Item):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("images/items.png")

        self.flowers = []
        image = pygame.transform.scale(sprite_sheet.get_image(0, 64, 20, 16), (32, 32))
        self.flowers.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(34, 64, 20, 16), (32, 32))
        self.flowers.append(image)

        super().__init__(screen=screen, image_list=self.flowers, center_start=400)

