# -*- coding: utf-8 -*-

#import
from moteur.window import Window
from moteur.Image import Image
from moteur.event import *
from moteur.time import *
from moteur.mouse import *
from moteur.text import *
from controller.init import init
from moteur.Button import Button
from moteur.player import Player
from moteur.mapV2 import Map

def test():
    img = Image('assets/img/logo/logo.png')
    window = Window(500,500,'test',img)
    run = 1
    tick = Tick(60)
    print(img.get_rect())

    while run == 1:
        window.update()
        for event in get_event():
            run = escape(event)
        tick.set_tick()

    stop()

def test2():
    img = Image('assets/img/logo/logo.png')
    img.resize(50,50)
    window = Window(2000,720,'test',img,bg_color=white)
    run = 1
    tick = Tick(60)
    text= Font('Rousseau il est pas bo',100,'Future',salmon)

    b = Button(img,text)

    while run == 1:
        window.update()
        for event in get_event():
            run = escape(event)
            if Mouse_on_window():
                clic , posCursor= clicgauche(event)
                if clic == True:
                    b.EventClic(posCursor[0],posCursor[1],lambda : text.aff(100,100,window))
        b.aff(window,50,50)
        tick.set_tick()

    stop()

def testPlayer():
    img = Image('')
    img.resize(5,5)
    window = Window(720,720,'test',img)
    map = Map(window,'')
    run = 1
    tick = Tick(60)
    player = Player(img,map)
    player.spawn(window)
    window.affSprite()
    while run == 1:       
        window.update()
        for event in get_event():
            run = escape(event)
            if Mouse_on_window():
                clic , posCursor= clicgauche(event)
                if clic:
                    print('yes')
                    window.removeSprite(Player)        
        tick.set_tick()

    stop()

testPlayer()
