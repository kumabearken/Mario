import pygame, sys
import time
import Constants
from pygame.locals import *
from Timer import Timer
from Mario import *
from Enemies import *
from Items import *
from Fireball import Fireball
from pygame.sprite import Group

def check_events(mario, screen, fireballs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event=event, screen=screen, mario=mario, fireballs=fireballs)
        elif event.type == pygame.KEYUP:
            check_keyup(event=event, mario=mario)


def check_keydown(event, screen, mario, fireballs):
    """ Respond to keypresses  """
    # Movement flags set to true
    if not mario.dead:
        if event.key == pygame.K_RIGHT or event.key == K_d:
            mario.moving_right = True
            mario.facing_right = True
            mario.facing_left = False
            mario.moving_left = False
        elif event.key == pygame.K_LEFT or event.key == K_a:
            mario.moving_left = True
            mario.facing_left = True
            mario.facing_right = False
            mario.moving_right = False
        elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
            mario.is_jumping = True
            mario.jump()
        elif event.key == pygame.K_DOWN or event.key == K_s:
            if mario.break_brick:
                mario.crouching = True
        elif pygame.key.get_mods() == pygame.KMOD_LSHIFT:
            if mario.fire:
                throw_fireball(screen=screen, mario=mario, fireballs = fireballs)

    if event.key == pygame.K_q:
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


def check_mario_enemy_collision(screen, mario, enemies):
    for enemy in enemies:
        #if pygame.sprite.collide_rect(mario, enemy):
        if mario.rect.colliderect(enemy) and not mario.dead:
            # base statement, if mario jumps on top of enemy, kills them
            if enemy.rect.top - 5 <= mario.rect.bottom <= enemy.rect.top + 5:
                print("hit")
                enemies.remove(enemy)
            # mario touches enemy and dies
            elif mario.rect.right >= enemy.rect.left and not mario.invincible:
                if mario.break_brick:
                    mario.become_small()
                    break
                # mario death, reset level
                # reset to beginning of level
                else:
                    mario.death_animation()

    # if mario is ever below the screen height, reset, the level
    if mario.rect.top >= Constants.WINDOW_HEIGHT:
        enemies.clear()
        create_goomba(screen=screen,enemies=enemies)
        mario.reset_level()

def check_mario_item_collision(screen, mario, items):
    for item in items:
        if pygame.sprite.collide_rect(mario, item):
            if type(item) is Mushroom:
                # make little mario into super mario
                mario.become_big()
            elif type(item) is Flower:
                # make super mario into Fire Mario
                mario.become_fire_mario()
            items.remove(item)

def create_goomba(screen, enemies):
    # create instance of Goomba class
    goomba = Goomba(screen=screen)
    enemies.append(goomba)

def check_collisiontype(level, mario, LEVELS):
    for blocks in level.environment:
        if (pygame.sprite.collide_rect(mario, blocks)):
            #floor==========================================================================================
            if not mario.dead:
                if str(type(blocks)) == "<class 'Brick.Floor'>" and mario.rect.bottom >= blocks.rect.top:
                    mario.floor=True
                    if not mario.break_brick:
                        mario.rect.y = blocks.rect.y - 32
                    else:
                        mario.rect.y = blocks.rect.y - 64

            #sides===========================================================================================
            #PIPE-------------------------------------------------------------------------------------------
            if str(type(blocks)) == "<class 'Brick.Pipe'>" \
                    and (mario.rect.left <= blocks.rect.right or mario.rect.right >= blocks.rect.left) \
                    and mario.rect.bottom > blocks.rect.top\
                    and mario.rect.top > blocks.rect.top-16:
                if mario.rect.right >= blocks.rect.left \
                        and not mario.obstacleL\
                        and mario.rect.left < blocks.rect.left:
                    mario.rect.right = blocks.rect.left -1
                    mario.obstacleR = True
                else:
                    mario.obstacleR = False
                if mario.rect.left <= blocks.rect.right \
                    and not mario.obstacleR\
                    and mario.rect.right > blocks.rect.right:
                    print( "mario.rect " + str(mario.rect))
                    mario.rect.left = blocks.rect.right + 1
                    mario.obstacleL = True
                    print("block.rect " + str(blocks.rect))
                    print("culprit 5")
                else:
                    mario.obstacleL = False
            #BASIC--------------------------------------------------------------------------------------------
            elif str(type(blocks)) == "<class 'Brick.Basic'>" \
                    and (mario.rect.left <= blocks.rect.right or mario.rect.right >= blocks.rect.left) \
                    and mario.rect.bottom > blocks.rect.top\
                    and mario.rect.top > blocks.rect.top-16\
                    and mario.rect.bottom <= blocks.rect.bottom:
                if mario.rect.right >= blocks.rect.left \
                        and not mario.obstacleL\
                        and mario.rect.left < blocks.rect.left:
                    mario.rect.right = blocks.rect.left -1
                    mario.obstacleR = True
                else:
                    mario.obstacleR = False
                if mario.rect.left <= blocks.rect.right \
                    and not mario.obstacleR\
                    and mario.rect.right > blocks.rect.right:
                    mario.rect.left = blocks.rect.right + 1
                    mario.obstacleL = True
                    print("culprit 4")
                else:
                    mario.obstacleL = False
            #QUESTION------------------------------------------------------------------------------------------
            elif str(type(blocks)) == "<class 'Brick.Question'>" \
                    and (mario.rect.left <= blocks.rect.right or mario.rect.right >= blocks.rect.left) \
                    and mario.rect.bottom > blocks.rect.top\
                    and mario.rect.top > blocks.rect.top-16\
                    and mario.rect.bottom <= blocks.rect.bottom:
                if mario.rect.right >= blocks.rect.left \
                        and not mario.obstacleL\
                        and mario.rect.left < blocks.rect.left:
                    mario.rect.right = blocks.rect.left -1
                    mario.obstacleR = True
                else:
                    mario.obstacleR = False
                if mario.rect.left <= blocks.rect.right \
                    and not mario.obstacleR\
                    and mario.rect.right > blocks.rect.right:
                    mario.rect.left = blocks.rect.right + 1
                    mario.obstacleL = True
                    print("culprit 3")
                else:
                    mario.obstacleL = False
            #INTERACTABLE------------------------------------------------------------------------------------------
            elif str(type(blocks)) == "<class 'Brick.Interactable'>" \
                    and (mario.rect.left <= blocks.rect.right or mario.rect.right >= blocks.rect.left) \
                    and mario.rect.bottom > blocks.rect.top\
                    and mario.rect.top > blocks.rect.top-16\
                    and mario.rect.bottom <= blocks.rect.bottom:
                if mario.rect.right >= blocks.rect.left \
                        and not mario.obstacleL\
                        and mario.rect.left < blocks.rect.left:
                    mario.rect.right = blocks.rect.left -1
                    mario.obstacleR = True
                    print("culprit 2")
                else:
                    mario.obstacleR = False
                if mario.rect.left <= blocks.rect.right \
                    and not mario.obstacleR\
                    and mario.rect.right > blocks.rect.right:
                    mario.rect.left = blocks.rect.right + 1
                    mario.obstacleL = True
                    print("culprit 1")
                else:
                    mario.obstacleL = False
            #FLAG------------------------------------------------------------------------------------------
            elif str(type(blocks)) == "<class 'Brick.Flag'>" \
                    and (mario.rect.left <= blocks.rect.right or mario.rect.right >= blocks.rect.left) \
                    and mario.rect.bottom > blocks.rect.top\
                    and mario.rect.top > blocks.rect.top-16\
                    and mario.rect.bottom <= blocks.rect.bottom:
                print("got flag")
            #RESET-----------------------------------------------------------------------------------------------
            else:
                mario.obstacleR = False
                mario.obstacleL = False
            if mario.obstacleR or mario.obstacleL:
                print("im colliding")

            #top==================================================================================================
            #PIPE-----------------------------------------------------------------------------------------------
            if str(type(blocks)) == "<class 'Brick.Pipe'>" \
                    and (mario.rect.left < blocks.rect.right-5 and mario.rect.right > blocks.rect.left+5) \
                    and mario.rect.bottom > blocks.rect.top-32\
                    and not mario.obstacleL and not mario.obstacleR:
                mario.floor = True
                if not mario.break_brick:
                    mario.rect.y= blocks.rect.y - 32

                else:
                    mario.rect.y = blocks.rect.y - 64
            #BASIC-----------------------------------------------------------------------------------------------
            if str(type(blocks)) == "<class 'Brick.Basic'>" \
                    and (mario.rect.left < blocks.rect.right-5 and mario.rect.right > blocks.rect.left+5) \
                    and mario.rect.bottom > blocks.rect.top-32 \
                    and mario.rect.top < blocks.rect.top \
                    and not mario.obstacleL and not mario.obstacleR:
                mario.floor = True
                if not mario.break_brick:
                    mario.rect.y = blocks.rect.y - 32

                else:
                    mario.rect.y = blocks.rect.y - 64            #QUESTION-----------------------------------------------------------------------------------------------
            if str(type(blocks)) == "<class 'Brick.Question'>" \
                    and (mario.rect.left < blocks.rect.right-5 and mario.rect.right > blocks.rect.left+5) \
                    and mario.rect.bottom > blocks.rect.top-32\
                    and mario.rect.top < blocks.rect.top\
                    and not mario.obstacleL and not mario.obstacleR:
                mario.floor = True
                if not mario.break_brick:
                    mario.rect.y = blocks.rect.y - 32

                else:
                    mario.rect.y = blocks.rect.y - 64            #INTERACTABLE-----------------------------------------------------------------------------------------------
            if str(type(blocks)) == "<class 'Brick.Interactable'>" \
                    and (mario.rect.left < blocks.rect.right-5 and mario.rect.right > blocks.rect.left+5) \
                    and mario.rect.bottom > blocks.rect.top-32\
                    and mario.rect.top < blocks.rect.top\
                    and not mario.obstacleL and not mario.obstacleR:
                mario.floor = True
                if not mario.break_brick:
                    mario.rect.y = blocks.rect.y - 32

                else:
                    mario.rect.y = blocks.rect.y - 64                
                    print("its me")
                if mario.crouching:
                    print('crouching')
                    change_zone(mario=mario, level=level, LEVELS=LEVELS, index=1)
                    mario.rect.x = 100
                    mario.rect.y = 100
                    mario.center = mario.rect.centerx

            #hit===================================================================================
            #BASIC--------------------------------------------------------------------------------
            if str(type(blocks)) == "<class 'Brick.Basic'>"\
                    and mario.rect.top <= blocks.rect.bottom\
                    and (not mario.obstacleL or not mario.obstacleR)\
                    and mario.rect.bottom > blocks.rect.bottom:
                print("im basic")
                mario.jump_speed = .5
                mario.is_jumping = False
                mario.rect.top = blocks.rect.bottom +1
            #QUESTION--------------------------------------------------------------------------------
            elif str(type(blocks)) == "<class 'Brick.Question'>"\
                    and mario.rect.top <= blocks.rect.bottom\
                    and (not mario.obstacleL and not mario.obstacleR)\
                    and mario.rect.bottom > blocks.rect.bottom:
                print("im question")
                mario.jump_speed = .5
                mario.is_jumping = False
                mario.rect.top = blocks.rect.bottom +1
        #bounds====================================================================================
        if mario.rect.left < 0:
            mario.obstacleL = True
            mario.rect.left = 0

def check_mario_offstage(mario, level,LEVELS):
    if mario.rect.bottom >= 470:
        print("mario offstage")
        reset_level(mario=mario, level=level, LEVELS=LEVELS, index=0)

def change_zone(mario, level, LEVELS, index):
    level.move_zone(mario=mario,LEVELS=LEVELS, index=index)
    mario.rect.x = 300
    mario.rect.y = 300

def reset_level(mario, level, LEVELS, index):
    level.reset(LEVELS[index])
    mario.dead = False
    mario.rect.x= 50
    mario.rect.y = 200

def throw_fireball(screen, mario, fireballs):
    """ Throw fireball """

    # Create a new fireball and add it to the fireball group
    if len(fireballs) < Constants.fireballs_allowed:
        new_fireball = Fireball(screen=screen, mario=mario)
        fireballs.add(new_fireball)

def updateLevel(level, mario):
    level.camera(mario)
    level.update()

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

def update_fireballs(fireballs):
    """ Update position of fireball and remove those outside of frame """
    fireballs.update()

    # Get rid of bullets that have disappeared
    for fireball in fireballs.copy():
        if fireball.rect.left >= Constants.WINDOW_WIDTH or fireball.rect.right <= 0:
            fireballs.remove(fireball)

def update_screen(screen, mario, level, sb, enemies, items, fireballs):
    level.blitme()
    mario.blitme()
    for item in items:
        item.blitme()
    for enemy in enemies:
        enemy.blitme()
    for fireball in fireballs:
        fireball.draw_fireball()

    # draw score information
    sb.show_score()

    pygame.display.flip()