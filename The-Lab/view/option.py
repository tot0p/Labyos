from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.fichier import Fichier
from moteur.forme import draw_fill_rectangle , Point

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
        self.view = ['option',False,'']
        self.keychange = [False,None,None]


    def events(self,event):
        '''
        fonction qui prend en paramètre un event pygame et qui renvoie une liste qui est constituer d'un str option et d'un bool False 
        '''
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],lambda : self.__change(self.attribut[i]))
                    if g:
                        return self.view
                g , v = self.retour.EventClic(posCursor[0],posCursor[1],lambda :self.__echap())
                if g:
                    return v
                g ,v = self.buttonApply.EventClic(posCursor[0],posCursor[1],lambda : self.__apply())
                return self.view
            if self.keychange[0] and self.keychange[1] is not None and self.keychange[2] is not None:
                    self.touche[self.keychange[1]] = str(self.keychange[2])
                    self.keychange[0] = False
            elif self.keychange[0] and self.keychange[1] is not None:
                if event.type == pygame.KEYDOWN:
                    self.keychange[2] = event.key
        return self.view

    def __echap(self):
        '''
        fonction permet de retourner a la vue menu
        '''
        self.touche = self.file.variableFileLecture()  
        return ['menu',True,'']
                

    def eventEscape(self,event):
        '''
        Fonction qui prend en paramètre un event pygame et qui renvoie ce que renvoie la fonction escape avec comme paramètre event
        '''
        return escape(event)

    def __affall(self,window):
        self.buttonApply.aff(window,150,450)
        self.retour.aff(window,25,25)
        self.font.aff(window,pygame.key.name(int(self.touche['avancer'])),400,65)
        self.font.aff(window,pygame.key.name(int(self.touche['reculer'])),400,165)
        self.font.aff(window,pygame.key.name(int(self.touche['gauche'])),400,265)
        self.font.aff(window,pygame.key.name(int(self.touche['droite'])),400,365)
        self.font.aff(window,'vaut',300,65)
        self.font.aff(window,'vaut',300,165)
        self.font.aff(window,'vaut',300,265)
        self.font.aff(window,'vaut',300,365)
        for i in range(len(self.button)):
                self.button[i].aff(window,100,50+100*i)

    def affUpdate(self,window):
        '''
        fonction qui prend en paramètre: window de type Window
        sert a afficher la touche utiliser
        '''
        print('il marche tu va rager')
        draw_fill_rectangle(Point(250,250),500,500,black,window)
        self.__affall(window)
        #self.font.aff(window,pygame.key.name(int(self.touche['avancer'])),400,65)
        #self.font.aff(window,pygame.key.name(int(self.touche['reculer'])),400,165)
        #self.font.aff(window,pygame.key.name(int(self.touche['gauche'])),400,265)
        #self.font.aff(window,pygame.key.name(int(self.touche['droite'])),400,365)

    def aff(self,window):
        '''
        fonction qui prend en paramètre: window de type Window
        elle permet d'afficher les button, les str '='  
        '''
        window.reload(500,500)
        self.__affall(window)

    def __apply(self):
        '''
        Fonction qui sert a afficher les nouvelle option
        '''
        self.file.variableFileWrite(self.touche)
        
    def __change(self,attribut:str):
        '''
        Fonction qui prend un attribut : str
        '''
        self.keychange = [True,attribut,None]