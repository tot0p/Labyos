from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.fichier import Fichier

#g{avancer : z,reculer : s,aller a gauche : q,aller a droite : d}
#g['avancer'] 
class Option:

    def __init__(self):
        self.file = Fichier('donne/touche.txt')
        self.touche = self.file.variableFileLecture()  
        self.img = Image('assets/img/vide.png');self.img2 = Image('assets/img/vide.png');self.img3= Image('assets/img/vide.png'); self.img4=Image('assets/img/vide.png');self.imgApply=Image('assets/img/button/200x50.png');self.imgretour = Image('assets/img/button/retour.png')
        self.img.resize(200,50);self.img2.resize(200,50);self.img3.resize(200,50);self.img4.resize(200,50);self.imgretour.resize(50,50);self.imgApply.resize(200,50)
        self.font= Font(20,'Thick',salmon)
        self.font2=Font(8,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Avancer'),Button(self.img2,self.font,'reculer'),Button(self.img3,self.font,'gauche'),Button(self.img4,self.font,'droite')]
        self.retour = Button(self.imgretour,self.font2)
        self.attribut = ["avancer","reculer","gauche","droite"]
        self.buttonApply = Button(self.imgApply,self.font,'Apply')
        self.view = ['option',False]


    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],lambda : self.__change(self.attribut[i]))
                    if g:
                        return self.view
                g , v = self.retour.EventClic(posCursor[0],posCursor[1],lambda :self.__view('menu'))
                if g:
                    return v
                g ,v = self.buttonApply.EventClic(posCursor[0],posCursor[1],lambda : self.__apply())
                return self.view

                    
        return self.view

    def __view(self,name):
        return [name,True]
                

    def eventEscape(self,event):
        return escape(event)

    def affUpdate(self,window):
        self.font.aff(window,pygame.key.name(int(self.touche['avancer'])),400,65)
        self.font.aff(window,pygame.key.name(int(self.touche['reculer'])),400,165)
        self.font.aff(window,pygame.key.name(int(self.touche['gauche'])),400,265)
        self.font.aff(window,pygame.key.name(int(self.touche['droite'])),400,365)

    def aff(self,window):
        window.reload(500,500)
        self.buttonApply.aff(window,150,450)
        self.retour.aff(window,25,25)
        self.font.aff(window,pygame.key.name(int(self.touche['avancer'])),400,65)
        self.font.aff(window,pygame.key.name(int(self.touche['reculer'])),400,165)
        self.font.aff(window,pygame.key.name(int(self.touche['gauche'])),400,265)
        self.font.aff(window,pygame.key.name(int(self.touche['droite'])),400,365)
        self.font.aff(window,'=',350,65)
        self.font.aff(window,'=',350,165)
        self.font.aff(window,'=',350,265)
        self.font.aff(window,'=',350,365)
        self.affUpdate(window)
        for i in range(len(self.button)):
                self.button[i].aff(window,150,50+100*i)

        



    def __apply(self):
        self.file.variableFileWrite(self.touche)
        
    def __change(self,attribut:str):
        key = None
        while key == None:
            for event in get_event():
                if event.type == pygame.KEYDOWN:
                    key = event.key
            
        self.touche[attribut] = str(key)




