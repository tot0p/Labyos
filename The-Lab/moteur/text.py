import pygame
from moteur.color import *

class Text:

    def __init__(self,text,color=black,font='Bold'):
        self.text = text
        self.color = color
        self.font = font+'.ttf'