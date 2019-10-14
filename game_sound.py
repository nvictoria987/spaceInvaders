import pygame

class Game_sound():
    def __init__(self):
        self.dying = pygame.mixer.Sound('sounds/death.wav')
        self.shoot = pygame.mixer.Sound('sounds/shoot.wav')
        self.background = pygame.mixer.Sound('sounds/bgg.wav')
        #self.bgON= False


    def dyingsound(self):
        self.dying.play()

    def shootsound(self):
        self.shoot.play()
    def backgroundsound(self):
        self.background.play()






