from moteur.color import *

class Window:

    def __init__(self,W,H,name,icon,bg_color=black,fullscreen=0):
        '''
        initialisation de la fenetre graphique
        W(int) , H(int) represante la taille la fenetre
        name(str) represante le nom de la fenetre
        icon(Image (moteur.Image)) est l'icon de la fenetre graphique
        bg_color(tuple(r,g,b)) optionel de base Noir
        fullscreen(bool) optionel de base False
        '''
        self.name = name
        self.display  = pygame.display
        self.W = int(W)
        self.H = int(H)
        self.fullscreen = fullscreen
        if fullscreen:
            self.window = self.display.set_mode((int(W),int(H)),pygame.FULLSCREEN)
        else:
            self.window = self.display.set_mode((int(W),int(H)))
        self.display.set_caption(self.name)
        self.display.set_icon(icon.img)
        self.window.fill(bg_color)
        self.sprites = pygame.sprite.Group()
    
    def reload(self,W,H,bg_color=black):
        '''
        permet de recharger la fenetre
        W(int) , H(int) represante la taille la fenetre
        bg_color(tuple(r,g,b)) optionel
        fullscreen(bool) optionel
        '''
        self.W = int(W)
        self.H = int(H)
        if self.fullscreen:
            self.window = self.display.set_mode((int(W),int(H)),pygame.FULLSCREEN)
        else:
            self.window = self.display.set_mode((int(W),int(H)))
        self.window.fill(bg_color)
        self.update()

    def set_fullscreen(self,fullscreen):
        """
        permet de définir le fullscreen
        """
        self.fullscreen = fullscreen
        self.reload(self.W,self.H)

    def get_fullscreen(self)->bool:
        '''
        permet de récuperer si c en fullscreen
        '''
        return self.fullscreen

    def get_size(self)-> tuple:
        '''
        return un tuple de la taille de la fenetre
        '''
        return (self.W , self.H)

    def update(self):
        '''
        permet d'afficher les nouveaux elements sur l'ecran
        '''
        self.display.flip()
        
    def aff(self,elem,x,y):
        '''
        permet d'afficher des elements sur la window
        '''
        self.window.blit(elem,(x,y))