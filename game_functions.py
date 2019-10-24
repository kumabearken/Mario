import pygame, sys
import constants
from pygame.locals import *
from timer import Timer
from mario import SuperMario
from enemies import Goomba


def check_events(mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event=event, mario=mario)
        elif event.type == pygame.KEYUP:
            check_keyup(event=event, mario=mario)


def check_keydown(event, mario):
    """ Respond to keypresses  """
    # Movement flags set to true
    if event.key == pygame.K_RIGHT or event.key == K_d:
        mario.moving_right = True
        mario.facing_right = True
        mario.facing_left = False
    elif event.key == pygame.K_LEFT or event.key == K_a:
        mario.moving_left = True
        mario.facing_left = True
        mario.facing_right = False
    elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
        mario.is_jumping = True
        mario.jump()
    elif event.key == pygame.K_DOWN or event.key == K_s:
        mario.crouching = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, mario):
    """ Respond to key releases """
    if event.key == pygame.K_RIGHT or event.key == K_d:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == K_a:
        mario.moving_left = False
    elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
        mario.is_jumping = True
    elif event.key == pygame.K_DOWN or event.key == K_s:
        mario.crouching = False
        pass

def check_mario_enemy_collision(screen, mario, enemies):
    for enemy in enemies:
        #if pygame.sprite.collide_rect(mario, enemy):
        if mario.rect.colliderect(enemy):
            # base statement, if mario jumps on top of enemy, kills them
            if enemy.rect.top - 5 <= mario.rect.bottom <= enemy.rect.top + 5:
                enemies.remove(enemy)
            # mario touches enemy
            elif mario.rect.right >= enemy.rect.left and not mario.invincible:
                if mario.break_brick:
                    mario.become_small()
                    break
                # mario death, reset level
                # reset to beginning of level
                else:
                    mario.death_animation()
                    enemies.clear()
                    create_goomba(screen=screen,enemies=enemies)
                    mario.reset_level()

def check_mario_item_collision(screen, mario, items):
    for item in items:
        if pygame.sprite.collide_rect(mario, item):
            # make little mario into super mario
            mario.become_big()
            items.remove(item)

def create_goomba(screen, enemies):
    # create instance of Goomba class
    goomba = Goomba(screen=screen)
    enemies.append(goomba)


def update_mario(screen, mario, enemies, items):
    mario.update()

    check_mario_item_collision(screen=screen, mario=mario, items=items)
    check_mario_enemy_collision(screen=screen, mario=mario, enemies=enemies)

def update_enemies(enemies):
    for enemy in enemies:
        enemy.update()

def update_items(items):
    for item in items:
        item.update()

def update_screen(screen, mario, enemies, items):
    screen.fill(constants.bg_color)
    for item in items:
        item.blitme()
    mario.blitme()
    for enemy in enemies:
        enemy.blitme()
    pygame.display.flip()
