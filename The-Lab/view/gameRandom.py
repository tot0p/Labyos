from moteur.map import Map
import random

class game:

    def __init__(self):
        self.__choice()

    def __choice(self):
        t = random.randint(1,10)
        if t == 1:
            self.map = Map('assets/level/level1/level1.txt','assets/level/level1/code.txt')