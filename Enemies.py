import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from Timer import Timer


class Enemy(Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 380
        # store objects exact position
        self.x = float(self.rect.centerx)

        # movement flags
        self.moving_left = False
        self.moving_right = False

        self.speedx = 2
        self.speedy = 4

        self.floor=False
        self.obstacleR=False
        self.obstacleL=False

    def check_collisions(self, level):
        for blocks in level.environment:
            if (pygame.sprite.collide_rect(self, blocks)):
                # floor==========================================================================================
                if str(type(blocks)) == "<class 'Brick.Floor'>" and self.rect.bottom >= blocks.rect.top:
                    self.floor = True
                    self.rect.y = blocks.rect.y - 32

                # sides===========================================================================================
                # PIPE-------------------------------------------------------------------------------------------
                if str(type(blocks)) == "<class 'Brick.Pipe'>" \
                        and (self.rect.left <= blocks.rect.right or self.rect.right >= blocks.rect.left) \
                        and self.rect.bottom > blocks.rect.top \
                        and self.rect.top > blocks.rect.top - 16:
                    if self.rect.right >= blocks.rect.left \
                            and not self.obstacleL \
                            and self.rect.left < blocks.rect.left:
                        self.rect.right = blocks.rect.left - 1
                        self.obstacleR = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleL = False
                # BASIC--------------------------------------------------------------------------------------------
                elif str(type(blocks)) == "<class 'Brick.Basic'>" \
                        and (self.rect.left <= blocks.rect.right or self.rect.right >= blocks.rect.left) \
                        and self.rect.bottom > blocks.rect.top \
                        and self.rect.top > blocks.rect.top - 16 \
                        and self.rect.bottom <= blocks.rect.bottom:
                    if self.rect.right >= blocks.rect.left \
                            and not self.obstacleL \
                            and self.rect.left < blocks.rect.left:
                        self.rect.right = blocks.rect.left - 1
                        self.obstacleR = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleL = False

                # QUESTION------------------------------------------------------------------------------------------
                elif str(type(blocks)) == "<class 'Brick.Question'>" \
                        and (self.rect.left <= blocks.rect.right or self.rect.right >= blocks.rect.left) \
                        and self.rect.bottom > blocks.rect.top \
                        and self.rect.top > blocks.rect.top - 16 \
                        and self.rect.bottom <= blocks.rect.bottom:
                    if self.rect.right >= blocks.rect.left \
                            and not self.obstacleL \
                            and self.rect.left < blocks.rect.left:
                        self.rect.right = blocks.rect.left - 1
                        self.obstacleR = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleL = False
                # INTERACTABLEV------------------------------------------------------------------------------------------
                elif str(type(blocks)) == "<class 'Brick.InteractableV'>" \
                        and (self.rect.left <= blocks.rect.right or self.rect.right >= blocks.rect.left) \
                        and self.rect.bottom > blocks.rect.top \
                        and self.rect.top > blocks.rect.top - 16 \
                        and self.rect.bottom <= blocks.rect.bottom:
                    if self.rect.right >= blocks.rect.left \
                            and not self.obstacleL \
                            and self.rect.left < blocks.rect.left:
                        self.rect.right = blocks.rect.left - 1
                        self.obstacleR = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
                        self.speedx = self.speedx * (-1)
                    else:
                        self.obstacleL = False
                # RESET-----------------------------------------------------------------------------------------------
                else:
                    self.obstacleR = False
                    self.obstacleL = False

                # top==================================================================================================
                # PIPE-----------------------------------------------------------------------------------------------
                if str(type(blocks)) == "<class 'Brick.Pipe'>" \
                        and (self.rect.left < blocks.rect.right - 5 and self.rect.right > blocks.rect.left + 5) \
                        and self.rect.bottom > blocks.rect.top - 32 \
                        and not self.obstacleL and not self.obstacleR:
                    self.floor = True
                    self.rect.y = blocks.rect.y - 32
                # BASIC-----------------------------------------------------------------------------------------------
                if str(type(blocks)) == "<class 'Brick.Basic'>" \
                        and (self.rect.left < blocks.rect.right - 5 and self.rect.right > blocks.rect.left + 5) \
                        and self.rect.bottom > blocks.rect.top - 32 \
                        and self.rect.top < blocks.rect.top \
                        and not self.obstacleL and not self.obstacleR:
                    self.floor = True
                    self.rect.y = blocks.rect.y - 32
                # QUESTION-----------------------------------------------------------------------------------------------
                if str(type(blocks)) == "<class 'Brick.Question'>" \
                        and (self.rect.left < blocks.rect.right - 5 and self.rect.right > blocks.rect.left + 5) \
                        and self.rect.bottom > blocks.rect.top - 32 \
                        and self.rect.top < blocks.rect.top \
                        and not self.obstacleL and not self.obstacleR:
                    self.floor = True
                    self.rect.y = blocks.rect.y - 32
                # INTERACTABLEV-----------------------------------------------------------------------------------------------
                if str(type(blocks)) == "<class 'Brick.InteractableV'>" \
                        and (self.rect.left < blocks.rect.right - 5 and self.rect.right > blocks.rect.left + 5) \
                        and self.rect.bottom > blocks.rect.top - 32 \
                        and self.rect.top < blocks.rect.top \
                        and not self.obstacleL and not self.obstacleR:
                    self.floor = True
                    self.rect.y = blocks.rect.y - 32
                # INTERACTABLEH-----------------------------------------------------------------------------------------------
                if str(type(blocks)) == "<class 'Brick.InteractableH'>" \
                        and (self.rect.left < blocks.rect.right - 5 and self.rect.right > blocks.rect.left + 5) \
                        and self.rect.bottom > blocks.rect.top - 32 \
                        and self.rect.top < blocks.rect.top \
                        and not self.obstacleL and not self.obstacleR:
                    self.floor = True
                    self.rect.y = blocks.rect.y - 32

            # bounds====================================================================================
            if self.rect.left < -32:
                self.obstacleL = True
                self.rect.left = -32



class Goomba(Enemy):
    """ Class to define Goomba """
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("images/enemies.png")
        self.goombas = []
        image = pygame.transform.scale(sprite_sheet.get_image(0, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(30, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        self.walk_list = self.goombas

        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list)

        # get the rect of the image
        self.image = self.animation.imagerect()
        self.rect = self.image.get_rect()

        # next image for squished goomba
        # list to hold animation images
        """image = pygame.transform.scale(sprite_sheet.get_image(60, 5, 16, 16), (30, 30))
        self.goombas.append(image)"""
        super().__init__(screen=screen)

    def update(self,level):
        self.rect.right+= self.speedx
        self.rect.bottom += self.speedy
        if (level.move):
            self.rect.right -= 4
        self.check_collisions(level=level)
        self.image = self.walk_list[self.animation.frame_index()]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class RegularKoopa(Enemy):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("Images/enemies.png")
        self.koopas_left = []
        self.koopas_right = []
        self.koopas_shell = []

        # shell flag
        self.shell_mode = False
        self.shell_mode_moving = False

        self.brick = False

        imageRight = pygame.transform.scale(sprite_sheet.get_image(210, 0, 19, 25), (32, 32))
        self.koopas_right.append(imageRight)
        imageRight = pygame.transform.scale(sprite_sheet.get_image(240, 0, 19, 25), (32, 32))
        self.koopas_right.append(imageRight)
        imageLeft = pygame.transform.scale(sprite_sheet.get_image(179, 0, 19, 25), (32, 32))
        self.koopas_left.append(imageLeft)
        imageLeft = pygame.transform.scale(sprite_sheet.get_image(149, 0, 19, 25), (32, 32))
        self.koopas_left.append(imageLeft)
        imageShell = pygame.transform.scale(sprite_sheet.get_image(360, 0, 19, 25), (32, 32))
        self.koopas_shell.append(imageShell)
        imageShell = pygame.transform.scale(sprite_sheet.get_image(360, 0, 19, 25), (32, 32))
        self.koopas_shell.append(imageShell)

        # Timer class to animate sprites
        self.animation = Timer(frames=self.koopas_left)

        # get the rect of the image
        self.imageLeft = self.animation.imagerect()
        self.imageRight = self.animation.imagerect()
        self.imageShell = self.animation.imagerect()
        self.rect = self.imageLeft.get_rect()
        self.rect = self.imageRight.get_rect()
        self.rect = self.imageShell.get_rect()

        super().__init__(screen=screen)
        self.rect.x = 400
        self.rect.y = 300

    def blitme(self):
        if self.moving_left:
            self.screen.blit(self.imageLeft, self.rect)
        if self.moving_right:
            self.screen.blit(self.imageRight, self.rect)
        # TODO: handle blitme when the koopa is in shell mode
        if self.shell_mode:
            self.screen.blit(self.imageShell, self.rect)
        if self.shell_mode_moving:
            self.screen.blit(self.imageShell, self.rect)
        print("im koopa")

    def update(self,level):
        self.rect.right+= self.speedx
        self.rect.bottom += self.speedy
        if (level.move):
            self.rect.right -= 4
        self.check_collisions(level=level)
        if self.moving_left:
            self.imageLeft = self.koopas_left[self.animation.frame_index()]
        if self.moving_right:
            self.imageRight = self.koopas_right[self.animation.frame_index()]
        if self.shell_mode or self.shell_mode_moving:
            self.imageShell = self.koopas_shell[self.animation.frame_index()]
