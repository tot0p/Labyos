import pygame
from moteur.Image import Image
from moteur.time import Chrono
from moteur.event import keypressed



class Player:

    def __init__(self,imgbase:str,spawnCoord:tuple=(0,0),imgIdle:list=None,imgWalk:list=None):
        super().__init__()
        #chrono
        self.chrono = Chrono()
        #imgbase
        self.imgbase = Image(imgbase)
        self.imgbase.split(300,300,0)
        self.imgbase.resize_all_tile(50,50)
        self.rect = self.imgbase.get_rect()
        self.n = 0
        #imgIdle
        self.imgIdle = imgIdle
        #imgWalk
        self.imgWalk = imgWalk
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
        if self.keys[self.av]:print('av')
        if self.keys[self.re]:print('re')
        if self.keys[self.le]:print('le')
        if self.keys[self.ri]:print('ri')

    def affUpdate(self,window):
        if self.chrono.get_val()%10 == 0:
            self.n +=1
            if self.n > 7:
                self.n = 0
            self.imgbase.changeImagewithtiletable(self.n)
            pygame.draw.rect(window.window,pygame.Color(0,0,0),(50,50,50,50),0)
            self.imgbase.aff(window,50,50)

    def aff(self,window):
        self.imgbase.aff(window,50,50)

        

