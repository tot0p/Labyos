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
from moteur.Senario import naration

def test():
    img = Image('assets/img/logo/testimage.png')
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

img = Image('assets/img/logo/testimage.png')
window = Window(500,500,'test',img)
run = 1
tick = Tick(60)
test = naration()
while run == 1:
    window.update()
    for event in get_event():
        run = escape(event)
    tick.set_tick()
    test.aff(window,'oui')

stop()

