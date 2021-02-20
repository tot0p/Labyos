from moteur.map import Map
#import random
from view.Load import Load
from moteur.time import wait
from moteur.event import *
from moteur.player import Player

class Game:

    def __init__(self,window,filname):
        self.window = window
        self.view = []
        self.map = Map(window,filname)
        self.player = Player(self.map,'assets/img/player/IDLE.png','assets/img/player/RUNDOWN.png')
        self.__load()

    def __load(self):
        load = Load()
        load.aff(self.window)
        self.window.update()
        wait(2000)

    def events(self,event):
        self.player.event(event)

    def eventEscape(self,event):
        return escapeandkey(event)
    
    def affUpdate(self):
        self.map.aff(self.window)
        self.player.affUpdate(self.window)

    def aff(self):
        self.window.reload(500,500)
        self.map.aff(self.window)
        self.player.aff(self.window)

        #pass
        