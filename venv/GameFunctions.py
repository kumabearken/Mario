import pygame
import sys

WHITE = (255, 255, 255)


def check_events(screen, mario):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event=event, mario=mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event=event, mario=mario)


def check_keydown_events(event, mario):
    '''Respond to keypresse.'''
    if event.key == pygame.K_RIGHT:
        mario.right = True
        print('right')
    elif event.key == pygame.K_LEFT:
        mario.left = True
        print('left')
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, mario):
    '''Respond to keypresse.'''
    if event.key == pygame.K_RIGHT:
        mario.right = False
    elif event.key == pygame.K_LEFT:
        mario.left = False

def checkCollideKoopa(screen, koopa):
    koopa.check_collision(screen)

def updateMario(mario):
    mario.update()

def updateKoopa(koopa):
    koopa.update()

def updateScreen(screen, mario, koopa):
    screen.fill(WHITE)
    mario.blitme()
    koopa.blitme()
    pygame.display.flip()
