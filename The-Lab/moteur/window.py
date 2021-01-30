import pygame
from moteur.color import *

class Window:

    def __init__(self,W,H,name,icon,bg_color=black,fullscreen=0):
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
        self.W = int(W)
        self.H = int(H)
        self.window = self.display.set_mode((int(W),int(H)),fullscreen)
        self.window.set_caption(self.name)
        self.window.fill(bg_color)
        self.update()

    def get_size(self):
        return (self.W , self.H)

    def update(self):
        self.display.flip()
        