import pygame

class Tick:

    def __init__(self,tick):
        self.clock = pygame.time.Clock()
        self.tick = tick

    def set_tick(self):
        '''
        permet de limiter le nombre de tour de boucle par seconde
        '''
        self.clock.tick(self.tick)


class Chrono:
    def __init__(self):
        self.chrono = temp_since_start()

    def get_val(self):
        '''
        permet de recupérer la valeur du chrono
        '''
        return temp_since_start()-self.chrono
    
    def reset(self):
        '''
        permet de renistialiser le chrono
        '''
        self.chrono = temp_since_start()


def temp_since_start():
    '''
    return le temp depuis le lancement du programme
    '''
    return pygame.time.get_ticks()

def wait(mil):
    '''
    permet d'attendre mil milliseconde
    '''
    pygame.time.delay(mil)