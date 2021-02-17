from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
class MenuJouer:

    def __init__(self):
        self.img = Image('assets/img/logo/Metre nom de l image du premier jeux.png')
        self.img2 = Image('assets/img/logo/Metre nom de l image du deuxième jeux jeux.png')
        self.img3 = Image('assets/img/logo/Metre nom de l image du troisième jeux.png')
        self.img4 = Image('assets/img/logo/metre nom d image du button retour')
        self.img.resize(200,50)
        self.img2.resize(200,50)
        self.img3.resize(200,50)
        self.img4.resize(50,50)
        self.title= Font('Mode',40,'Future',salmon)
        self.text= Font('Jeux 1',40,'Future',salmon) # peut changer
        self.text2=Font('Jeux 2',40,'Future',salmon)
        self.text3=Font('Jeux 3',40,'Future',salmon)
        self.text4= Font('retour',10,'Future',salmon)
        self.button = [Button(self.img,self.text),Button(self.img2,self.text2),Button(self.img3,self.text3),Button(self.img4,self.text4)]
     #   self.function = [lambda : self.__view('menujouer'), lambda : self.__view('option') , self.__exit]
        self.view = ['menu',False]

    def __view(self,name):
        self.view = [name,True]


    def events(self,event):
        print(self.view)
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
        self.title.aff(window,150,50)
        self.button[3].aff(window,25,25)
        for i in range(0,len(self.button)-1):
                self.button[i].aff(window,150,200+100*i)