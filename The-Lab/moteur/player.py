import pygame
from moteur.Image import Image
from moteur.time import Chrono
from moteur.event import keypressed
from moteur.map import Wall

#Thomas Lemaitre

class Player:

    def __init__(self,imgbase:str,imgrunDown:str):
        '''
        initialise le player avec imgbase : chemin img et imgrunDown  chemin img
        '''
        super().__init__()
        #move
        self.move = False
        self.nRun = 0
        self.left = False
        self.up = False
        self.velocity = 2
        self.imgRun = Image(imgrunDown)
        self.imgRun.split(36,36,0)
        self.imgRun.resize_all_tile(40,40)
        #chrono
        self.chrono = Chrono()
        #imgbase
        self.imgbase = Image(imgbase)
        self.imgbase.split(36,36,0)
        self.imgbase.resize_all_tile(40,40)
        self.nIDLE = 0
        self.rect= self.imgbase.get_rect()
        #control
        self.av = pygame.K_z
        self.re = pygame.K_s
        self.le = pygame.K_q
        self.ri = pygame.K_d
        self.keys = {self.av : False,self.re : False,self.le:False,self.ri:False}

    def def_map(self,map):
        '''
        return la map charger a partir de code.txt
        '''
        self.map = map
  
    def set_spawn(self,x,y):
        '''
        défini le spawn du joueur
        '''
        self.rect.x = x
        self.rect.y = y


    def move_on_axe_x(self,add:bool = True):
        '''
        permet de se deplace sur l'axe x si add == True on ajoute sinon on supprime
        '''
        if add:
            self.rect.x += self.velocity
            if self.check_collision():
                self.rect.x -= self.velocity
            self.left = False ; self.up = False;self.move = True
        else:
            self.rect.x -= self.velocity
            if self.check_collision():
                self.rect.x += self.velocity
            self.left = True; self.up = False;self.move = True

    def move_on_axe_y(self,add:bool = True):
        '''
        permet de se deplace sur l'axe y si add == True on ajoute sinon on supprime
        '''
        if add:
            self.rect.y += self.velocity
            if self.check_collision():
                self.rect.y -= self.velocity
            self.left = False ; self.up = False;self.move = True
        else:
            self.rect.y -= self.velocity
            if self.check_collision():
                self.rect.y += self.velocity
            self.up =True ; self.left = False;self.move = True



    def affUpdate(self,window):
        '''
        permet de mettre a jour l'affichage du player
        '''
        if not self.move:
            if self.chrono.get_val()%10 == 0:
                self.nRun = 0
                self.nIDLE +=1
                if self.nIDLE > 7:
                    self.nIDLE = 0
                self.imgbase.changeImagewithtiletable(self.nIDLE)
            self.imgbase.aff(window,self.rect.x,self.rect.y)
        if self.move:
            if self.chrono.get_val()%5 == 0:
                self.nIDLE = 0
                self.nRun += 1
                if self.nRun > 7:
                    self.nRun = 0
                self.imgRun.changeImagewithtiletable(self.nRun)
            self.imgRun.aff(window,self.rect.x,self.rect.y)


    def check_collision(self):
        '''
        return True si le player a un colision avec un mur
        '''
        return self.rect.collidelistall(self.map.listofwall)
            
            
    
    def inter(self):
        '''
        permet de recuperer les eventes sur les sol ou est le player
        '''
        xhg = (self.rect.x // 50)
        yhg = (self.rect.y // 50)
        xhd = ((self.rect.x + self.rect.width) // 50) 
        yhd = (self.rect.y // 50)
        xbg = (self.rect.x // 50)
        ybg = ((self.rect.y + self.rect.height) // 50)
        xbd = ((self.rect.x + self.rect.width) // 50)
        ybd = (self.rect.y // 50)
        hg = self.map.listoftiles[yhg][xhg].get_event()
        hd = None
        bg = None
        bd = None
        if self.map.listoftiles[yhd][xhd].get_law():
            hd = self.map.listoftiles[yhd][xhd].get_event()      
        if self.map.listoftiles[ybg][xbg].get_law():
            bg = self.map.listoftiles[ybg][xbg].get_event()
        if self.map.listoftiles[ybd][xbd].get_law():
            bd = self.map.listoftiles[ybd][xbd].get_event()
        if hg == "mort" or hd == "mort" or bg == "mort" or bd == "mort" :
            return "mort"
        elif hg == "fin" or hd == "fin" or bg == "fin" or bd == "fin":
            return "fin"
        #elif hg == "tp" or hd == "tp" or bg == "tp" or bd == "tp":
        #    return "tp"
        elif hg == None or hd == None or bg == None or bd == None:
            return None

    def getTpfile(self):
        '''
        franchement la flemme pour ça lit c pas trop compliqué ^^
        '''
        xhg = (self.rect.x // 50)
        yhg = (self.rect.y // 50)
        xhd = ((self.rect.x + self.rect.width) // 50) 
        yhd = (self.rect.y // 50)
        xbg = (self.rect.x // 50)
        ybg = ((self.rect.y + self.rect.height) // 50)
        xbd = ((self.rect.x + self.rect.width) // 50)
        ybd = (self.rect.y // 50)
        hg = self.map.listoftiles[yhg][xhg].get_event()
        hd = None
        bg = None
        bd = None
        if self.map.listoftiles[yhd][xhd].get_law():
            hd = self.map.listoftiles[yhd][xhd].get_event()      
        if self.map.listoftiles[ybg][xbg].get_law():
            bg = self.map.listoftiles[ybg][xbg].get_event()
        if self.map.listoftiles[ybd][xbd].get_law():
            bd = self.map.listoftiles[ybd][xbd].get_event()
        if hg == "tp":
            return (xhg , yhg)
        elif hd == "tp":
            return (xhd , yhd)
        elif bg == "tp":
            return (xbg , ybg)
        elif bd == "tp":
            return (xbd , ybd)

    def get_rect(self):
        '''
        permet de recuperer le rect du player
        '''
        return self.rect




    def aff(self,window):
        """
        affiche le player sur la window de type window
        """
        self.imgbase.aff(window,self.rect.x,self.rect.y)
