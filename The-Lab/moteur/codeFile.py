from moteur.fichier import Fichier
from moteur.map import Map
from moteur.Senario import Naration

class codeFile:

    def __init__(self,window,filename,player,view):
        '''
        initialise la class code file qui permet de lire le fichier code du jeu
        prend window de type window
        filename est un str 
        player est de type player
        view est la view du jeu ou il faut load les events
        '''
        file = Fichier(filename)
        self.contenu = file.lectureTable()
        self.player = player
        self.view = view
        self.initGame = []
        #self.inGame = []
        self.endGameInLife = []
        self.endGameDead = []
        self.__load(window)

    def __load(self,window):
        '''
        methode privée qui sert a chargé la map
        prend en parrametre window de type Window
        '''

        self.map = Map(window,self.contenu.pop(0))
        self.contenu = ''.join(self.contenu).split('/') #   'initGame{spawn(0,4)}/inGame{wall(3,5):to:wall(3,6)}/endGameInLife{hist('test')}/endGameDead{}'
        for i in range(len(self.contenu)):
            self.contenu[i] = self.contenu[i].split('{')
            self.contenu[i].pop(0)
            self.contenu[i] = self.contenu[i][0].split('}')[0]
            self.contenu[i] = self.contenu[i].split(';')
            for y in range(len(self.contenu[i])):
                t = self.contenu[i][y]
                if t != '':
                    if i == 0:
                        self.initGame.append(self.__keyword(t))
                    #elif i == 1:
                        #self.inGame.append(self.__keyword(t))
                    elif i == 1:
                        self.endGameInLife.append(self.__keyword(t))
                    elif i == 2:
                        self.endGameDead.append(self.__keyword(t))
        self.view.load_event(self.initGame,self.endGameInLife,self.endGameDead)
        

    def __keyword(self,t):
        '''
        permet de charger les fonction correspondant au mot clé du fichier code
        '''
        t = t.split('(')
        print(t)
        if t[0] == 'spawn':
            return lambda : self.player.set_spawn(int(t[1])*50,int(t[2])*50)
        elif t[0] == 'set_fog':
            return lambda : self.map.set_fog(bool(t[1]))
        elif t[0] == 'diff_fog':
            return lambda : self.map.fogofwar.set_dif(int(t[1]))
        elif t[0] == 'hist':
            return lambda : print(t[1])
        return lambda:print('error')
    def get_map(self):
        '''
        permet de recuperer la map
        '''
        return self.map
            
        






