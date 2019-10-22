import pygame
import constants


class SpriteSheet(object):
    """ Class used to grab images from sprite sheet """
    sprite_sheet = None

    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        """ Grabs one image from sprite sheet """
        image = pygame.Surface([width, height]).convert()
        image.set_colorkey(constants.BLACK)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
