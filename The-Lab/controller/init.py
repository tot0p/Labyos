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

def init():
    '''
    verif des fichiers
    '''
    conf  = fichierconf()