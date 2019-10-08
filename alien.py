import pygame
from pygame.sprite import Sprite
from timer import Timer
import random


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.value=150

        # moving animation
        self.frames = [pygame.image.load('images/alienPaint.png'), pygame.image.load('images/alien-1Paint.png')]
        self.rect = self.frames[0].get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # current animation
        self.animation = Timer(self.frames, wait=500)

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def draw(self):
        image = self.animation.imagerect()
        self.screen.blit(image, self.rect)

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

   # def blitme(self):
    #    """Draw the alien at its current location."""
     #   self.screen.blit(self.image, self.rect)


class Alien_two(Alien):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien_two,self ).__init__(ai_settings,screen)
        # Load the alien image, and set its rect attribute.
        self.frames = [pygame.image.load('images/alien2Paint.png'), pygame.image.load('images/alien2-1Paint.png')]
        self.rect = self.frames[0].get_rect()
        self.animation = Timer(self.frames, wait=random.randint(2, 5) * 100)
        self.value = 100


class Alien_three(Alien):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super().__init__(ai_settings,screen)
        # Load the alien image, and set its rect attribute.
        self.frames = [pygame.image.load('images/alien3Paint.png'), pygame.image.load('images/alien3-1Paint.png')]
        self.rect = self.frames[0].get_rect()
        self.animation = Timer(self.frames, wait=random.randint(2, 5) * 100)
        self.value = 50