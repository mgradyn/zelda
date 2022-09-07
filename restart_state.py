
import pygame

class Restart:
    def __init__(self, stop):
        self.stop = stop

    def restart(self):
        self.stop()