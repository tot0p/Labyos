from moteur.Button import Button
from moteur.Image import Image
from moteur.text import Font
from moteur.color import *
from moteur.time import Chrono
class Naration:
    """
    En cours de développement, Bug à résoudre
    """
    def __init__(self):
        self.chrono = Chrono()
        self.img = Image('assets/img/histoiretile.png')
        self.imgg = Image('assets/img/button/100x25.png')
        self.imgm = Image('assets/img/button/150x120.png')
        self.font = Font(15)
        self.button1 = Button(self.imgg,self.font)
        self.button2 = Button(self.imgm,self.font)
        self.nIDLE = 0
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def aff(self,window):
        if self.chrono.get_val()%10 == 0:
            self.nIDLE +=1
            if self.nIDLE > 7:
                self.nIDLE = 0
            self.img.changeImagewithtiletable(self.nIDLE)
        self.img.aff(window,self.rect.x,self.rect.y)

    def affupdate(self,window,joueur:bool,text:str):
        if joueur == True :
            self.button1.aff(window,100,225)
            self.font.aff(window,text,100,225)
        else :
            self.button2.aff(windown,280,180)
            self.font.aff(window,text,280,180)

        