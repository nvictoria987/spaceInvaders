import pygame
from pygame.sprite import Sprite
from timer import Timer

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.dead = False

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/mainship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Ship's explosion animation
        # frames = [pygame.image.load('images/mainshipEX1.png'),
        #           pygame.image.load('images/mainshipEX2.png'),
        #           pygame.image.load('images/mainshipEX3.png'),
        #           pygame.image.load('images/mainshipEX4.png'),
        #           pygame.image.load('images/mainshipEX5.png')]
        #self.die_anim = Timer(frames, wait=100, looponce=True)

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        if not self.dead:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.die_anim.imagerect(), self.rect)

    def die(self):
        frames = [pygame.image.load('images/mainshipEX1.png'),
                  pygame.image.load('images/mainshipEX2.png'),
                  pygame.image.load('images/mainshipEX3.png'),
                  pygame.image.load('images/mainshipEX4.png'),
                  pygame.image.load('images/mainshipEX5.png'),
                  pygame.image.load('images/mainship.png')]
        self.die_anim = Timer(frames, wait=100, looponce=True)
        self.dead=True
        #self.reset()
    def reset(self):
        self.center_ship()
        self.dead = False
        self.die_anim.reset()