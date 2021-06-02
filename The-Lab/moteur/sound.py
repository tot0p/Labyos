import pygame


pygame.mixer.init()


def load_music(F) :
    """
    F est une chaîne de caractères contenant le nom du fichier audio.
    Charge la musique F mais ne la joue pas.
    Si une musique était déjà chargée, cela la stoppe si elle etait jouée.
    Utiliser de préférence des .wav
    """
    pygame.mixer.music.load(F)


def play_music(loop=0) :
    """
    Lance la musique. Si la musique était déjà jouée, elle reprend au début
    L'argument optionnel loop prend les valeurs 0 ou 1.
    Si loop vaut 1, alors la musique est jouée en boucle.
    """
    if loop == 1:
        pygame.mixer.music.play(loops=-1)
    else:
        pygame.mixer.music.play()