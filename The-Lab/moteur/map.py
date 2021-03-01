import pygame
from moteur.Image import Image
from moteur.fichier import *
from moteur.loadtiletable import load_tile_table

class Map(pygame.sprite.Group):

    def __init__(self,window,filename):
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


    def __load(self,filename):
        f = Fichier(filename)
        if not f.existFile():
            print("Erreur le ficier n'existe pas ou incompatible--")
            return
        self.encodageMap = f.lectureTable()
        for i in range(len(self.encodageMap)):
            self.encodageMap[i] = self.encodageMap[i].split(",")
        self.__mapBuild()

    def __mapBuild(self):
        for i in range(len(self.encodageMap)):
            for k in range(len(self.encodageMap[0])):
                x,y = 0+50*k,0+50*i
                if self.encodageMap[i][k] == 'hole':
                    tile = Hole(x,y)
                elif self.encodageMap[i][k] == 'fire':
                    tile = Fire(x,y)
                elif self.encodageMap[i][k] == 'end':
                    tile = arrive(x,y)
                elif self.encodageMap[i][k] != 'None':
                    tile = Wall(int(self.encodageMap[i][k]),x,y)
                    self.listofwall.append(tile)
                else:
                    tile = Sol(x,y)
                self.listoftiles[i].append(tile)
                self.add(tile)

    def set_fog(self,bool):
        self.afffogofwar = bool
        

    def aff(self,window,playerRect):
        self.draw(window.window)
        if self.afffogofwar:
            self.fogofwar.aff(playerRect)

        


class Wall(pygame.sprite.Sprite):
    def __init__(self,name,x,y):
        super().__init__()
        tile_table = load_tile_table('assets/img/map/tileset.png',36,36) # a changer
        self.image = pygame.transform.scale(tile_table[name],(50,50)) # a changer utiliser l'objet Image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect
    def get_law(self):
        return False

    def aff(self,window):
        window.aff(self.image,self.rect.x,self.rect.y)
        


class Sol(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = Image('assets/img/map/sol.png')
        image.resize(50,50)
        self.image = image.get_imgFormpygame()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect

    def get_law(self):
        return True

    def get_event(self):
        return None
    
    def aff(self,window):
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
        return self.rect

    def get_law(self):
        return True

    def get_event(self):
        return 'mort'

    def aff(self,window):
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
        return self.rect

    def get_law(self):
        return True

    def get_event(self):
        return 'fin'

    def aff(self,window):
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
        return self.rect

    def get_law(self):
        return True

    def get_event(self):
        return 'mort'

    def aff(self,window):
        window.aff(self.image,self.rect.x,self.rect.y)

class FogOfWar:
    def __init__(self,window,dif=0):
        super().__init__()
        self.listOfFog = []
        self.window = window
        for y in range(self.window.H//50):
            self.listOfFog.append([])
        self.__load(dif)

    def __load(self,dif):
        for y in range(len(self.listOfFog)):
            for x in range(len(self.listOfFog)) :
                self.listOfFog[y].append(Fog(x*50,y*50,dif))
        
    def set_dif(self,dif):
        for y in range(len(self.listOfFog)):
            for x in range(len(self.listOfFog)) :
                self.listOfFog[y][x].change_img(dif)

    def aff(self,rectPlayer):
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
        super().__init__()
        self.image = Image('assets/img/map/noirTrans.png')
        self.image.split(36,36,n)
        self.image.resize_all_tile(50,50)
        print(len(self.image.tile_table))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_xy(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def change_img(self,n):
        self.image.changeImagewithtiletable(n)

    def aff(self,window):
        self.image.aff(window,self.rect.x,self.rect.y)

