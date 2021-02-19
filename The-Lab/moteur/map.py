import pygame
from moteur.fichier import *
from moteur.loadtiletable import load_tile_table

class Map(pygame.sprite.Group):

    def __init__(self,window,filename):
        super().__init__()
        self.window = window
        self.encodageMap = []
        self.__load(filename)
        self.coordMap = []
        self.__createCoordMap((50,50))

    def __createCoordMap(self,taillecase):
        for x in range(self.window.W//taillecase[0]):
            for y in range(self.window.H//taillecase[1]):
                self.coordMap.append((0+taillecase[0]*x,0+taillecase[1]*y))

    def __load(self,filename):
        f = Fichier(filename)
        if not f.existFile():
            print("Erreur le ficier n'existe pas")
            return
        self.encodageMap = f.lectureTable()
        for i in range(len(self.encodageMap)):
            self.encodageMap[i] = self.encodageMap[i].split(",")
        self.__mapBuild()

    def __mapBuild(self):
        for i in range(len(self.encodageMap)):
            for k in range(len(self.encodageMap[0])):
                if self.encodageMap[i][k] != 'None':
                    x,y = 0+50*k,0+50*i
                    tile = Tiles(int(self.encodageMap[i][k]),x,y)
                    self.add(tile)
                    #self.tileslist.append(tile)
        #self.nbtile = len(self.tileslist)

    def aff(self,window):
        self.draw(window.window)

class Tiles(pygame.sprite.Sprite):
    def __init__(self,name,x,y):
        super().__init__()
        tile_table = load_tile_table('assets/img/map/tileset.png',36,36) # a changer
        self.image = pygame.transform.scale(tile_table[name],(50,50)) # a changer utiliser l'objet Image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect


class scanner(pygame.sprite.Sprite):
    def __init__(self):
        pass

