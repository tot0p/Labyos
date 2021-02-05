import pygame
from moteur.fichier import *

class Map(pygame.sprite.Group):

    def __init__(self,window,filename,taillecase=(50,50)):
        super().__init__()
        self.window = window
        self.dictTiles = {}
        self.encodageMap = []
        self.__load()
        self.coordMap = []

    def __createCoordMap(self,taillecase):
        for x in range(self.window.W//taillecase[0]):
            for y in range(self.window.H//taillecase[1]):
                self.coordMap.append((0+taillecase[0]*x,0+taillecase[1]*y))

    def __load(self,filname):
        pass