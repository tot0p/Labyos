from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from tkinter import Tk
from tkinter.filedialog import *

class MenuJouer:

    def __init__(self):

        self.img = Image('assets/img/button/200x50.png')
        self.img2 = Image('assets/img/button/200x50.png')
        self.img3 = Image('assets/img/button/retour.png')
        self.font= Font(20,'Thick',salmon) 
        self.font2= Font(8,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Histoire'),Button(self.img2,self.font,'Creatif'),Button(self.img3,self.font2)]
        self.function = [lambda : self.__view('menulevel'), lambda : self.__charger('game') ,lambda : self.__view('menu')]
        self.view = ['menujouer',False,'']

    def __view(self,name):
        '''
        fonction qui prend en parametre name et qui renvoie une liste qui comprend name, un bool qui vaut True et un str vide
        '''

        return [name,True,'']

    def __charger(self,name):
        '''
        fonction qui prend en paramètre : name
        cette fonction permet d'ouvrir l'explorateur de fichier
        renvoie 
       
        '''
        tk = Tk()
        tk.geometry("0x0")
        tk.iconbitmap('assets/img/logo/logo.ico')
        filename = askopenfilename(initialdir="/Desktop", title="Ouvrir", filetypes=(("Text Files","*.txt"),("Python Files","*.py"),("all files","*.*")))   
        tk.destroy()
        if filename != '':
            return [name,True,filename]
        else:
            return self.view

    def events(self,event):
        '''
        fonction qui prend en parametre un event et qui renvoie une liste qui est constituer d'un str menujoueur, d'un bool False et d'un str vide(self.view)
        '''
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],self.function[i])
                    if g:   return v
        return self.view



    def eventEscape(self,event):
        '''
        Fonction qui prend en paramètre un event pygame et qui renvoie ce que renvoie la fonction escape avec comme paramètre event
        '''
        return escape(event)

    def aff(self,window):
        '''
        fonction qui prend en paramètre: window de type Window
        elle permet d'afficher les button '
        '''
        
        window.reload(500,500)
        self.button[2].aff(window,25,25)
        for i in range(0,len(self.button)-1):
                self.button[i].aff(window,150,200+100*i)