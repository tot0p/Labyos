from moteur.fichier import Fichier
from moteur.map import Map


class codeFile:

    def __init__(self,window,filename,player,view):
        file = Fichier(filename)
        self.contenu = file.lectureTable()
        self.player = player
        self.view = view
        self.initGame = []
        self.inGame = []
        self.endGameInLife = []
        self.endGameDead = []
        self.__load(window)

    def __load(self,window):

        self.map = Map(window,self.contenu.pop(0))
        self.contenu = ''.join(self.contenu).split('/') #   'initGame{spawn(0,4)}/inGame{wall(3,5):to:wall(3,6)}/endGameInLife{hist('test')}/endGameDead{}'
        print(self.contenu)
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
                    elif i == 1:
                        self.inGame.append(self.__keyword(t))
                    elif i == 2:
                        self.endGameInLife.append(self.__keyword(t))
                    elif i == 3:
                        self.endGameDead.append(self.__keyword(t))
        self.view.load_event(self.initGame,self.inGame,self.endGameInLife,self.endGameDead)
        

    def __keyword(self,t):
        print(t)
        t = t.split('(')
        print(t)
        if t[0] == 'spawn':
            return lambda : self.player.set_spawn(int(t[1])*50,int(t[2])*50)
        return
    def get_map(self):
        return self.map
            
        






