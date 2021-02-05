import pygame
from moteur.color import *

pygame.font.init()

class Font(pygame.font.Font):


    def __init__(self,text,taille,font='Bold',color=black):
        self.text = text
        self.color = color
        super().__init__('assets/font/' + font + '.ttf',taille)

    def space_taken(self):
        '''
        return un tuple de l'espace que prend le texte
        '''
        return self.size(self.text)

    def aff(self,x:int,y:int,window):
        '''
        affiche le texte
        sur window de type Window
        avec comme cordonné au point haut gauche x et y
        '''
        t =self.render(self.text,None,self.color)
        window.window.blit(t,(x,y))