import pygame

class Image:
    '''
    Objet contenant une image
    '''

    def __init__(self,filename):
        try :
            self.img = pygame.image.load(filename)
            self.rect = self.img.get_rect()
        except : 
            self.img = pygame.image.load('assets/img/texture-none.png')
            self.rect = self.img.get_rect()
        self.tile_table = []

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

    def split(self,width,height,n):
        '''
        permet de load un tile table avec width et height la taille des morceaux et n l'image de numero 
        '''
        self.tile_table = []
        for tile_x in range(0, self.rect.width//width):
            for tile_y in range(0,self.rect.height//height):
                rect = (tile_x*width, tile_y*height, width, height)
                self.tile_table.append(self.img.subsurface(rect))
        self.img = self.tile_table[n]

    def changeImagewithtiletable(self,n):
        self.img = self.tile_table[n]

    def resize_all_tile(self,W,H):
        self.resize(W,H)
        for i in range(len(self.tile_table)):
            self.tile_table[i] = pygame.transform.scale(self.tile_table[i],(W,H))

    def flip_all_tile(self,X:bool,Y:bool):
        self.flip(X,Y)
        for i in range(len(self.tile_table)):
            self.tile_table[i] = pygame.transform.flip(self.tile_table[i],X,Y)



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

    def get_imgFormpygame(self):
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
        window.aff(self.img,X,Y)