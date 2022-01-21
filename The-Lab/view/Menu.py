#import
from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *

#Dany Costa , modifié par Thomas lemaitre pour l'ajout de la langue

class Menu:

    def __init__(self):
        self.img = Image('assets/img/button/200x50.png')
        self.img2 = Image('assets/img/button/200x50.png')
        self.img3 = Image('assets/img/button/200x50.png')
        self.img.resize(200,50)
        self.img2.resize(200,50)
        self.img3.resize(200,50)
        self.logo = Image('assets/img/logo/logo.png')
        self.logo.resize(100,100)
        self.font= Font(20,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Jouer'),Button(self.img2,self.font,'Option'),Button(self.img3,self.font,'Quitter')]
        self.function = [lambda : self.__view('menujouer'), lambda : self.__view('option') , self.__exit]
        self.view = ['menu',False,'']
        self.exit = False


    def __exit(self):
        '''
        fonction qui donne la valeur True a self.exit
        '''
        self.exit = True

    def __view(self,name):
        '''
        fonction qui prend en parametre name et qui renvoie une liste qui comprend name, un bool qui vaut True et un str vide
        '''

        return [name,True,'']
        

    def events(self,event):
        '''
        fonction qui prend en paramètre un event pygame et qui renvoie une liste qui contient un str menu, un boll qui vaut False et un str vide
        '''
        click , posCursor = clicgauche(event)
        if click == True:
            for i in range(len(self.button)):
                g , v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                if g:   return v
        return self.view
    

    def eventEscape(self,event):
        '''
        fonction qui prend en paramètre un event pygame et qui renvoie False si l'un des deux bool vaut False sinon il renvoi True        
        '''
        return escape(event) and not self.exit

    def aff(self,window,lang):
        '''
        fonction qui affiche les 3 boutons definie lors de l'initialisation
        '''
        window.reload(500,500)
        if lang == "english":
            self.button = [Button(self.img,self.font,'Play'),Button(self.img2,self.font,'Option'),Button(self.img3,self.font,'Leave')]      
        else:
            self.button = [Button(self.img,self.font,'Jouer'),Button(self.img2,self.font,'Option'),Button(self.img3,self.font,'Quitter')]      
        self.logo.aff(window,200,50)
        for i in range(len(self.button)):
            self.button[i].aff(window,150,200+100*i)
