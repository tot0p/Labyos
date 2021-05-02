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
from view.Menu import Menu
from view.MenuJouer import MenuJouer
from view.MenuLevel import MenuLevel
from moteur.mouse import *
from view.game import Game
from view.option import Option
from view.win import Win
from view.gameover import GameOver
from moteur.sound import play_music ,load_music
from moteur.fichier import Fichier
from moteur.error import error


def whoIsSelect(view):
    '''
    return des bool pour savoir quelle vue est selcetionner
    '''
    t = view[0]
    if t == 'menu': return True,False,False,False,False,False,False
    elif t == 'menujouer': return False,True,False,False,False,False,False
    elif t == 'menulevel': return False,False,True,False,False,False,False
    elif t == 'game': return False,False,False,True,False,False,False
    elif t== 'option': return False,False,False,False,True,False,False
    elif t == 'gameover': return False,False,False,False,False,True,False
    elif t == 'win': return False,False,False,False,False,False,True


if __name__ == '__main__':
    view = ['menu',True,'']
    load_music('assets/song.wav')
    play_music(1)
    img = Image('assets/img/logo/logo.png')
    img.resize(50,50)
    option = Option()
    window = Window(10,10,'Labyos',img,fullscreen = option.get_fullscreen())
    lang = option.get_lang()
    langUpdate = option.get_lang()
    run = 1
    tick = Tick(60)
    menu  = Menu()
    menuJouer = MenuJouer()
    menuLevel = MenuLevel(lang)
    win = Win()
    gameover = GameOver()
    game = None
    while run:
        Ismenu , Ismenujouer, Ismenulevel , Isgame , Isoption, Isgameover , Iswin= whoIsSelect(view)
        window.update()
        if Ismenu:
            if view[1]:
                view[1] = False
                menu.aff(window)
        elif Ismenujouer:
            if view[1]:
                view[1] = False
                menuJouer.aff(window)
        elif Ismenulevel:
            if view[1]:
                view[1] = False
                menuLevel.aff(window)
        elif Isgame:
            if view[1]:
                view[1] = False
                game = Game(window,view[2])
                if game.error:
                    error("le niveau n'est pas valide , le jeu vas s'arréter",True)
                else:
                    game.aff()
            view = game.viewIs()
            game.affUpdate()
        elif Isoption:
            if view[1]:
                view[1]=False
                option.aff(window)
            option.affUpdate(window)
        elif Isgameover:
            if view[1]:
                view[1] = False
                gameover.set_filename(view[2])
                gameover.aff(window)
        elif Iswin:
            if view[1]:
                view[1]=False
                win.aff(window)
            win.affUpdate(window)
                
        for event in get_event():
           if Ismenu:
               view = menu.events(event)
               run = menu.eventEscape(event)
           elif Ismenujouer:
               view = menuJouer.events(event)
               run = menuJouer.eventEscape(event)
           elif Ismenulevel:
               view = menuLevel.events(event)
               run = menuLevel.eventEscape(event)
           elif Isgame:
               game.events(event)
               run = game.eventEscape(event)
           elif Isoption:
                view = option.events(event)
                run = option.eventEscape(event)
                langUpdate = option.get_lang()
                if lang != langUpdate:
                    menuLevel = MenuLevel(lang)
                    lang = langUpdate
           elif Isgameover:
                view = gameover.events(event)
                run = gameover.eventEscape(event)
           elif Iswin:
                view = win.events(event)
                run = win.eventEscape(event)


        tick.set_tick()
        

    stop()

