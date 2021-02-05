import pygame
from moteur.color import *


class Font(pygame.font.Font):


    def __init__(self,text,taille,font='Bold',color=black):
        self.text = text
        self.color = color
        super().__init__('assets/font/' + font + '.ttf',taille)

    def space_taken(self):
        return self.size()

    def aff(self,x,y,window):
        t =self.render(self.text,None,self.color)
        window.window.blit(t,(x,y))