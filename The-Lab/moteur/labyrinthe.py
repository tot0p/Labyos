import random
import time


class Labyrinthe:

    def __init__(self,coordMap):
        self.encodageLab = []
        self.visited = []
        self.__createEncodageMap(coordMap)
        return self.encodageLab


    def __createEncodageMap(self,grid):
        pass