#import
from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import escape
class Menu:

    def __init__(self):
        self.img = Image('assets/img/logo/testimage.png')
        self.img2 = Image('assets/img/logo/testimage2.png')
        self.img3 = Image('assets/img/logo/testimage3.png')
        self.img.resize(200,50)
        self.img2.resize(200,50)
        self.img3.resize(200,50)
        self.text= Font('Rousseau il est pas bo',100,'Future',salmon)
        self.text2=Font('i',100,'Future',salmon)
        self.text3=Font('i5',100,'Future',salmon)
        self.b = Button(self.img,self.text)
        self.b2=Button(self.img2,self.text2)
        self.b3=Button(self.img3,self.text3)


    def events(self,event):
        pass

    def affUpdate(self,window):
        pass

    def eventEscape(self,event):
        return escape(event)

    def aff(self,window):
        
        window.reload(500,500)
        self.b.aff(window,150,200)
        self.b2.aff(window,150,300)
        self.b3.aff(window,150,400)
