import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from Timer import Timer

class Items(Sprite):
    def __init__(self,screen, animation):
        super().__init__()
        self.screen=screen
        self.animation = animation
        self.animation_timer = Timer(frames=self.animation)
        self.image = self.animation_timer.imagerect()
        self.rect = self.image.get_rect()
        self.floor=False
        self.obstacleR=False
        self.obstacleL=False
        self.speedx = 2
        self.speedy = 4
        self.bound = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
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
                self.bounds=True

class Mushroom(Items):
    def __init__(self,screen):
        self.animation = []
        sprite_sheet = SpriteSheet("Images/items.png")
        self.image = pygame.transform.scale(sprite_sheet.get_image(184, 34, 16, 16), (32, 32))
        self.animation.append(self.image)
        super().__init__(screen=screen, animation=self.animation)

    def update(self,level):
        self.rect.right +=self.speedx
        self.rect.bottom +=self.speedy
        if (level.move):
            self.rect.right -= 3
        self.image = self.animation[self.animation_timer.frame_index()]
        self.check_collisions(level=level)

class Flower(Items):
    def __init__(self,screen):
        self.animation = []
        sprite_sheet = SpriteSheet("Images/items.png")
        self.image = pygame.transform.scale(sprite_sheet.get_image(4, 64, 20, 16), (32, 32))
        self.animation.append(self.image)
        self.image = pygame.transform.scale(sprite_sheet.get_image(34, 64, 20, 16), (32, 32))
        self.animation.append(self.image)
        self.image = pygame.transform.scale(sprite_sheet.get_image(64, 64, 20, 16), (32, 32))
        self.animation.append(self.image)
        self.image = pygame.transform.scale(sprite_sheet.get_image(94, 64, 20, 16), (32, 32))
        self.animation.append(self.image)
        super().__init__(screen=screen, animation=self.animation)

    def update(self,level):
        self.image = self.animation[self.animation_timer.frame_index()]
        if (level.move):
            self.rect.right -= 4

class Coin(Items):
    def __init__(self,screen):
        self.animation = []
        sprite_sheet = SpriteSheet("Images/items.png")
        self.image = pygame.transform.scale(sprite_sheet.get_image(128, 95, 8, 14), (16, 28))
        self.animation.append(self.image)
        self.image = pygame.transform.scale(sprite_sheet.get_image(160, 95, 4, 14), (8, 28))
        self.animation.append(self.image)
        self.image = pygame.transform.scale(sprite_sheet.get_image(191, 95, 1, 14), (2, 28))
        self.animation.append(self.image)
        self.image = pygame.transform.scale(sprite_sheet.get_image(220, 95, 4, 14), (8, 28))
        self.animation.append(self.image)
        super().__init__(screen=screen, animation=self.animation)

    def update(self,level):
        self.image = self.animation[self.animation_timer.frame_index()]
        if (level.move):
            self.rect.right -= 4

class Star(Items):
    def __init__(self,screen):
        super().__init__(screen=screen)
        sprite_sheet = SpriteSheet("Images/items-objects.png")
        self.image = pygame.transform.scale(sprite_sheet.get_image(0,48,16,16), (32,32))
        self.rect =self.image.get_rect()

    def update(self,level):
        if (level.move):
            self.rect.right -= 4