from moteur.map import Map
#import random
from view.Load import Load

class Game:

    def __init__(self,window,filname):
        self.window = window
        self.view = []
        self.map = Map(window,filname)
        self.__load()

    def __load(self):
        load = Load()
        load.aff(self.window)
        