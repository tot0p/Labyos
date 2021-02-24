import random
from moteur.fichier import Fichier
from moteur.text import Font
from moteur.color import *

class Load:

    def __init__(self):
        file = Fichier('donne/load.txt')
        self.contenu = file.lectureTable() #[ligne1,ligne2,ligne3] list de str
        self.font= [Font(9,'Thick',white),Font(17,'Barcode',white),Font(13,'Blocks',white),Font(10,'Bold',white),Font(14,'Future Narrow',white),Font(15,'Future Square',white),Font(26,'High Square',white),Font(16,'Mini Square',white),Font(9,'PressStart',white),Font(8,'Space',white)]
    def aff(self,window):
        
        window.reload(500,500)
        s=random.choice(self.contenu)
        s2 = random.choice(self.font)
        Issplit = False
        for i in s:
            if i == ';':
                Issplit = True
        if Issplit :
            Issplit = s.split(';')
            for i in range(len(Issplit)):
                t = s2.space_taken(Issplit[i])
                s2.aff(window,Issplit[i],(500-t[0])//2,(500-t[1])//2+t[1]*i)

        else:
            t = s2.space_taken(s)
            s2.aff(window,s,(500-t[0])//2,(500-t[1])//2)
            
       