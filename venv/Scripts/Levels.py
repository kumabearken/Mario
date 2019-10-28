import pygame
import Mario
import Enemies
import Brick
import Scoreboard
BLACK = (0,0,0)
CREATE = False
SPEED = 4
if CREATE:
    SPEED=960
END = True

class Level():
    def __init__(self, screen):
        self.image = pygame.image.load('Images/bg-1-1.png')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.environment = []
        self.start_x = 0
        self.start_y = 0
        self.end_x = 960
        self.end_y = 470
        self.move = False

    def step(self):
        if(CREATE):
            while(True):
                test = input()
                if test:
                    break

    def blitme(self):
        self.screen.blit(pygame.transform.scale(self.image,(6784,960)), (0,0,960,470), (self.start_x,self.start_y,self.end_x,self.end_y))
        for object in self.environment:
            self.screen.blit(object.sur,object.rect)

    def update(self):
        self.step()
        if self.move or CREATE:
            self.end_x += SPEED
            self.start_x += SPEED
            for object in self.environment:
                object.rect.left -= SPEED

    def create_rects(self,file):
        with open(file) as f:
            for line in f:
                type, width, height, x,y = line.split()
                if type == 'Obstacle':
                    self.create_obstacle(width=int(width),height=int(height),x=int(x),y=int(y))
                if type == 'Destructable':
                    self.create_destructable(width=int(width),height=int(height),x=int(x),y=int(y))
                if type == 'Question':
                    self.create_question(width=int(width),height=int(height),x=int(x),y=int(y))
                if type == 'Pipe':
                    self.create_pipe(width=int(width),height=int(height),x=int(x),y=int(y))
                if type == 'Floor':
                    self.create_floor(width=int(width),height=int(height),x=int(x),y=int(y))
                if type == 'Flag':
                    self.create_flag(width=int(width),height=int(height),x=int(x),y=int(y))

    def create_obstacle(self, width, height, x, y):
        box = Brick.Pipe(width, height, x, y)
        self.environment.append(box)
        
    def create_destructable(self, width, height, x, y):
        box = Brick.Basic(width, height, x, y)
        self.environment.append(box)

    def create_pipe(self, width, height, x, y):
        box = Brick.Interactable(width, height, x, y)
        self.environment.append(box)

    def create_question(self, width, height, x, y):
        box = Brick.Question(width, height, x, y)
        self.environment.append(box)

    def create_floor(self, width, height, x, y):
        box = Brick.Floor(width, height, x, y)
        self.environment.append(box)

    def create_flag(self, width, height, x, y):
        box = Brick.Flag(width, height, x, y)
        self.environment.append(box)

    def camera(self,mario):
        if (mario.rect.x >= 480 and mario.moving_right and not mario.obstacleR):
            self.move = True
            #print("camera moving")
        else:
            self.move = False
            #print("camera NOT moving")

    def move_zone(self,mario,LEVELS,index):
        self.start_x = 0
        self.end_x = 960
        self.start_y = 480
        self.end_y = 950
        self.reset(LEVELS[index])

    def reset(self,file):
        self.environment = []
        self.create_rects(file=file)
        self.start_x = 0
        self.end_x=960
