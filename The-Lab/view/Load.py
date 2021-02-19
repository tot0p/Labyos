import random
from moteur.fichier import Fichier
from moteur.text import Font
from moteur.color import *

class Load:

    def __init__(self):
        file = Fichier('donne/load.txt')
        self.contenu = file.lectureTable() #[ligne1,ligne2,ligne3] list de str
        self.font= [Font(8,'Thick',salmon),Font(8,'Pixel',salmon),Font(8,'Thick',salmon),Font(8,'Rocket',salmon)]
        #self.color = [black,salmon]
        #self.font_family = ['Thick','Pixel']
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

        #s2 = random.choice(self.color)
        #s3 = random.choice(self.font_family)
        #font = Font(40,s3,s2)
            t = s2.space_taken(s)
            s2.aff(window,s,(500-t[0])//2,(500-t[1])//2)
            
       