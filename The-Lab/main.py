# -*- coding: utf-8 -*-

#import
from graphics import *
from m import *
from moteur.map import *

def main():
    init_graphic(500,500)
    run = 1
    map = Map(500,500)
    while run == 1:
        draw_circle(Point(250,250),39,white)
        run = eventMenu()
        affiche_all()
    quit()
    


main()