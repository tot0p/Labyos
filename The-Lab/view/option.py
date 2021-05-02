from moteur.Image import Image
from moteur.text import Font
from moteur.Button import Button
from moteur.color import *
from moteur.event import *
from moteur.fichier import Fichier
from moteur.forme import draw_fill_rectangle , Point

#g{avancer : z,reculer : s,aller a gauche : q,aller a droite : d}
#g['avancer'] 
class Option:

    def __init__(self):

        self.file = Fichier('donne/touche.txt')
        self.touche = self.file.variableFileLecture()  
        self.img = Image('assets/img/vide1x1.png');self.img2 = Image('assets/img/vide1x1.png');self.img3= Image('assets/img/vide1x1.png'); self.img4=Image('assets/img/vide1x1.png');self.imgApply=Image('assets/img/button/200x50.png');self.imgretour = Image('assets/img/button/retour.png');self.imgfullscreen = Image('assets/img/button/200x50.png');self.imglang = Image('assets/img/button/200x50.png')
        self.img.resize(200,50);self.img2.resize(200,50);self.img3.resize(200,50);self.img4.resize(200,50);self.imgretour.resize(50,50);self.imgApply.resize(200,50)
        self.font= Font(20,'Thick',salmon)
        self.font2=Font(8,'Thick',salmon)
        self.button = [Button(self.img,self.font,'Avancer'),Button(self.img2,self.font,'reculer'),Button(self.img3,self.font,'gauche'),Button(self.img4,self.font,'droite')]
        self.retour = Button(self.imgretour,self.font2)
        self.Bfullscreen = Button(self.imgfullscreen,self.font2)
        self.attribut = ["avancer","reculer","gauche","droite"]
        self.buttonApply = Button(self.imgApply,self.font,'Apply')
        self.view = ['option',False,'']
        self.keychange = [False,None,None]
        #fullscreen & lang
        self.fileInfo= Fichier('donne/info.txt')
        self.info = self.fileInfo.variableFileLecture()
        self.infoTemp = self.fileInfo.variableFileLecture()

        self.Blang = Button(self.imglang,self.font2,self.infoTemp['lang'])
    

    def get_fullscreen(self):
        return bool(int(self.info['fullscreen']))

    def get_lang(self):
        return self.info['lang']

    def events(self,event):
        '''
        fonction qui prend en paramètre un event pygame et qui renvoie une liste qui est constituer d'un str option et d'un bool False 
        '''
        if Mouse_on_window():
            click , posCursor = clicgauche(event)
            if click == True:
                for i in range(len(self.button)):
                    g , v = self.button[i].EventClic(posCursor[0],posCursor[1],lambda : self.__changeKey(self.attribut[i]))
                    if g:
                        return self.view
                g, v =self.Bfullscreen.EventClic(posCursor[0],posCursor[1], lambda : self.__changeFullscreen())
                if g:
                        return self.view
                g , v = self.Blang.EventClic(posCursor[0],posCursor[1],lambda :self.__changeLang())
                if g:
                    return self.view
                g , v = self.retour.EventClic(posCursor[0],posCursor[1],lambda :self.__echap())
                if g:
                    return v
                g ,v = self.buttonApply.EventClic(posCursor[0],posCursor[1],lambda : self.__apply())
                return self.view
            if self.keychange[0] and self.keychange[1] is not None and self.keychange[2] is not None:
                    self.touche[self.keychange[1]] = str(self.keychange[2])
                    self.keychange[0] = False
            elif self.keychange[0] and self.keychange[1] is not None:
                if event.type == pygame.KEYDOWN:
                    self.keychange[2] = event.key
        return self.view

    def __echap(self):
        '''
        fonction permet de retourner a la vue menu
        '''
        self.touche = self.file.variableFileLecture()  
        return ['menu',True,'']
          
    def __changeFullscreen(self):
        self.infoTemp['fullscreen'] = str(int(not self.get_fullscreen()))

    def __changeLang(self):
        if self.info['lang'] == "francais":
            self.infoTemp['lang'] = "english"
        else:
            self.infoTemp['lang'] = "francais"
        self.__setTexteLang()

    def eventEscape(self,event):
        '''
        Fonction qui prend en paramètre un event pygame et qui renvoie ce que renvoie la fonction escape avec comme paramètre event
        '''
        return escape(event)

    def __setTexteFullscreen(self):
        if bool(int(self.infoTemp['fullscreen'])):
            self.Bfullscreen.change_text('Fullscreen')
        else:
            self.Bfullscreen.change_text('Fenetre')

    def __setTexteLang(self):
        self.Blang.change_text(self.infoTemp['lang'])


    def __affall(self,window):
        if self.get_fullscreen() != window.get_fullscreen():
            window.set_fullscreen(self.get_fullscreen())
        if self.infoTemp['lang'] == "english":
            self.font.aff(window,pygame.key.name(int(self.touche['avancer'])),375,125)
            self.font.aff(window,pygame.key.name(int(self.touche['reculer'])),375,175)
            self.font.aff(window,pygame.key.name(int(self.touche['gauche'])),375,225)
            self.font.aff(window,pygame.key.name(int(self.touche['droite'])),375,275)
            self.font.aff(window,'worth',250,125)
            self.font.aff(window,'worth',250,175)
            self.font.aff(window,'worth',250,225)
            self.font.aff(window,'worth',250,275)
            self.button = [Button(self.img,self.font,'forward'),Button(self.img2,self.font,'back'),Button(self.img3,self.font,'left'),Button(self.img4,self.font,'right')]
            for i in range(len(self.button)):
                    self.button[i].aff(window,65,50*i+111)
        else:
            self.font.aff(window,pygame.key.name(int(self.touche['avancer'])),375,125)
            self.font.aff(window,pygame.key.name(int(self.touche['reculer'])),375,175)
            self.font.aff(window,pygame.key.name(int(self.touche['gauche'])),375,225)
            self.font.aff(window,pygame.key.name(int(self.touche['droite'])),375,275)
            self.font.aff(window,'vaut',275,125)
            self.font.aff(window,'vaut',275,175)
            self.font.aff(window,'vaut',275,225)
            self.font.aff(window,'vaut',275,275)
            for i in range(len(self.button)):
                    self.button[i].aff(window,75,50*i+111)


        self.font.aff(window,'Option',200,50)
        self.buttonApply.aff(window,150,450)
        self.retour.aff(window,25,25)
        self.__setTexteFullscreen()
        self.Bfullscreen.aff(window,150,330)
        self.Blang.aff(window,150,390)

    def affUpdate(self,window):
        '''
        fonction qui prend en paramètre: window de type Window
        sert a afficher la touche utiliser
        '''
        draw_fill_rectangle(Point(250,250),500,500,black,window)
        self.__affall(window)


    def aff(self,window):
        '''
        fonction qui prend en paramètre: window de type Window
        elle permet d'afficher les button, les str '='  
        '''
        window.reload(500,500)
        self.__affall(window)

    def __apply(self):
        '''
        Fonction qui sert a afficher les nouvelle option
        '''
        self.file.variableFileWrite(self.touche)
        self.fileInfo.variableFileWrite(self.infoTemp)
        self.info = self.fileInfo.variableFileLecture()
        
        
    def __changeKey(self,attribut:str):
        '''
        Fonction qui prend un attribut : str
        '''
        self.keychange = [True,attribut,None]