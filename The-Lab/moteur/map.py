import pygame
from moteur.Image import Image
from moteur.fichier import *
from moteur.loadtiletable import load_tile_table

class Map(pygame.sprite.Group):

    def __init__(self,window,filename):
        '''
        initialise toute les variables necessaire a map
        '''
        super().__init__()
        self.window = window
        self.listoftiles = []
        self.encodageMap = []
        for y in range(self.window.H//50):
            self.listoftiles.append([])
        self.listofwall = []
        self.fogofwar = FogOfWar(window)
        self.afffogofwar = True
        self.__load(filename)


    def reload(self,cord):
        '''
        permet de recharger la map
        '''
        filename = self.encodageMap[cord[1]][cord[0]].get_filename()
        self.encodageMap[cord[1]][cord[0]].tp()
        self.listoftiles = []
        self.encodageMap = []
        for y in range(self.window.H//50):
            self.listoftiles.append([])
        self.listofwall = []
        self.fogofwar = FogOfWar(window)
        self.afffogofwar = True
        self.__load(filename)

    def __load(self,filename):
        '''
        charge le fichier contenant l'encodage de la map
        '''
        f = Fichier(filename)
        if not f.existFile():
            print("Erreur le ficier n'existe pas ou incompatible")
            return
        self.encodageMap = f.lectureTable()
        for i in range(len(self.encodageMap)):
            self.encodageMap[i] = self.encodageMap[i].split(",")
        self.__mapBuild()

    def __mapBuild(self):
        '''
        permet de crée la map
        '''
        for i in range(len(self.encodageMap)):
            for k in range(len(self.encodageMap[0])):
                x,y = 0+50*k,0+50*i
                if self.encodageMap[i][k] == 'hole':
                    tile = Hole(x,y)
                elif self.encodageMap[i][k] == 'fire':
                    tile = Fire(x,y)
                elif self.encodageMap[i][k] == 'end':
                    tile = arrive(x,y)
                elif self.encodageMap[i][k] == 'fakehole':
                    tile = FakeHole(x,y)
                elif self.encodageMap[i][k] != 'None':
                    tile = Wall(int(self.encodageMap[i][k]),x,y)
                    self.listofwall.append(tile)
                else:
                    tile = Sol(x,y)
                self.listoftiles[i].append(tile)
                self.add(tile)

    def set_tp(self,x,y,filename,player,spawnx,spawny):
        '''
        (pour un ajout)
        permet de tp le player
        '''
        tile = TP(x,y,filename,player,spawnx,spawny)
        self.encodageMap[y//50][x//50] = tile
        self.add(tile)

    def set_fog(self,bool):
        '''
        permet d'activé où desactivé le brouillard de guerre
        '''
        self.afffogofwar = bool
        

    def aff(self,window,playerRect):
        '''
        permet d'afficher la map 
        et prend en parametre window de type window et le rect du player
        '''
        self.draw(window.window)
        if self.afffogofwar:
            self.fogofwar.aff(playerRect)

        
class TP(pygame.sprite.Sprite):

    '''
    (nouvel object actuellement pas fonctionnel)
    '''
    def __init__(self,x,y,filename,player,spawnx,spawny):
        super().__init__()
        image = Image('assets/img/texture-none.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(x,y)
        self.filename = filename
        self.player = player
        self.spawnx , self.spawny = spawnx,spawny


    def get_filename(self):
        return self.filename

    def tp(self):
        self.player.set_spawn(self.spawnx,self.spawny)

    def get_rect(self):
        '''
        return le rect du sol
        '''
        return self.rect

    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return True

    def get_event(self):
        '''
        return l'event pour le player
        '''
        return 'tp'
    
    def aff(self,window):
        '''
        affiche l'objet
        '''
        window.aff(self.image,self.rect.x,self.rect.y)

class Wall(pygame.sprite.Sprite):
    def __init__(self,name,x,y):
        '''
        créé le wall de texture name et de coordoné x , y
        '''
        super().__init__()
        tile_table = load_tile_table('assets/img/map/tileset.png',36,36) # a changer
        self.image = pygame.transform.scale(tile_table[name],(50,50)) # a changer utiliser l'objet Image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        '''
        return le rect du wall
        '''
        return self.rect
    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return False

    def aff(self,window):
        '''
        permet d'afficher le wall
        '''
        window.aff(self.image,self.rect.x,self.rect.y)
        


class Sol(pygame.sprite.Sprite):
    def __init__(self,x,y):
        '''
        créé un sol de coordonné x, y
        '''
        super().__init__()
        image = Image('assets/img/map/sol.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        '''
        return le rect du sol
        '''
        return self.rect

    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return True

    def get_event(self):
        '''
        return l'event pour le player
        '''
        return None
    
    def aff(self,window):
        '''
        affiche l'objet
        '''
        window.aff(self.image,self.rect.x,self.rect.y)

class Hole(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = Image('assets/img/map/hole.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        '''
        return le rect de l'objet
        '''
        return self.rect

    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return True

    def get_event(self):
        '''
        return l'event pour le player
        '''
        return 'mort'

    def aff(self,window):
        '''
        affiche l'objet
        '''
        window.aff(self.image,self.rect.x,self.rect.y)
   
class FakeHole(pygame.sprite.Sprite):
    '''
    (nouveau) mais pas encore de texture
    '''
    def __init__(self,x,y):
        super().__init__()
        image = Image('assets/img/map/holdfse.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        '''
        return le rect de l'objet
        '''
        return self.rect

    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return True

    def get_event(self):
        '''
        return l'event pour le player
        '''
        return None

    def aff(self,window):
        '''
        affiche l'objet
        '''
        window.aff(self.image,self.rect.x,self.rect.y)

class arrive(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = Image('assets/img/map/solfin.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        '''
        return le rect de l'objet
        '''
        return self.rect

    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return True

    def get_event(self):
        '''
        return l'event pour le player
        '''
        return 'fin'

    def aff(self,window):
        '''
        affiche l'objet
        '''
        window.aff(self.image,self.rect.x,self.rect.y)

class Fire(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = Image('assets/img/map/feu.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        '''
        return le rect de l'objet
        '''
        return self.rect

    def get_law(self):
        '''
        return si le joueur a droit être là
        '''
        return True

    def get_event(self):
        '''
        return l'event pour le player
        '''
        return 'mort'

    def aff(self,window):
        '''
        affiche l'objet
        '''
        window.aff(self.image,self.rect.x,self.rect.y)

class FogOfWar:
    def __init__(self,window,dif=0):
        '''
        initialise le brouillard de guerre avec window de type window et dif la transparence du broullard de guerre dif < ou = a 2
        '''
        super().__init__()
        self.listOfFog = []
        self.window = window
        for y in range(self.window.H//50):
            self.listOfFog.append([])
        self.__load(dif)

    def __load(self,dif):
        '''
        permet de cree la list de list de Frog
        '''
        for y in range(len(self.listOfFog)):
            for x in range(len(self.listOfFog)) :
                self.listOfFog[y].append(Fog(x*50,y*50,dif))
        
    def set_dif(self,dif):
        '''
        permet de definir la transparence dif = ou < a 2
        '''
        for y in range(len(self.listOfFog)):
            for x in range(len(self.listOfFog)) :
                self.listOfFog[y][x].change_img(dif)

    def aff(self,rectPlayer):
        '''
        affiche l'objet et prend rectPlayer pour bien afficher le brouillard
        '''
        xP = rectPlayer.x//50
        yP = rectPlayer.y//50
        for y in range(len(self.listOfFog)):
            for x in range(len(self.listOfFog[0])):
                if xP != 0 and yP !=0 and xP != 9 and yP != 9:
                    if (x != xP or y != yP)and(x!= xP+1 or y!= yP)and(x!= xP-1 or y!= yP)and(x!= xP or y!= yP-1)and(x!= xP or y!= yP+1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP != 9 and yP !=0 and yP!=9:
                    if (x != xP or y != yP)and(x!= xP+1 or y!= yP)and(x!= xP or y!= yP-1)and(x!= xP or y!= yP+1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP != 0 and yP !=0 and yP!=9:
                    if (x != xP or y != yP)and(x!= xP-1 or y!= yP)and(x!= xP or y!= yP-1)and(x!= xP or y!= yP+1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP != 0 and xP != 9 and yP != 9:
                    if (x != xP or y != yP)and(x!= xP+1 or y!= yP)and(x!= xP-1 or y!= yP)and(x!= xP or y!= yP+1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP != 0 and xP != 9 and yP != 0:
                    if (x != xP or y != yP)and(x!= xP+1 or y!= yP)and(x!= xP-1 or y!= yP)and(x!= xP or y!= yP-1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP == 0 and yP == 0:
                    if (x != xP or y != yP)and(x!= xP+1 or y!= yP)and(x!= xP or y!= yP+1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP == 9 and yP == 9:
                    if (x != xP or y != yP)and(x!= xP-1 or y!= yP)and(x!= xP or y!= yP-1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP == 0 and yP == 9:
                    if (x != xP or y != yP)and(x!= xP+1 or y!= yP)and(x!= xP or y!= yP-1):
                        self.listOfFog[y][x].aff(self.window)
                elif xP == 9 and yP == 0:
                    if (x != xP or y != yP)and(x!= xP-1 or y!= yP)and(x!= xP or y!= yP+1):
                        self.listOfFog[y][x].aff(self.window)






class Fog:

    def __init__(self,x,y,n):
        '''
        est un morceau de brouillard avec x , y de coordoné et de transparence n = < 2
        '''
        super().__init__()
        self.image = Image('assets/img/map/noirTrans.png')
        self.image.split(36,36,n)
        self.image.resize_all_tile(50,50)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_xy(self,x,y):
        '''
        permet de changer les coord de Fog
        '''
        self.rect.x = x
        self.rect.y = y

    def change_img(self,n):
        '''
        permet de changer l'image de Fog
        '''
        self.image.changeImagewithtiletable(n)

    def aff(self,window):
        '''
        affiche l'objet
        '''
        self.image.aff(window,self.rect.x,self.rect.y)

