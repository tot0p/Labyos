import pygame

class Tick:

    def __init__(self,tick):
        self.clock = pygame.time.Clock()
        self.tick = tick

    def set_tick(self):
        self.clock.tick(self.tick)


class Chrono:
    def __init__(self):
        self.chrono = temp_since_start()

    def get_val(self):
        return temp_since_start()-self.chrono
    
    def reset(self):
        self.chrono = temp_since_start()


def temp_since_start():
    return pygame.time.get_ticks()

def wait(mil):
    pygame.time.delay(mil)