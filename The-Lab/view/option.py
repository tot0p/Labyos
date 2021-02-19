from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.fichier import *

#g{avancer : z,reculer : s,aller a gauche : q,aller a droite : d}
#g['avancer'] 
class Option:
    def __init__(self):
        touche = Fichier('donne/touche.txt')
        self.touche = touche.variableFileLecture()

