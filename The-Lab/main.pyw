# -*- coding: utf-8 -*-

#import
from moteur.window import Window
from moteur.Image import Image
from moteur.event import *
from moteur.time import Tick
from moteur.mouse import get_PressedMouse , get_posMouse

def test():
    img = Image('assets/img/logo/logo.png')
    window = Window(500,500,'test',img)
    run = 1
    tick = Tick(60)
    img.resize(100,100)
    print(img.get_rect())
    img.aff(window,150,150)
    print(img.get_rect())
    while run == 1:
        window.update()
        #print(get_PressedMouse())
        print(get_posMouse())
        for event in get_event():
            run = escape(event)
        tick.set_tick()

    stop()

test()