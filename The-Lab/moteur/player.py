import pygame
from moteur.Image import Image
from moteur.map import Map

class Player(pygame.sprite.Sprite):

    def __init__(self,imgbase:Image,map:Map,spawnCoord:tuple=(0,0),imgIdle:list=None,imgWalk:list=None):
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

    def spawn(self,window):
        window.addSprite(self)
        

    def event(self):
        pass

