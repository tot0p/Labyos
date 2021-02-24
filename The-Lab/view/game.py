from moteur.map import Map
#import random
from view.Load import Load
from moteur.time import wait
from moteur.event import *
from moteur.player import Player
from moteur.event import keypressed
from moteur.fichier import Fichier
from moteur.codeFile import codeFile
from tkinter.filedialog import *
from tkinter import Tk

class Game:

    def __init__(self,window):
        tk = Tk()
        tk.geometry("0x0")
        tk.iconbitmap('assets/img/logo/logo.ico')
        filename = askopenfilename(initialdir="/Desktop", title="Ouvrir", filetypes=(("Text Files","*.txt"),("Python Files","*.py"),("all files","*.*")))   
        tk.destroy() 
        self.window = window
        self.__load()
        file =Fichier('donne/touche.txt')
        touche = file.variableFileLecture()
        self.av = int(touche['avancer'])
        self.re = int(touche['reculer'])
        self.le = int(touche['gauche'])
        self.ri = int(touche['droite'])
        self.pressed = {self.av : False , self.re : False , self.le : False,self.ri : False}
        self.view = []
        self.player = Player('assets/img/player/IDLE.png','assets/img/player/RUNDOWN.png')
        self.code = codeFile(window,filename,self.player,self)
        self.map = self.code.get_map()
        self.player.def_map(self.map)

    def __load(self):
        load = Load()
        load.aff(self.window)
        self.window.update()
        wait(2000)

    def __control(self,event):
        rect = self.player.get_rect()
        if self.pressed[self.av] and rect.y > 0 and not self.player.prev_check_collision(0,-1): self.player.move_on_axe_y(False)
        elif self.pressed[self.re] and rect.y+50 <500 and not self.player.prev_check_collision(0,1):self.player.move_on_axe_y()
        elif self.pressed[self.le] and rect.x > 0 and not self.player.prev_check_collision(-1,0):self.player.move_on_axe_x(False)
        elif self.pressed[self.ri]  and rect.x + 50 < 500 and not self.player.prev_check_collision(1,0):self.player.move_on_axe_x()
        else:self.player.move=False

    def load_event(self,initGame,inGame,endGameInLife,endGameDead):
        self.initGame = initGame
        self.inGame = inGame
        self.endGameInLife = endGameInLife
        self.endGmeDead = endGameDead

    def events(self,event):
        if event.type == pygame.KEYDOWN:
            self.pressed[event.key] = True
            #event player
        elif event.type == pygame.KEYUP:
            self.pressed[event.key] = False
        #self.player.event(event)
        self.__control(event)
        print(self.player.inter())

    def eventEscape(self,event):
        return escapeandkey(event)
    
    def affUpdate(self):
        self.map.aff(self.window)
        self.player.affUpdate(self.window)

    def aff(self):
        self.window.reload(500,500)
        print(self.initGame)
        for i in self.initGame:
            print(i)
            i()
        self.map.aff(self.window)

        self.player.aff(self.window)
        #pass
        