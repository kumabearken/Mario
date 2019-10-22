import pygame, sys
import constants
from pygame.locals import *
from timer import Timer


def check_events(mario, goomba):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event=event, mario=mario, goomba=goomba)
        elif event.type == pygame.KEYUP:
            check_keyup(event=event, mario=mario, goomba=goomba)


def check_keydown(event, mario, goomba):
    """ Respond to keypresses  """
    # Movement flags set to true
    if event.key == pygame.K_RIGHT or event.key == K_d:
        mario.moving_right = True
        mario.facing_right = True
        mario.facing_left = False
        goomba.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == K_a:
        mario.moving_left = True
        mario.facing_left = True
        mario.facing_right = False
        goomba.moving_left = True
    elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
        mario.is_jumping = True
        mario.jump()
    elif event.key == pygame.K_DOWN or event.key == K_s:
        # mario.crouch = True
        pass
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, mario, goomba):
    """ Respond to key releases """
    if event.key == pygame.K_RIGHT or event.key == K_d:
        mario.moving_right = False
        mario.facing_right = True
        goomba.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == K_a:
        mario.moving_left = False
        mario.facing_left = True
        goomba.moving_left = False
    elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
        mario.is_jumping = True
    elif event.key == pygame.K_DOWN or event.key == K_s:
        # mario.crouch = False
        pass

def check_mario_enemy_collision(mario, enemies):
    for enemy in enemies:
        if pygame.sprite.collide_rect(mario, enemy):
            if enemy.rect.top - 5 <= mario.rect.bottom <= enemy.rect.top + 5:
                enemies.remove(enemy)
            elif enemy.rect.left - 5 <= mario.rect.right <= enemy.rect.left + 5:
                print("HELP")

def update_mario(mario, enemies):
    mario.update()

    check_mario_enemy_collision(mario=mario, enemies=enemies)

def update_screen(screen, mario, enemies):
    screen.fill(constants.bg_color)
    mario.blitme()
    for enemy in enemies:
        enemy.blitme()
    pygame.display.flip()
