import pygame
import sys
import Mario
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def check_events(screen, mario):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event = event, mario = mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event = event, mario = mario)
            
            
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

def check_collisiontype(level, mario):
    for blocks in level.environment:
        if (pygame.sprite.collide_rect(mario, blocks)):
            #floor
            if str(type(blocks)) == "<class 'Brick.Floor'>" and mario.rect.bottom >= blocks.rect.top:
                mario.floor=True
                mario.rect.y= blocks.rect.y - 32
            #sides
            if str(type(blocks)) == "<class 'Brick.Pipe'>" and (mario.rect.left <= blocks.rect.right or mario.rect.right >= blocks.rect.left) and mario.rect.bottom >= blocks.rect.top and mario.rect.top >= blocks.rect.top:
                if mario.rect.left <= blocks.rect.right:
                    print("mario left "+str(mario.rect.left) + " box right " + str(blocks.rect.right))
                    mario.rect.left = blocks.rect.right + 1
                    mario.obstacleL = True
                else:
                    mario.obstacleL = False
                if mario.rect.right >= blocks.rect.left:
                    print("mario right " + str(mario.rect.right) + " box left " + str(blocks.rect.left))
                    mario.rect.right = blocks.rect.left -1
                    mario.obstacleR = True
                else:
                    mario.obstacleR = False
            #bounds
            if mario.rect.left < 0:
                mario.obstacleL = True
                mario.rect.left = 0

def updateLevel(level, mario):
    level.camera(mario)
    level.update()


def updateMario(mario):
    mario.update()


def updateScreen(screen, mario, level):
    screen.fill(BLACK)
    level.blitme()
    mario.blitme()
    pygame.display.flip()
