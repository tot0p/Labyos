from view.Menu import Menu
from moteur.event import escape

def start(window):
    menu = Menu()
    menu.aff(window)

def update(window):
    menu.affUpdate(window)

def events(event):
    menu.events()

def eventEscape(event):
    return escape(event)