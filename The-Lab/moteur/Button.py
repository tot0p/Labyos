from moteur.Image import *
from moteur.text import *
class Button:


    def __init__(self,img,Font,text:str=''):
        self.rect = img.get_rect() # contient x , y du point au gauche et height et width la taille
        self.img = img #image du fond du bouton
        self.font = Font
        self.text = text
        self.afficher = False
        self.isClick = False

    def EventClic(self,xC,yC,function):
        '''
        Fonction qui permet de lancer une fonction en cliqaunt sur un bouton
        Prend en paramètre:
        xC= coordonnée du curseur en X
        xY= coordonnée du curseur en Y
        function est une fonction exécuter l'or d'un clic
        et renvoie False et None si le clic n'est pas dans le bouton ou True et le return de function si il existe
        '''
        X2= self.rect.x+ self.rect.width               
        Y2=self.rect.y+ self.rect.height
        if (xC >= self.rect.x and xC <= X2) : 
            if (yC >= self.rect.y and yC <= Y2):               
            #if self.rect.collidepoint(xC,yC):
                t =function()
                if t is not None:
                     return True , t
                return True, None
        return False , None
        

    def EventHover(self,xC,yC):
        #si curseur au dessus
        pass

    def aff(self,window,x,y):
        self.afficher=True
        self.img.aff(window,x,y)
        L=self.font.space_taken(self.text)
        if L[0] >= self.rect.width and L[1] >= self.rect.height:
             self.font.aff(window,self.text,x,y)
        elif L[0] < self.rect.width and L[1] < self.rect.height:
            t1=self.rect.width - L[0]
            t2=self.rect.height - L[1]
            self.font.aff(window,self.text,self.rect.x+(t1//2),self.rect.y+(t2//2))
        else:
            self.font.aff(window,self.text,x,y)