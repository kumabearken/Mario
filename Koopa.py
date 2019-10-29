import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from Timer import Timer


class Koopa(Sprite):
    def __init__(self, screen, walk_list_left, walk_list_right, shell_list):
        super(Koopa, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # list to hold animation images
        self.walk_list_left = walk_list_left
        self.walk_list_right = walk_list_right
        self.shell_list = shell_list

        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list_left)
        self.animation = Timer(frames=self.walk_list_right)
        self.animation = Timer(frames=self.shell_list)

        # get the rect of the image
        self.imageLeft = self.animation.imagerect()
        self.imageRight = self.animation.imagerect()
        self.imageShell = self.animation.imagerect()
        self.rect = self.imageLeft.get_rect()
        self.rect = self.imageRight.get_rect()
        self.rect = self.imageShell.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.middle_x = float(self.rect.centerx)

        # movement flags
        self.moving_left = True
        self.moving_right = False
        self.direction = -1

        # shell flag
        self.shell_mode = False
        self.shell_mode_moving = False

        #collision flags
        self.floor = False
        self.brick = False
        self.obstacleL = False
        self.obstacleR = False
        self.rect.x =300
        self.rect.y = 300

    def blitme(self):
        if self.moving_left:
            self.sur = self.imageLeft
            print("moving left")
            self.screen.blit(self.imageLeft, self.rect)
        if self.moving_right:
            self.sur = self.imageRight
            self.screen.blit(self.imageRight, self.rect)
        # TODO: handle blitme when the koopa is in shell mode
        if self.shell_mode:
            self.sur = self.imageShell
            self.screen.blit(self.imageShell, self.rect)
        if self.shell_mode_moving:
            self.sur = self.imageShell
            self.screen.blit(self.imageShell, self.rect)

    def update(self,level):
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
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
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
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
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
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
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
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
                    else:
                        self.obstacleL = False
                # INTERACTABLEH------------------------------------------------------------------------------------------
                elif str(type(blocks)) == "<class 'Brick.InteractableH'>" \
                        and (self.rect.left <= blocks.rect.right or self.rect.right >= blocks.rect.left) \
                        and self.rect.bottom > blocks.rect.top \
                        and self.rect.top > blocks.rect.top - 16 \
                        and self.rect.bottom <= blocks.rect.bottom:
                    if self.rect.right >= blocks.rect.left \
                            and not self.obstacleL \
                            and self.rect.left < blocks.rect.left:
                        self.rect.right = blocks.rect.left - 1
                        self.obstacleR = True
                    else:
                        self.obstacleR = False
                    if self.rect.left <= blocks.rect.right \
                            and not self.obstacleR \
                            and self.rect.right > blocks.rect.right:
                        self.rect.left = blocks.rect.right + 1
                        self.obstacleL = True
                    else:
                        self.obstacleL = False
                # FLAG------------------------------------------------------------------------------------------
                elif str(type(blocks)) == "<class 'Brick.Flag'>" \
                        and (self.rect.left <= blocks.rect.right or self.rect.right >= blocks.rect.left) \
                        and self.rect.bottom > blocks.rect.top \
                        and self.rect.top > blocks.rect.top - 16 \
                        and self.rect.bottom <= blocks.rect.bottom:
                    print("got flag")
                # RESET-----------------------------------------------------------------------------------------------
                else:
                    self.obstacleR = False
                    self.obstacleL = False
                if self.obstacleR or self.obstacleL:
                    print("im colliding")

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

        if self.obstacleR:
            self.sur = self.imageLeft
            self.direction *= -1
            self.moving_left = True
            self.moving_right = False
        elif self.obstacleL:
            self.sur = self.imageRight
            self.direction *= -1
            self.moving_right = True
            self.moving_left = False
        if self.obstacleR and self.shell_mode_moving:
            self.sur = self.imageShell
            self.direction *= - 1
        if self.obstacleL and self.shell_mode_moving:
            self.sur = self.imageShell
            self.direction *= 1
        if self.moving_left:
            self.imageLeft = self.walk_list_left[self.animation.frame_index()]
        if self.moving_right:
            self.imageRight = self.walk_list_right[self.animation.frame_index()]
        # TODO: handle movement when turtle is in shell mode
        if self.shell_mode:
            self.moving_right = False
            self.moving_left = False
            self.direction = 0
            self.imageShell = self.shell_list[self.animation.frame_index()]
            print("static")
        if self.shell_mode_moving:
            self.moving_right = False
            self.moving_left = False
            if self.direction == 1:
                self.direction *= -1
            if self.direction == -1:
                self.direction *= 1
            self.imageShell = self.shell_list[self.animation.frame_index()]
            print("moving")


class RegularKoopa(Koopa):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("Images/enemies.png")
        self.koopas_left = []
        self.koopas_right = []
        self.koopas_shell = []
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
        super().__init__(screen=screen, walk_list_left=self.koopas_left, walk_list_right=self.koopas_right, shell_list=self.koopas_shell)
