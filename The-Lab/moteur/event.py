import pygame


def keypressed(event):
    pressed = {}
    if event.type == pygame.KEYDOWN:
        pressed[event.key] = True
    return pressed

def get_event():
    return pygame.event.get()
        
def escape(event):
    if event.type == pygame.QUIT :
        return 0
    return 1

def get_click(event):
    pass

def stop():
    pygame.quit()