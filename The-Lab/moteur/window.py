import pygame
from moteur.color import *

class Window:

    def __init__(self,W,H,name,icon,bg_color=black,fullscreen=0):
        '''
        initialisation de la fenetre graphique
        W(int) , H(int) represante la taille la fenetre
        name(str) represante le nom de la fenetre
        icon(Image (moteur.Image)) est l'icon de la fenetre graphique
        bg_color(tuple(r,g,b)) optionel
        fullscreen(bool) optionel
        '''
        self.name = name
        self.display  = pygame.display
        self.W = int(W)
        self.H = int(H)
        self.window = self.display.set_mode((int(W),int(H)),fullscreen)
        self.display.set_caption(self.name)
        self.display.set_icon(icon.img)
        self.window.fill(bg_color)
        self.update()
    
    def reload(self,W,H,bg_color=black,fullscreen=0):
        '''
        permet de recharger la fenetre
        W(int) , H(int) represante la taille la fenetre
        bg_color(tuple(r,g,b)) optionel
        fullscreen(bool) optionel
        '''
        self.W = int(W)
        self.H = int(H)
        self.window = self.display.set_mode((int(W),int(H)),fullscreen)
        self.window.set_caption(self.name)
        self.window.fill(bg_color)
        self.update()

    def set_fullscreen(self):
        '''
        Mais en fullscreen ou en fenetre si deja en fullscreen
        '''
        self.display.toggle_fullscreen()

    def get_size(self):
        '''
        return un tuple de la taille de la fenetre
        '''
        return (self.W , self.H)

    def update(self):
        '''
        permet d'afficher les nouveaux elements sur l'ecran
        '''
        self.display.flip()
        