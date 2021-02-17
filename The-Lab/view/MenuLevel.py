from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
class MenuLevel:
    def __init__(self):
        self.img = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img2 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img3 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img4 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img5 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img6 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img7 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img8 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img9 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.img10 = Image('assets/img/logo/Metre nom de l image du premier jeux.png');self.imgretour = Image('assets/img/logo/metre nom d image du button retour')#créer les objets images
        self.img.resize(25,25);self.img2.resize(25,25);self.img3.resize(25,25);self.img4.resize(25,25);self.img5.resize(200,50);self.img6.resize(200,50);self.img7.resize(200,50);self.img8.resize(200,50);self.img9.resize(200,50);self.img10.resize(200,50);self.imgretour.resize(200,50) #redimentionne les images
        self.font= Font(10,'Thick',salmon);self.font2= Font(8,'Thick',salmon)#les polices
        self.button = [Button(self.img,self.font,'niveau 1'),Button(self.img2,self.font,'niveau 2'),Button(self.img3,self.font,'niveau 3'),Button(self.img4,self.font,'niveau 4'),Button(self.img5,self.font,'niveau 5'),Button(self.img6,self.font,'niveau 6'),Button(self.img7,self.font,'niveau 7'),Button(self.img8,self.font,'niveau 8'),Button(self.img9,self.font,'niveau 9'),Button(self.img10,self.font,'niveau 10'),Button(self.imgretour,self.font2,'Retour')]
        #self.function = [lambda : self.__view('menulevel'), lambda : self.__view('gameendless') , lambda : self.__view('gamecharger') ,lambda : self.__view('menu')]
    


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
        self.button[10].aff(window,25,25)
        for i in range(0,len(self.button)-1):
            self.button[i].aff(window,150+100*i,200+100*i)
        
