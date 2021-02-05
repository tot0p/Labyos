#import

from moteur.fichier import Fichier

'''
initialisation des données essentiel du jeu
'''


def fichierconf():
    confFile = Fichier('donne/config.txt')
    if not confFile.existFile():
        confFile.createFile('')
    conf = confFile.variableFileLecture()
    if list(conf.keys()) != ['textplayer']:
        confFile.variableFileWrite({'textplayer':'default'})

def fichiertouche():
    toucheFile = Fichier('donne/touche.txt')
    if not toucheFile.existFile():
        toucheFile.createFile('')
    touche = toucheFile.variableFileLecture()
    if list(conf.keys()) != ['']:
        toucheFile.variableFileWrite()
        touche = {}


def init():
    '''
    verif des fichiers
    '''
    conf  = fichierconf()