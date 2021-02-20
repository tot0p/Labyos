import pygame
from moteur.Image import Image
from moteur.time import Chrono
from moteur.event import keypressed



class Player:

    def __init__(self,map,imgbase:str,imgrun:str):
        super().__init__()
        self.map = map
        self.pos = [50,50,50,50]
        #move
        self.move = False
        self.nRun = 0
        self.left = False
        self.velocity = 5
        self.imgRun = Image(imgrun)
        self.imgRunLeft = Image(imgrun)
        self.imgRun.split(36,36,0);self.imgRunLeft.split(36,36,0)
        self.imgRun.resize_all_tile(50,50);self.imgRunLeft.resize_all_tile(50,50)
        self.imgRunLeft.flip_all_tile(True,False)
        #chrono
        self.chrono = Chrono()
        #imgbase
        self.imgbase = Image(imgbase)
        self.imgbase.split(36,36,0)
        self.imgbase.resize_all_tile(50,50)
        self.nIDLE = 0
        #control
        self.av = pygame.K_z
        self.re = pygame.K_s
        self.le = pygame.K_q
        self.ri = pygame.K_d
        self.keys = {self.av : False,self.re : False,self.le:False,self.ri:False}
  


    def event(self,event):
        #for event in events:
        if event.type == pygame.KEYDOWN:
            self.keys[event.key] = True
        elif event.type == pygame.KEYUP:
            self.keys[event.key] = False
        if self.keys[self.av] and self.pos[1] > 0: self.pos[3] = self.pos[1];self.pos[1] -= self.velocity
        if self.keys[self.re] and self.pos[1]+50 <500:self.pos[3] = self.pos[1];self.pos[1] += self.velocity
        if self.keys[self.le] and self.pos[0] > 0:self.pos[2] = self.pos[0];self.pos[0] -= self.velocity;self.left =True
        if self.keys[self.ri] and self.pos[0] + 50 < 500:self.pos[2] = self.pos[0];self.pos[0] += self.velocity;self.left =False
        if self.keys[self.av] or self.keys[self.re] or self.keys[self.le] or self.keys[self.ri]:self.move = True
        else:self.move=False
        if self.move:
            self.change = [(self.pos[0],self.pos[1]),(self.pos[2],self.pos[3])]

    def affUpdate(self,window):
        if not self.move:
            if self.chrono.get_val()%10 == 0:
                self.nRun = 0
                self.nIDLE +=1
                if self.nIDLE > 7:
                    self.nIDLE = 0
                self.imgbase.changeImagewithtiletable(self.nIDLE)
            self.imgbase.aff(window,self.pos[0],self.pos[1])

        if self.move:
            if self.chrono.get_val()%10 == 0:
                self.nIDLE = 0
                self.nRun += 1
                if self.nRun > 3:
                    self.nRun = 0
                self.imgRun.changeImagewithtiletable(self.nRun)
                self.imgRunLeft.changeImagewithtiletable(self.nRun)
            if self.left:
                self.imgRunLeft.aff(window,self.pos[0],self.pos[1])
            else:
                self.imgRun.aff(window,self.pos[0],self.pos[1])




    def aff(self,window):
        self.imgbase.aff(window,self.pos[0],self.pos[1])

        

