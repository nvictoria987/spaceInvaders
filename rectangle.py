import pygame
from pygame.sprite from Sprite

class rectangle(Sprite):
    def __init__(self, length, width):
        super(rectangle , self).__init__()
        self.length = length
        self.width = width