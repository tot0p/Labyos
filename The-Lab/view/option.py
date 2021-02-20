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
        self.img = Image('assets/img/logo/1');self.img2 = Image('assets/img/logo/2');self.img3= Image('assets/img/logo/3'); self.img4=Image('assets/img/logo/4');self.imgApply=Image('assets/img/logo/apply');self.imgretour = Image('assets/img/logo/retour')
        self.img.resize(200,50);self.img2.resize(200,50);self.img3.resize(250,50);self.img4.resize(200,50);self.imgretour.resize(50,50);self.imgApply.resize(200,50)
        self.font= Font(,'Thick',salmon)
        self.font2=Font(8,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Avancer'),Button(self.img2,self.font,'reculer'),Button(self.img2,self.font,'gauche'),Button(self.img2,self.font,'droite')]
        self.retour = Button(self.imgretour,self.font,'Retour')
        self.attribut = ["avancer","reculer","aller a gauche","aller a droite"]
        self.buttonApply = Button(self.imgApply,self.font,'Apply')
        self.view = ['option',False]


    def events(self,event):
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],lambda : self.__change(self.attribut[i],event))
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
        pass

    def aff(self,window):
        window.reload(500,500)
        self.buttonApply.aff(window,150,450)
        self.retour.aff(window,25,25)
        for i in range(len(self.button)):
                self.button[i].aff(window,150,50+100*i)

        



    def __apply(self):
        self.file.variableFileWrite(self.touche)
        
    def __change(self,attribut:str,event):
            self.touche[attribut] = str(keypressed(event))




