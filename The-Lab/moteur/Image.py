import pygame

class Image:

    def __init__(self,filename):
        self.filename = filename
        self.img = pygame.image.load(filename)

    def fondTransparant(self):
        self.img = self.img.convert_alpha()

    def resize(W,H):
        self.img = pygame.transform.scale(self.img,(W,H))

    def flip(X:bool,Y:bool):
        self.img = pygame.transform.flip(self.img,X,Y)

    def aff(window:Window,X:int,Y:int):
        window.blit(self.img,(X,Y))
