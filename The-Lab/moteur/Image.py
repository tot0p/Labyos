import pygame

class Image:
    '''
    Objet contenant une image
    '''

    def __init__(self,filename):
        self.filename = filename
        self.img = pygame.image.load(filename)
        self.rect = self.img.get_rect()

    def fondTransparant(self):
        '''
        permet de rendre le fond transparent d'une image
        '''
        self.img = self.img.convert_alpha()

    def resize(self,W,H):
        '''
        redimension l'image avc W en int qui est la largeur et H en int qui est la hauteur
        '''
        self.img = pygame.transform.scale(self.img,(W,H))
        self.rect.width = W
        self.rect.height = H

    def flip(self,X:bool,Y:bool):
        '''
        permet de retourner l'image sur x , y ou x et y
        '''
        self.img = pygame.transform.flip(self.img,X,Y)

    def get_rect(self):
        '''
        permet de recuperer self.rect
        '''
        return self.rect

    def get_image(self):
        '''
        permet de recuperer self.img
        '''
        return self.img

    def aff(self,window,X:int,Y:int):
        '''
        permet d'afficher l'image
        sur window : Window
        en coordonné X,Y
        '''
        self.rect.x = X
        self.rect.y = Y
        window.window.blit(self.img,(X,Y))