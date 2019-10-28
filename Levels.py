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
SCREENX=960
SCREENY=470
class Level():
    def __init__(self, screen):
        self.image = pygame.image.load('Images/bg-1-1.png')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.environment = []
        self.start_x = 0
        self.start_y = 0
        self.end_x = SCREENX
        self.end_y = SCREENY
        self.move = False

    def step(self):
        if(CREATE):
            while(True):
                test = input()
                if test:
                    break

    def blitme(self):
        self.screen.blit(pygame.transform.scale(self.image,(6784,SCREENX)), (0,0,SCREENX,SCREENY), (self.start_x,self.start_y,self.end_x,self.end_y))
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
                type, width, height, x,y, items = line.split()
                if type == 'Obstacle':
                    self.create_obstacle(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))
                if type == 'Destructable':
                    self.create_destructable(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))
                if type == 'Question':
                    self.create_question(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))
                if type == 'PipeV':
                    self.create_pipeV(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))
                if type == 'Floor':
                    self.create_floor(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))
                if type == 'Flag':
                    self.create_flag(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))
                if type == 'PipeH':
                    self.create_pipeH(width=int(width),height=int(height),x=int(x),y=int(y), items=int(items))

    def create_obstacle(self, width, height, x, y, items):
        box = Brick.Pipe(width, height, x, y, items)
        self.environment.append(box)
        
    def create_destructable(self, width, height, x, y, items):
        box = Brick.Basic(width, height, x, y, items)
        self.environment.append(box)

    def create_pipeV(self, width, height, x, y, items):
        box = Brick.InteractableV(width, height, x, y, items)
        self.environment.append(box)

    def create_pipeH(self, width, height, x, y, items):
        box = Brick.InteractableH(width, height, x, y, items)
        self.environment.append(box)

    def create_question(self, width, height, x, y, items):
        box = Brick.Question(width, height, x, y, items)
        self.environment.append(box)

    def create_floor(self, width, height, x, y, items):
        box = Brick.Floor(width, height, x, y, items)
        self.environment.append(box)

    def create_flag(self, width, height, x, y, items):
        box = Brick.Flag(width, height, x, y, items)
        self.environment.append(box)

    def camera(self,mario):
        if (mario.rect.x >= 480 and mario.moving_right and not mario.obstacleR):
            self.move = True
            #print("camera moving")
        else:
            self.move = False
            #print("camera NOT moving")

    def move_zone(self,mario,LEVELS,index, settings):
        self.reset(LEVELS[index])
        if (settings == 1):
            self.start_x = 0
            self.end_x = SCREENX
            self.start_y = 480
            self.end_y = 950
        elif (settings == 2):
            self.start_x = SCREENX * 5
            self.end_x = SCREENX * 6
            self.start_y = 0
            self.end_y = SCREENY
            for objects in self.environment:
                objects.rect.x -= SCREENX * 5
    def reset(self,file):
        self.environment = []
        self.create_rects(file=file)
        self.start_x = 0
        self.end_x= SCREENX
        self.start_y=0
        self.end_y = SCREENY
