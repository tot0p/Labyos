import pygame
from moteur.mouse import *

def clicgauche(event):
    if event.type == pygame.MOUSEBUTTONDOWN and get_PressedMouse()[0] :
        return True , get_posMouse()
    return False , None

def keypressed(event):
    pressed = []
    if event.type == pygame.KEYDOWN:
        pressed.append(event.key)
    return pressed


def get_event():
    return pygame.event.get()
        
def escape(event):
    if event.type == pygame.QUIT :
        return 0
    return 1

def escapeandkey(event,key=pygame.K_ESCAPE):
    if event.type == pygame.QUIT:
        return 0
    elif event.type == pygame.KEYDOWN and event.key == key:
        return 0
    return 1

def get_click(event):
    pass

def stop():
    pygame.quit()