import pygame
from moteur.Image import Image
from moteur.event import keypressed



class Player(pygame.sprite.Sprite):

    def __init__(self,imgbase:Image,spawnCoord:tuple=(0,0),imgIdle:list=None,imgWalk:list=None):
        super().__init__()
        #imgbase
        self.image = imgbase.get_image()
        self.rect = imgbase.get_rect()
        self.imgbase = imgbase
        #coord
        self.rect.x = spawnCoord[0]
        self.rect.y = spawnCoord[1]
        #imgIdle
        self.imgIdle = imgIdle
        #imgWalk
        self.imgWalk = imgWalk
        #control
        self.keys = {}
        self.av = pygame.K_z
        self.re = pygame.K_s
        self.le = pygame.K_q
        self.ri = pygame.K_d

    def spawn(self,window):
        window.addSprite(self)
        

    def event(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keys[event.key] = True
            else:
                self.keys[event.key] = False
        if self.keys[self.av]:print('av')
        if self.keys[self.re]:print('re')
        if self.keys[self.le]:print('le')
        if self.keys[self.ri]:print('ri')

    def aff(self,window):
        window.aff(self.image,self.rect.x,self.rect.y)

        

