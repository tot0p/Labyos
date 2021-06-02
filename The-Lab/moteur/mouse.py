import pygame


def get_posMouse():
    '''
    return un tuple des position du curseur
    '''
    return pygame.mouse.get_pos()

def get_PressedMouse():
    '''
    renvoie un tuple de 5 bool, chaque bool represante un bouton souris ,qui sont True si le bouton est préssé et False sinon
    '''
    return pygame.mouse.get_pressed(5)


def Mouse_on_window():
    '''
    renvoie True si la souris est sur la fenetre sinon False
    '''
    return pygame.mouse.get_focused()