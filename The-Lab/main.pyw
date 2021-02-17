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

if __name__ == '__main__':
    view = ['menu',True]
    img = Image('assets/img/logo/logo.png')
    img.resize(50,50)
    window = Window(10,10,'Labios',img)
    run = 1
    tick = Tick(60)
    menu  = Menu()
    menuJouer = MenuJouer()
    while run:
         window.update()
         if view[0] == 'menu':
             if view[1]:
                 view[1] = False
                 menu.aff(window)
             menu.affUpdate(window)
         elif view[0] == 'menujouer':
             if view[1]:
                 view[1] = False
                 menuJouer.aff(window)
             menuJouer.affUpdate(window)
         for event in get_event():
            if view[0] == 'menu':
                view = menu.events(event)
                run = menu.eventEscape(event)
            elif view[0] == 'menujouer':
                view = menuJouer.events(event)
                run = menuJouer.eventEscape(event)
         tick.set_tick()

    stop()

