#import
from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
class Menu:

    def __init__(self):
        self.img = Image('assets/img/button/200x50.png')
        self.img2 = Image('assets/img/button/200x50.png')
        self.img3 = Image('assets/img/button/200x50.png')
        self.img.resize(200,50)
        self.img2.resize(200,50)
        self.img3.resize(200,50)
        self.font= Font(20,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Jouer'),Button(self.img2,self.font,'Option'),Button(self.img3,self.font,'Quitter')]
        self.function = [lambda : self.__view('menujouer'), lambda : self.__view('option') , self.__exit]
        self.exit = False
        self.view = ['menu',False]


    def __exit(self):
        self.exit = True

    def __view(self,name):
        #self.view = [name,True]
        return [name,True]
        

    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return v
        return self.view

    def affUpdate(self,window):
        pass

    def eventEscape(self,event):
        return escape(event) and not self.exit

    def aff(self,window):
        
        window.reload(500,500)
        for i in range(len(self.button)):
            self.button[i].aff(window,150,200+100*i)
