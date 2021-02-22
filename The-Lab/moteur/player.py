import pygame
from moteur.Image import Image
from moteur.time import Chrono
from moteur.event import keypressed
from moteur.map import Wall



class Player:

    def __init__(self,map,imgbase:str,imgrunDown:str):
        super().__init__()
        self.map = map
        self.pos = [50,50,50,50]
        #move
        self.move = False
        self.nRun = 0
        self.left = False
        self.up = False
        self.velocity = 5
        self.imgRun = Image(imgrunDown)
        self.imgRun.split(36,36,0)
        self.imgRun.resize_all_tile(50,50)
        #chrono
        self.chrono = Chrono()
        #imgbase
        self.imgbase = Image(imgbase)
        self.imgbase.split(36,36,0)
        self.imgbase.resize_all_tile(50,50)
        self.nIDLE = 0
        self.rect= self.imgbase.get_rect()
        self.rect.x , self.rect.y = 0,50
        #control
        self.av = pygame.K_z
        self.re = pygame.K_s
        self.le = pygame.K_q
        self.ri = pygame.K_d
        self.keys = {self.av : False,self.re : False,self.le:False,self.ri:False}
  
    def move_on_axe_x(self,add:bool = True):
        if add:
            self.rect.x += self.velocity
            self.left = False ; self.up = False;self.move = True
        else:
            self.rect.x -= self.velocity
            self.left = True; self.up = False;self.move = True

    def move_on_axe_y(self,add:bool = True):
        if add:
            self.rect.y += self.velocity
            self.left = False ; self.up = False;self.move = True
        else:
            self.rect.y -= self.velocity
            self.up =True ; self.left = False;self.move = True



    def affUpdate(self,window):
        if not self.move:
            if self.chrono.get_val()%10 == 0:
                self.nRun = 0
                self.nIDLE +=1
                if self.nIDLE > 7:
                    self.nIDLE = 0
                self.imgbase.changeImagewithtiletable(self.nIDLE)
            self.imgbase.aff(window,self.rect.x,self.rect.y)

        if self.move:
            if self.chrono.get_val()%5 == 0:
                self.nIDLE = 0
                self.nRun += 1
                if self.nRun > 7:
                    self.nRun = 0
                self.imgRun.changeImagewithtiletable(self.nRun)
            self.imgRun.aff(window,self.rect.x,self.rect.y)


    def prev_check_collision(self,xb,yb):
        if xb == 1 and self.rect.x%50 == 0:
            x = (self.rect.x+(self.velocity*xb)) // 50+1
            y = (self.rect.y+(self.velocity*yb)) // 50
        elif yb == 1 and self.rect.y%50 == 0:
            x = (self.rect.x+(self.velocity*xb)) // 50
            y = (self.rect.y+(self.velocity*yb)) // 50 +1
        else:
            x = (self.rect.x+(self.velocity*xb)) // 50
            y = (self.rect.y+(self.velocity*yb)) // 50
        print(x,y)
        #x = (self.rect.x // 50) +xb
        #y = (self.rect.y // 50) +yb
        return not self.map.listoftiles[y][x].get_law()
    
    def inter(self):
        x = (self.rect.x // 50)
        y = (self.rect.y // 50)
        return self.map.listoftiles[y][x].get_event()

    def get_rect(self):
        return self.rect




    def aff(self,window):
        self.map.listoftiles[2][1].aff(window)
        self.imgbase.aff(window,self.rect.x,self.rect.y)

        

