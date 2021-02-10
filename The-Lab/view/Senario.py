from moteur.Button import*
from moteur.Image import*

class naration:
    def __init__(self,img):
        self.img = Button(img)
    
    def events(self,event):
        pass

    def aff(self,window):
        self.img.aff(window,50,50)

    def affUpdate(self,window):
        pass

    def lecture(self,text):
        img.aff(window,0,0)
        text.aff(window,0,0)
