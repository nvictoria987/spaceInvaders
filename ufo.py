import pygame
from pygame.sprite import Sprite

class ufo(Sprite):

    def __init__(self,ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/alien2Paint.png')
        self.rect = self.image.get_rect()

        # starting pos (either from left or right edge of screen) and moving direction

        self.rect.centerx = self.screen_rect.width
        self.direction = -1
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        # Start each ufo at the top corner of the screen.
        self.x = float(self.rect.x)
        self.rect.y = self.rect.height



    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        self.x += (self.direction * self.ai_settings.ufo_speed_factor * 0.85)
        # Update the rect position.
        self.rect.x = int(self.x)

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True