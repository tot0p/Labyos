#import

from moteur.fichier import Fichier

'''
initialisation des données essentiel du jeu
'''


def init():
    confFile = Fichier('donne/config.txt')
    if not confFile.existFile():
        confFile.createFile('')
    conf = confFile.variableFileLecture()