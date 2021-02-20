from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.fichier import *

#g{avancer : z,reculer : s,aller a gauche : q,aller a droite : d}
#g['avancer'] 
class Option:
    def __init__(self):
        self.file = Fichier('donne/touche.txt')
        self.touche = self.file.variableFileLecture()  
        self.img = Image('assets/img/logo/1');self.img2 = Image('assets/img/logo/2');self.img3= Image('assets/img/logo/3'); self.img4=Image('assets/img/logo/4')
        self.img.resize(83,83);self.img2.resize(83,83);self.img3.resize(83,83);self.img4.resize(83,83)
        self.font= Font(40,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Avancer'),Button(self.img2,self.font,'reculer'),Button(self.img2,self.font,'gauche'),Button(self.img2,self.font,'droite')]
        buttonApply = Button('',fsfd,'Apply')


    def events(self,event):
        


    def __apply(self):
        self.file.variableFileWrite(self.touche)
        
    def __change(self,attribut:str,event)
            self.touche[attribut] = str(keypressed(event))



