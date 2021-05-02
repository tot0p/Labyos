from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.func import whatislang


class GameOver:

    def __init__(self):
        self.img = Image('assets/img/button/200x50.png');self.img2 = Image('assets/img/button/200x50.png');self.imgretour = Image('assets/img/button/retour.png')#créer les objets images
        self.img.resize(200,50);self.img2.resize(200,50);self.imgretour.resize(50,50) #redimentionne les images
        self.font= Font(20,'Thick',salmon);self.font2= Font(8,'Thick',salmon);self.font3= Font(13,'Thick',salmon)#les polices
        self.button = [Button(self.img,self.font,'Ressayer'),Button(self.img2,self.font3,'Retour aux Menu')]
        self.buttonretour = Button(self.imgretour,self.font2)
        self.filename = ''
        self.function = [lambda : self.__view('game',self.filename), lambda : self.__view('menu','')]
        self.view = ['gameover',False,'']

    def set_filename(self,filename):
        self.filename = filename

    def __view(self,name,filename):
        #self.view = [name,True]
        return [name,True,filename]


    def aff(self,window):
        window.reload(500,500)
        if whatislang(self.filename) == "english":
            self.font.aff(window,'you are dead',150,150)
            self.button = [Button(self.img,self.font,'Try again'),Button(self.img2,self.font3,'Back to Menu')]
        else:
            self.font.aff(window,'vous etes mort',100,150)
            self.button = [Button(self.img,self.font,'Ressayer'),Button(self.img2,self.font3,'Retour aux Menu')]
        for i in range(len(self.button)):
                self.button[i].aff(window,35+250*i,350)


    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return v
        return self.view


    
    def eventEscape(self,event):
        return escape(event)