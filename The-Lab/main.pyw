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
#from controller import Menu
from view.Menu import Menu

if __name__ == '__main__':
    view = ['menu',True]
    img = Image('assets/img/logo/logo.png')
    img.resize(50,50)
    window = Window(500,500,'Labios',img)
    run = 1
    text= Font('Rousseau il est pas bo',100,'Future',salmon)
    b = Button(img,text)
    tick = Tick(60)
    #menu = Menu()
    while run:
         window.update()
         #if view[0] == 'menu':
             #if view[1]:
                 #view[1] == False
                 #menu.aff(window)
         b.aff(window,50,50)
                 #Menu.start(window)
             #Menu.update(window)
         for event in get_event():
             #Menu.events(event)
             #run = Menu.eventEscape(event)
             run = escape(event)
         tick.set_tick()
         
    stop()
                
