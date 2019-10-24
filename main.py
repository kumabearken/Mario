import pygame
import constants
import game_functions as gf
from mario import LittleMario, SuperMario
from enemies import Goomba
from items import Item, Mushroom


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    screen.fill(constants.bg_color)
    pygame.display.set_caption("Super Mario Bros")
    mario = LittleMario(screen=screen)
   # super_mario = SuperMario(screen=screen)
    goomba = Goomba(screen=screen)
    enemies = [goomba]
    mushroom = Mushroom(screen=screen)
    items = [mushroom]

    while True:
        gf.check_events(mario=mario)
        gf.update_mario(screen=screen, mario=mario, enemies=enemies, items=items)
        gf.update_enemies(enemies=enemies)
        gf.update_items(items=items)
        gf.update_screen(screen=screen, mario=mario, enemies=enemies, items=items)


if __name__ == "__main__":
    main()
