from moteur.mapV2 import Map
from moteur.fichier import Fichier


class Level:
    def __init__(self,window,filenameCode):
        self.code = []
        self.start = []
        self.run = []
        self.end = []
        self.window = window
        self.map = None
        self.file = Fichier(filenameCode)
        self.__load()

    def __load(self):
        if not self.file.existFile():
            return False , 'Le fichier code n\'existe pas '
        self.code = self.file.lectureTable() #lis le fichier code
        t = Fichier(self.code[0])
        if not t.existFile():
            return False , 'La première ligne du fichier code n\'est pas bonne'
        self.map = Map(self.window,self.code.pop(0)) #lis le fichier represantant le tilset
        for i in range(len(self.code)):
            if self.code[i] == 'start':
                nIn = self.__loadStart(i)
                


    def __loadStart(self,n):
        for i in range(n,len(self.code)):
            if self.code[i] == '':
                return i
            self.start.append(self.code[i])
            


