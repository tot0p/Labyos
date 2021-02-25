from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *


class GameOver:

    def __init__(self):
        self.img = Image('assets/img/button/200x50.png');self.img2 = Image('assets/img/button/200.50.png');self.imgretour = Image('assets/img/button/retour.png')#créer les objets images
        self.img.resize(200,50);self.img2.resize(200,50);self.imgretour.resize(50,50) #redimentionne les images
        self.font= Font(40,'Thick',salmon);self.font2= Font(8,'Thick',salmon)#les polices
        self.button = [Button(self.img,self.font,'Réessayer'),Button(self.img2,self.font,'Retour aux Menu')]
        self.buttonretour = Button(self.imgretour,self.font2)
        #self.function = [lambda : self.__view('menulevel'), lambda : self.__view('Menu') 
        self.view = ['gameover',False]


    def aff(self,window):
        window.reload(500,500)
        self.font.aff(window,'vous etes decedez',150,150)
        for i in range(len(self.button)):
                self.button[i].aff(window,150+100*i,350)


    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return v
        return self.view