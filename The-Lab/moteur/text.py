import pygame
from moteur.color import *

pygame.font.init()

class Font(pygame.font.Font):
    '''
    cree une font utilisable pour afficher du texte
    '''


    def __init__(self,taille,font='Bold',color=black):
        self.color = color
        super().__init__('assets/font/' + font + '.ttf',taille)

    def space_taken(self,text):
        '''
        return un tuple de l'espace que prend le texte
        '''
        return self.size(text)

    def aff(self,window,text,x:int,y:int):
        '''
        affiche le texte
        sur window de type Window
        avec comme cordonné au point haut gauche x et y
        '''
        window.aff(self.render(text,0,self.color),x,y)