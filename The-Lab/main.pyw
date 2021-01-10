# -*- coding: utf-8 -*-

#import
from graphics import *
from m import *
from moteur.map import *

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
    


main()