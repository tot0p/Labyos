import pygame
from moteur.fichier import Fichier

class Map(pygame.sprite.Group):

    def __init__(self,tx,ty):
        super().__init__()
        self.x = tx
        self.y = ty
        self.coordMap =[]
        for x in range(tx/50):
            for y in range(ty/50):
                self.coordMap.append((0+50*x,0+50*y))

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



class Tiles(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()


