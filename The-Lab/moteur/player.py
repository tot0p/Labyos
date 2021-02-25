import pygame
from moteur.Image import Image
from moteur.time import Chrono
from moteur.event import keypressed
from moteur.map import Wall



class Player:

    def __init__(self,imgbase:str,imgrunDown:str):
        super().__init__()
        self.pos = [50,50,50,50]
        #move
        self.move = False
        self.nRun = 0
        self.left = False
        self.up = False
        self.velocity = 1
        self.imgRun = Image(imgrunDown)
        self.imgRun.split(36,36,0)
        self.imgRun.resize_all_tile(45,45)
        #chrono
        self.chrono = Chrono()
        #imgbase
        self.imgbase = Image(imgbase)
        self.imgbase.split(36,36,0)
        self.imgbase.resize_all_tile(45,45)
        self.nIDLE = 0
        self.rect= self.imgbase.get_rect()
        self.rect.x , self.rect.y = 0,50
        #control
        self.av = pygame.K_z
        self.re = pygame.K_s
        self.le = pygame.K_q
        self.ri = pygame.K_d
        self.keys = {self.av : False,self.re : False,self.le:False,self.ri:False}

    def def_map(self,map):
        self.map = map
  
    def set_spawn(self,x,y):
        self.rect.x = x
        self.rect.y = y


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
        # x-x
        # | |
        # x-x
        # x
        #
        # x
        
        x = (self.rect.x+(self.velocity*xb))
        y = (self.rect.y+(self.velocity*yb))
        rect = self.map.listoftiles[y//50][x//50].get_rect()
        if xb == 1:
            xb =(self.rect.x+self.rect.width+(self.velocity*xb))
            yb = (self.rect.y+self.rect.height+(self.velocity*yb))
            law = self.map.listoftiles[y//50][x//50+1].get_law()
            print("law :",law)
            print("name1 :",type(self.map.listoftiles[y//50][x//50+1]))
            if not (xb >= rect.x and xb <= (rect.x + rect.width)) :
                if not (yb >= rect.y and yb <= rect.y + rect.height):
                    law = law and self.map.listoftiles[y//50+1][x//50+1].get_law()
                    print("name2 :",type(self.map.listoftiles[y//50+1][x//50+1]))
            print("law :",law)
            return not law
        elif xb == -1:
            yb =y+self.rect.height
            law = self.map.listoftiles[y//50][x//50].get_law()
            print("law :",law)
            print("name1 :",type(self.map.listoftiles[y//50][x//50]))
            if not (yb >= rect.y and yb <= rect.y + rect.height):
                print('yes')
                law = law and self.map.listoftiles[y//50+1][x//50].get_law()
                print("name2 :",type(self.map.listoftiles[y//50+1][x//50]))
            print("law :",law)
            return not law
        elif yb == 1:
            xb =(self.rect.x+self.rect.width+(self.velocity*xb))
            yb =(self.rect.y+self.rect.height+(self.velocity*yb))
            law = self.map.listoftiles[y//50+1][x//50].get_law()
            print("law :",law)
            print("name1 :",type(self.map.listoftiles[y//50+1][x//50]))
            if not (xb >= rect.x and xb <= rect.x + rect.width):
               law = law and self.map.listoftiles[y//50+1][x//50+1].get_law()
               print("name2 :",type(self.map.listoftiles[y//50+1][x//50+1]))
            print("law :",law)
            return not law
        elif yb == -1:
            xb =x+self.rect.width
            law = self.map.listoftiles[y//50][x//50].get_law()
            print("law :",law)
            print("name1 :",type(self.map.listoftiles[y//50][x//50]))
            if not (xb >= rect.x and xb <= rect.x + rect.width):
                print('yes')
                law = law and self.map.listoftiles[y//50][x//50+1].get_law()
                print("name2 :",type(self.map.listoftiles[y//50][x//50+1]))
            print("law :",law)
            return not law
        return False
        #if rect.x <= x and x <= (rect.x + rect.width):
            #if rect.y <= y and y <= (rect.y + rect.height):
                #return not self.map.listoftiles[y//50][x//50].get_law()
        #xb = (self.rect.x+self.rect.width+(self.velocity*xb))
        #if rect.x <= xb and xb <= (rect.x + rect.width):
            #if rect.y <= y and y <= (rect.y + rect.height):
                #print('ys')
                #return not self.map.listoftiles[y//50][x//50].get_law()

        
        return False
    
    def inter(self):
        x = (self.rect.x // 50)
        y = (self.rect.y // 50)
        return self.map.listoftiles[y][x].get_event()

    def get_rect(self):
        return self.rect




    def aff(self,window):
        self.imgbase.aff(window,self.rect.x,self.rect.y)

        

