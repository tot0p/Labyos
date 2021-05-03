from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.time import Chrono



class Win:

    def __init__(self):
       
        self.img = Image('assets/img/button/200x50.png');self.img2 = Image('assets/img/button/200x50.png');self.imgretour = Image('assets/img/button/retour.png')
        self.img.resize(200,50);self.img2.resize(200,50);self.imgretour.resize(50,50)
        self.font= Font(20,'Thick',salmon);self.font2= Font(8,'Thick',salmon); self.font3= Font(13,'Thick',salmon);self.font4= Font(11,'Thick',salmon)
        self.button = [Button(self.img,self.font4,'Retour aux Levels'),Button(self.img2,self.font3,'Retour aux Menu')]
        self.buttonretour = Button(self.imgretour,self.font2)
        self.function = [lambda : self.__view('menulevel',''), lambda : self.__view('menu','')]
        self.view = ['win',False,'']
        self.chrono= Chrono()
        self.playerimg = Image('assets/img/player/IDLE.png')
        self.playerimg.split(36,36,0)
        self.playerimg.resize_all_tile(150,150)
        self.nIDLE = 0


    def __view(self,name,filename):
        '''
        fonction qui prend en paramètre name et filename et qui renvoie une liste qui comprend le nom, un bool qui vaut True et le nom du File
        '''
        #self.view = [name,True]
        return [name,True,filename]


    def set_filename(self,filename):
        self.filename = filename

    def affUpdate(self,window):
        '''
        fonction qui met a jour l'affichage
        '''
        if self.chrono.get_val()%10 == 0:
                self.nIDLE +=1
                if self.nIDLE > 7:
                    self.nIDLE = 0
                self.playerimg.changeImagewithtiletable(self.nIDLE)
                self.playerimg.aff(window,175,175)

    def aff(self,window,lang):
        '''
        Fonction qui affiche un message lorsque le joueur à gagner
        '''
        window.reload(500,500)
        if lang == "english":
            self.font.aff(window,'You have succeeded',75,125)
            self.button = [Button(self.img,self.font4,'Back to Levels'),Button(self.img2,self.font3,'Back to Menu')]
        else:
            self.font.aff(window,'Vous avez reussie',100,125)
            self.button = [Button(self.img,self.font4,'Retour aux Levels'),Button(self.img2,self.font3,'Retour aux Menu')]
        # affiche le perso
        for i in range(len(self.button)):
                self.button[i].aff(window,25+250*i,350)
        self.playerimg.aff(window,175,175)

    
    def events(self,event):
        '''
        fonction qui prend en parametre un event et qui renvoie une liste qui est constituer d'un str win, d'un bool False et d'un str vide(self.view)
        '''
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return v
        return self.view


    
    def eventEscape(self,event):
        '''
        Fonction qui prend en paramètre un event pygame et qui renvoie ce que renvoie la fonction escape avec comme paramètre event
        '''
        return escape(event)