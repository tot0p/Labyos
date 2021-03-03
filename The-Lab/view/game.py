from moteur.map import Map
#import random
from view.Load import Load
from moteur.time import wait
from moteur.event import *
from moteur.player import Player
from moteur.event import keypressed
from moteur.fichier import Fichier
from moteur.codeFile import codeFile


class Game:

    def __init__(self,window,filename): 
        self.window = window
        self.isFin = False
        self.__load()
        file =Fichier('donne/touche.txt')
        touche = file.variableFileLecture()
        self.av = int(touche['avancer'])
        self.re = int(touche['reculer'])
        self.le = int(touche['gauche'])
        self.ri = int(touche['droite'])
        self.pressed = {self.av : False , self.re : False , self.le : False,self.ri : False}
        self.view = ['game',False,filename]
        self.player = Player('assets/img/player/IDLE.png','assets/img/player/RUNDOWN.png')
        self.code = codeFile(window,filename,self.player,self)
        self.map = self.code.get_map()
        self.naration = self.code.get_narration()
        self.player.def_map(self.map)
        self.fin = []

    def __load(self):
        '''
        permet d'afficher l'ecran de chargement le temp de chargement + 2 secondes
        '''
        load = Load()
        load.aff(self.window)
        self.window.update()
        wait(2000)

    def __control(self,event):
        '''
        defini les controle du jouer avec event un event pygame
        '''
        rect = self.player.get_rect()
        if self.pressed[self.av] and rect.y > 0 : self.player.move_on_axe_y(False)
        elif self.pressed[self.re] and rect.y+50 <500 :self.player.move_on_axe_y()
        elif self.pressed[self.le] and rect.x > 0:self.player.move_on_axe_x(False)
        elif self.pressed[self.ri]  and rect.x + 50 < 500 :self.player.move_on_axe_x()
        else:self.player.move=False

    def load_event(self,initGame,endGameInLife,endGameDead):
        '''
        permet de charger les events du fichier code.txt
        '''
        self.initGame = initGame
        #self.inGame = inGame
        self.endGameInLife = endGameInLife
        self.endGameDead = endGameDead

    def events(self,event):
        '''
        permet de gerer les events en general avec event un event pygame
        et return la view sur laquelle le programme doit etre
        '''
        if event.type == pygame.KEYDOWN:
            self.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            self.pressed[event.key] = False
        self.__control(event)
        evgame = self.player.inter()
        if evgame == 'mort'and self.isFin == False:
            self.isFin = True
            for i in self.endGameDead:
                i()    
            self.fin = ['gameover',True,self.view[2]]
        elif evgame == 'fin' and self.isFin == False:
            self.isFin = True
            for i in self.endGameInLife:
                i()
            self.fin = ['win',True,'']

    def viewIs(self):
        if self.naration.stop() and self.fin != []:
            t = self.fin
            self.fin = []
            return t
        return self.view

    def eventEscape(self,event):
        '''
        return True ou False et event et un event pygame
        '''
        return escapeandkey(event)
    
    def affUpdate(self):
        '''
        permet de mettre a jour l'affichage du jeu
        '''
        if self.naration.stop():
            self.map.aff(self.window,self.player.rect)
            self.player.affUpdate(self.window)
        else:
            self.naration.affupdate()

    def aff(self):
        '''
        permet d' afficher le jeu pour la premiere fois
        '''
        self.window.reload(500,500)
        for i in self.initGame:
            i()
        self.map.aff(self.window,self.player.rect)

        self.player.aff(self.window)
        