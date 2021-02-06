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

img = Image('assets/img/logo/logo.png')
img.resize(50,50)
window = Window(2000,720,'test',img)
run = 1
tick = Tick(60)
text= Font('Rousseau il est pas bo',100,'Future',salmon)

b = Button(img,text)
  
while run == 1:
    window.update()
    for event in get_event():
        run = escape(event)
        if Mouse_on_window():
            clic , posCursor= clicdroit(event)
            if clic == True:
                b.EventClic(posCursor[0],posCursor[1],lambda : text.aff(100,100,window))
    b.aff(window,50,50)
    tick.set_tick()

stop()

