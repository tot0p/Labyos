# -*- coding: utf-8 -*-

#import
from moteur.window import Window
from moteur.Image import Image
from m import eventMenu,quit

def main():
    init_graphic(500,500)
    run = 1
    map = Map()
    map.create(500,500)
    draw_circle(Point(250,250),50,white)
    while run == 1:
        run = eventMenu()
        affiche_all()
    quit()
    


def test():
    img = Image('assets/img/logo/logo.png')
    window = Window(500,500,'test',img)
    run = 1
    img.resize(100,100)
    img.aff(window,150,150)
    while run == 1:
        window.update()
        run = eventMenu()
    quit()

test()