import pygame

#couleur predefinies
black=pygame.Color(0,0,0)
blue=pygame.Color(0,0,255)
brown=pygame.Color(88,41,0)
cyan=pygame.Color(0,255,255)
gold=pygame.Color(255,215,0)
gray=pygame.Color(128,128,128)
green=pygame.Color(0,255,0)
magenta=pygame.Color(255,0,255)
orange=pygame.Color(255,127,0)
pink=pygame.Color(253,108,158)
purple=pygame.Color(127,0,255)
red=pygame.Color(255,0,0)
salmon=pygame.Color(248,142,85)
silver=pygame.Color(206,206,206)
turquoise=pygame.Color(37,253,233)
white=pygame.Color(255,255,255)
yellow=pygame.Color(255,255,0)


class Window:

    def __init__(self,W,H,name,icon,bg_color=black,fullscreen=0):
        self.name = name
        self.display  = pygame.display
        self.W = int(W)
        self.H = int(H)
        self.window = self.display.set_mode((int(W),int(H)),fullscreen)
        self.display.set_caption(self.name)
        self.display.set_icon(icon.img)
        self.window.fill(bg_color)
        self.update()
    
    def reload(self,W,H,bg_color=black,fullscreen=0):
        self.W = int(W)
        self.H = int(H)
        self.window = self.display.set_mode((int(W),int(H)),fullscreen)
        self.window.set_caption(self.name)
        self.window.fill(bg_color)
        self.update()

    def get_size(self):
        return (self.W , self.H)

    def update(self):
        self.display.flip()
        