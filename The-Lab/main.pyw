# -*- coding: utf-8 -*-

#import
from moteur.window import Window
from moteur.Image import Image
from moteur.event import *
from moteur.time import *
from moteur.mouse import *
from moteur.text import *
from moteur.Button import Button
from moteur.player import Player
from moteur.mapV2 import Map
from view.Menu import Menu
from view.MenuJouer import MenuJouer
from view.MenuLevel import MenuLevel
from moteur.mouse import *


def whoIsSelect(view):
    t = view[0]
    if t == 'menu': return True,False,False
    elif t == 'menujouer': return False,True,False
    elif t == 'menulevel': return False,False,True


if __name__ == '__main__':
    view = ['menu',True]
    img = Image('assets/img/logo/logo.png')
    img.resize(50,50)
    window = Window(10,10,'Labios',img)
    run = 1
    tick = Tick(60)
    menu  = Menu()
    menuJouer = MenuJouer()
    menuLevel = MenuLevel()
    while run:
        Ismenu , Ismenujouer, Ismenulevel = whoIsSelect(view)
        window.update()
        if Ismenu:
            if view[1]:
                print(view[0])
                view[1] = False
                menu.aff(window)
            menu.affUpdate(window)
        elif Ismenujouer:
            if view[1]:
                print(view[0])
                view[1] = False
                menuJouer.aff(window)
            menuJouer.affUpdate(window)
        elif Ismenulevel:
            if view[1]:
                print(view[0])
                view[1] = False
                menuLevel.aff(window)
            menuLevel.affUpdate(window)
        for event in get_event():
           if Ismenu:
               view = menu.events(event)
               run = menu.eventEscape(event)
           elif Ismenujouer:
               view = menuJouer.events(event)
               run = menuJouer.eventEscape(event)
           elif Ismenulevel:
               view = menuLevel.events(event)
               run = menuLevel.eventEscape(event)
        tick.set_tick()
    stop()

