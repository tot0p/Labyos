from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
class MenuJouer:

    def __init__(self):
        self.img = Image('assets/img/logo/Metre nom de l image du premier jeux.png')
        self.img2 = Image('assets/img/logo/Metre nom de l image du premier jeux.png')
        self.img3 = Image('assets/img/logo/Metre nom de l image du premier jeux.png')
        self.img4 = Image('assets/img/logo/metre nom d image du button retour')
        self.img.resize(200,50)
        self.img2.resize(200,50)
        self.img3.resize(200,50)
        self.img4.resize(50,50)
        self.font= Font(20,'Thick',salmon) 
        self.font2= Font(8,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Histoire'),Button(self.img2,self.font,'Endless'),Button(self.img3,self.font,'Créatif'),Button(self.img4,self.font2,'Retour')]
        self.function = [lambda : self.__view('menulevel'), lambda : self.__view('gameendless') , lambda : self.__view('gamecharger') ,lambda : self.__view('menu')]
        self.view = ['menu',False]

    def __view(self,name):
        self.view = [name,True]


    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return self.view
        return self.view

    def affUpdate(self,window):
        pass


    def eventEscape(self,event):
        return escape(event)

    def aff(self,window):
        
        window.reload(500,500)
        self.button[3].aff(window,25,25)
        for i in range(0,len(self.button)-1):
                self.button[i].aff(window,150,200+100*i)