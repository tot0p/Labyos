# -*- coding: utf-8 -*-

#import
import graphics
import pygame
from pygame.locals import *

pygame.init()


#event
def eventGame():
    pass

def eventMenu():
    for event in pygame.event.get():
        if escape(event) == 0:
            return 0
    return 1

def escape(event):
    if event.type == pygame.QUIT :
        return 0
    if event.type == KEYDOWN and event.key == K_ESCAPE :
        return 0
    return 1


def quit():
    pygame.quit()