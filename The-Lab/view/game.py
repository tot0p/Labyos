from moteur.map import Map
#import random
from view.Load import Load
from moteur.time import wait
from moteur.event import *
from moteur.player import Player
from moteur.event import keypressed

class Game:

    def __init__(self,window,filname):
        self.av = pygame.K_z
        self.re = pygame.K_s
        self.le = pygame.K_q
        self.ri = pygame.K_d
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

    def __control(self,event):
        key = keypressed(event)
        rect = self.player.get_rect()
        if key == self.av and rect.y > 0 and not self.player.prev_check_collision(0,-1): self.player.move_on_axe_y(False)
        elif key == self.re and rect.y+50 <500 and not self.player.prev_check_collision(0,1):self.player.move_on_axe_y()
        elif key == self.le and rect.x > 0 and not self.player.prev_check_collision(-1,0):self.player.move_on_axe_x(False)
        elif key ==self.ri  and rect.x + 50 < 500 and not self.player.prev_check_collision(1,0):self.player.move_on_axe_x()
        else:self.player.move=False

    def events(self,event):
        #self.player.event(event)
        self.__control(event)

    def eventEscape(self,event):
        return escapeandkey(event)
    
    def affUpdate(self):
        self.map.aff(self.window)
        self.player.affUpdate(self.window)

    def aff(self):
        self.window.reload(500,500)
        self.map.aff(self.window)
        self.player.aff(self.window)
        print(self.map.listoftiles)
        #pass
        