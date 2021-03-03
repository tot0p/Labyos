from moteur.Button import Button
from moteur.Image import Image
from moteur.text import Font
from moteur.color import *
from moteur.time import Chrono
class Naration:

    def __init__(self,window):
        self.delay = []
        self.window = window
        self.chrono = Chrono()
        self.imgb = Image('assets/img/histoiretile.png')
        self.imgb.split(500,500,0)
        self.imgg = Image('assets/img/button/100x25.png')
        self.imgm = Image('assets/img/button/150x120.png')
        self.replic = []
        self.font = Font(10)
        self.font1 = Font(30)
        self.nIDLE = 0
        self.nReplic = 0
        self.rect = self.imgb.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def aff(self):
        """
        fonction qui permet d'afficher la premiere image du gif qui tourne en fond
        """
        self.imgb.aff(self.window,self.rect.x,self.rect.y)

    def affupdate(self):
        """
        fonction qui permet d'afficher le gif en mouvement en arriere plan 
        """
        if self.chrono.get_val()%10 == 0:
            self.nIDLE += 1
            if self.nIDLE > 7:
                self.nIDLE = 0
            self.imgb.changeImagewithtiletable(self.nIDLE)
        self.imgb.aff(self.window,self.rect.x,self.rect.y)
        self.replic[self.nReplic]()
        if self.chrono.get_val()%self.delay[self.nReplic] == 0:
            self.nReplic += 1
        
            

    
    def addreplic(self,text:str,gentil:bool,delay):
        """
        fonction qui permet d'afficher la réplique du personnage voulu avec un delai prechoisie en milisecond
        """
        self.delay.append(delay)
        self.replic.append(lambda:self.__affreplic(text,gentil))

    def __affreplic(self,text:str,gentil:bool):
        """
        fonction permet d'afficher la replique choisi selon le personnage choisi avec le delai choisi en milisecond
        la replique fait un saut de ligne a chaque '/'
        """
        
        t = text.split("/")
        y = 200 - 15 * (len(t)-1)
        for i in range(len(t)):
            if gentil == True :
                #self.imgg.aff(self.window,100,200)
                self.font1.aff(self.window,t[i],110,y + i * 15)
            elif gentil == False :
                #self.imgm.aff(self.window,280,200)
                self.font.aff(self.window,t[i],320,y + i * 15)

    def stop(self):
        """
        fonction qui permet d'arreter le gif en arriere plan
        """
        return len(self.replic) == self.nReplic

    def reset(self):
        """
        fonction qui remet les valeurs du delai et des repliques a leur valeur initial
        """
        self.delay = []
        self.replic = []
        self.nReplic = 0