import pygame
from moteur.fichier import Fichier

class Map(pygame.sprite.Group):

    def __init__(self,tx,ty):
        super().__init__()
        self.x = tx
        self.y = ty
        self.tileslist = []  #liste d'objet des tiles
        self.nbtile = 0
        self.encodageMap = []
        self.coordMap =[]
        for x in range(tx//50):
            for y in range(ty//50):
                self.coordMap.append((0+50*x,0+50*y))
                print((0+50*x,0+50*y))

    def load(self,filename):
        fichier = Fichier(filename)
        exist = fichier.existFile()
        if not exist:
            return
        self.encodageMap = fichier.lectureTable()
        for i in range(len(self.encodageMap)):
            self.encodageMap[i] = self.encodageMap[i].split(",")
        self.__mapBuild()
        self.__listrectBuild()

    def __mapBuild(self):
        for i in range(len(self.encodageMap)):
            for k in range(len(self.encodageMap[0])):
                if self.encodageMap[i][k] != 'None':
                    x,y = 0+50*k,0+50*i
                    if self.encodageMap[i][k] == 'c':
                        self.listCoin.add(Coin(x,y))
                    else:
                        tile = Tile(int(self.encodageMap[i][k]),x,y)
                        self.add(tile)
                        self.tileslist.append(tile)
        self.nbtile = len(self.tileslist)

    def __listrectBuild(self):
        for i in range(self.nbtile):
            rect = self.get_rect(i)
            self.listRect.append([(rect.x,rect.y),(rect.x+rect.width,rect.y),(rect.x,rect.y+rect.height),(rect.x+rect.width,rect.y+rect.height)])



class Tiles(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()


