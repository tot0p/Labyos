import pygame
from moteur.mouse import *

def clicgauche(event):
    '''
    prend en entré un event de pygame et vérifie si c'est un clic gauche et return True et les possition du clic si event est un clic sinon False et None
    '''
    if event.type == pygame.MOUSEBUTTONDOWN and get_PressedMouse()[0] :
        return True , get_posMouse()
    return False , None

def keypressed(event):
    '''
    prend en entré un event de pygame et vérifie si c un touche qui est pressé et renvoy laquelle c'est
    sinon return None
    '''
    pressed = None
    if event.type == pygame.KEYDOWN:
        pressed = (event.key)
    return pressed


def get_event():
    '''
    return les events de pygame
    '''
    return pygame.event.get()
        
def escape(event):
    '''
    prend event en parramètre qui est un event des events de pygame 
    et vérifi si le buton croix est présse et si c'est le cas il return 0 sinon 1
    '''
    if event.type == pygame.QUIT :
        return 0
    return 1

def escapeandkey(event,key=pygame.K_ESCAPE):
    '''
    prend event en parramètre qui est un event des events de pygame et key qui est une touche
    et vérifi si le buton croix est présse ou si la key est préssé et si c'est le cas il return 0 sinon 1
    '''
    if event.type == pygame.QUIT:
        return 0
    elif event.type == pygame.KEYDOWN and event.key == key:
        return 0
    return 1


def stop():
    '''
    quit pygame
    '''
    pygame.quit()