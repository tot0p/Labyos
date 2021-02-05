import pygame

class Tick:

    def __init__(self,tick):
        self.clock = pygame.time.Clock()
        self.tick = tick

    def set_tick(self):
        self.clock.tick(self.tick)