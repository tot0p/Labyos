import pygame
from moteur.fichier import Fichier
from moteur.labyrinthe import Labyrinthe

class Map(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.tileslist = []  #liste d'objet des tiles
        self.nbtile = 0
        self.encodageMap = []
        self.coordMap =[]

    def __createCoordMap(self):
        for x in range(self.x//50):
            for y in range(self.y//50):
                self.coordMap.append((0+50*x,0+50*y))

    def load(self,filenameMap,filenameCode):
        fichier = Fichier(filenameMap)
        code = Fichier(filenameCode)
        exist = fichier.existFile() and code.existFile()
        if not exist:
            return
        self.encodageMap = fichier.lectureTable()
        for i in range(len(self.encodageMap)):
            self.encodageMap[i] = self.encodageMap[i].split(",")
        self.y = len(self.encodageMap)
        self.x = self.__verifX()
        self.__createCoordMap()

    def create(self,x,y):
        self.x,self.y = x,y
        self.__createCoordMap()
        self.encodageMap = Labyrinthe(self.coordMap)
        f = Fichier('t.txt')
        f.createFile()
        f.writeTable(self.encodageMap)
        
        
    def __verifX(self):
        t = len(self.encodageMap[0])
        for i in self.encodageMap:
            if i != t:
                print('error')
        return t

    def __mapBuild(self):
        for i in range(self.y):
            for k in range(self.x):
                if self.encodageMap[i][k] != 'None':
                    x,y = 0+50*k,0+50*i
                    tile = Tile(int(self.encodageMap[i][k]),x,y)
                    self.add(tile)
                    self.tileslist.append(tile)
        self.nbtile = len(self.tileslist)

    def get_rect(self,n):
        return self.tileslist[n].get_rect()

    def aff(self,surface):
        self.draw(surface)

class Items(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

class Tiles(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()


