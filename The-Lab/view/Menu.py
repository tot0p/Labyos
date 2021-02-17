#import
from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
class Menu:

    def __init__(self):
        self.img = Image('assets/img/logo/testimage.png')
        self.img2 = Image('assets/img/logo/testimage2.png')
        self.img3 = Image('assets/img/logo/testimage3.png')
        self.img.resize(200,50)
        self.img2.resize(200,50)
        self.img3.resize(200,50)
        self.text= Font('Jouer',40,'Future',salmon) # peut changer
        self.text2=Font('option',40,'Future',salmon)
        self.text3=Font('quiter',40,'Future',salmon)
        self.b = Button(self.img,self.text)
        self.b2=Button(self.img2,self.text2)
        self.b3=Button(self.img3,self.text3)
        self.button = [Button(self.img,self.text),Button(self.img2,self.text2),Button(self.img3,self.text3)]
        self.function = [lambda : self.__view('menujouer'), lambda : self.__view('option') , self.__exit]
        self.exit = False
        self.view = ['menu',False]


    def __exit(self):
        self.exit = True

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
        return escape(event) and not self.exit

    def aff(self,window):
        
        window.reload(500,500)
        for i in range(len(self.button)):
            self.button[i].aff(window,150,200+100*i)
