from moteur.map import Map
#import random
from view.Load import Load
from moteur.time import wait
from moteur.event import *

class Game:

    def __init__(self,window,filname):
        self.window = window
        self.view = []
        self.map = Map(window,filname)
        self.__load()

    def __load(self):
        load = Load()
        load.aff(self.window)
        self.window.update()
        wait(2000)

    def eventEscape(self,event):
        return escapeandkey(event)

    def aff(self):
        self.window.reload(500,500)
        self.window.set_fullscreen()
        self.map.aff(self.window)
        #pass
        