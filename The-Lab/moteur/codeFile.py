from moteur.fichier import Fichier
from moteur.map import Map


class codeFile:

    def __init__(self,window,filename):
        file = Fichier(filename)
        self.contenu = file.lectureTable()
        self.initGame = []
        self.inGame = []
        self.endGameInLife = []
        self.endGameDead = []
        self.__load(window)

    def __load(self,window):

        filenameMap=self.contenu.pop(0)
        self.contenu = ''.join(self.contenu).split('/') #   'initGame{spawn(0,4)}/inGame{wall(3,5):to:wall(3,6)}/endGameInLife{hist('test')}/endGameDead{}'
        print(self.contenu)
        for i in range(len(self.contenu)):
            self.contenu[i] = self.contenu[i].split('{')
            self.contenu[i].pop(0)
            self.contenu[i] = self.contenu[i][0].split('}')[0]
            self.contenu[i] = self.contenu[i].split(';')
            for y in range(len(self.contenu[i])):
                t = self.contenu[i][y]
                self.__keyword(t)
        print(self.contenu)

    def __keyword(self,t):
        print(t)
        t = t.split('(')
        print(t)
        if t[0] == 'spawn':
            
        



        return 'g'
        #return Map(window,filenameMap)



