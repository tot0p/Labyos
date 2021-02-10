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
img2 = Image('assets/img/logo/testimage2.png')
img3 = Image('assets/img/logo/testimage3.png')
img.resize(200,50)
img2.resize(200,50)
img3.resize(200,50)
window = Window(500,500,'test',img)
run = 1
tick = Tick(60)
text= Font('Rousseau il est pas bo',100,'Future',salmon)
text2=Font('i',100,'Future',salmon)
text3=Font('i5',100,'Future',salmon)
b = Button(img,text)
b2=Button(img2,text2)
b3=Button(img3,text3)
while run == 1:
    window.update()
    for event in get_event():
        run = escape(event)
        if Mouse_on_window():
            clic , posCursor= clicgauche(event)
            if clic == True:
                b.EventClic(posCursor[0],posCursor[1],lambda : text.aff(100,100,window))
    b.aff(window,150,200)
    b2.aff(window,150,300)
    b3.aff(window,150,400)
    tick.set_tick()

stop()

