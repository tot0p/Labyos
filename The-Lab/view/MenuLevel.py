from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
class MenuLevel:
    def __init__(self):
        self.img = Image('assets/img/button/83x83.png');self.img2 = Image('assets/img/button/83x83.png');self.img3 = Image('assets/img/button/83x83.png');self.img4 = Image('assets/img/button/83x83.png');self.img5 = Image('assets/img/button/83x83.png');self.img6 = Image('assets/img/button/83x83.png');self.img7 = Image('assets/img/button/83x83.png');self.img8 = Image('assets/img/button/83x83.png');self.img9 = Image('assets/img/button/83x83.png');self.img10 = Image('assets/img/button/83x83.png');self.imgretour = Image('assets/img/button/retour.png')#créer les objets images
        self.img.resize(83,83);self.img2.resize(83,83);self.img3.resize(83,83);self.img4.resize(83,83);self.img5.resize(83,83);self.img6.resize(83,83);self.img7.resize(83,83);self.img8.resize(83,83);self.img9.resize(83,83);self.img10.resize(83,83);self.imgretour.resize(50,50) #redimentionne les images
        self.font= Font(40,'Thick',salmon);self.font2= Font(8,'Thick',salmon)#les polices
        self.button = [Button(self.img,self.font,'1'),Button(self.img2,self.font,'2'),Button(self.img3,self.font,'3'),Button(self.img4,self.font,'4'),Button(self.img5,self.font,'5'),Button(self.img6,self.font,'6'),Button(self.img7,self.font,'7'),Button(self.img8,self.font,'8'),Button(self.img9,self.font,'9'),Button(self.img10,self.font,'10'),Button(self.imgretour,self.font2)]
        self.function = [lambda : self.__view('game','assets/level/level1/code.txt'), lambda : self.__view('game','assets/level/level2/code.txt') , lambda : self.__view('game','assets/level/level3/code.txt') , lambda : self.__view('game','assets/level/level4/code.txt') , lambda : self.__view('game','assets/level/level5/code.txt'), lambda : self.__view('game','assets/level/level6/code.txt') , lambda : self.__view('game','assets/level/level7/code.txt'), lambda : self.__view('game','assets/level/level8/code.txt') , lambda : self.__view('game','assets/level/level9/code.txt'), lambda : self.__view('game','assets/level/level10/code.txt') ,lambda : self.__view('menujouer','')]
        self.view = ['menulevel',False,'']
    


    def __view(self,name,filename):
        #self.view = [name,True]
        return [name,True,filename]



    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g ,v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return v

        return self.view


    def affUpdate(self,window):
        pass

    def eventEscape(self,event):
        return escape(event)

    def aff(self,window):
        
        window.reload(500,500)
        self.button[10].aff(window,25,25)
        for i in range(0,len(self.button)-1):
            self.button[i].aff(window,41+166*(i%3),100+100*(i//3))
        
