from moteur.Button import Button
from moteur.Image import Image
from moteur.text import Font
from moteur.color import *

class naration:
    def __init__(self):
        self.img = Image("")
        self.font = Font(40)
        self.button = Button(self.img,self.font)
        self.afficher=False
    
    def aff(self,window,text):
        self.img.aff(window,50,50)
        self.font.aff(window,text,50,50)

    def affUpdate(self,window):
        pass
