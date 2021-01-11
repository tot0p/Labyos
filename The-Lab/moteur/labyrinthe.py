import random
import time


class Labyrinthe:

    def __init__(self,coordMap):
        self.coordMap = coordMap
        self.encodageLab = []
        self.visited = []
        self.__createEncodageMap()
        return self.encodageLab


    def __createEncodageMap(self):
        cursor = self.coordMap[0][0]
