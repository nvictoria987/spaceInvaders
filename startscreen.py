import pygame.font



class Startscreen():
    def __init__(self,ai_settings, screen, play_button, high_score_button):
        self.screen=screen
        self.ai_settings = ai_settings
        self.play_button=play_button
        self.high_score_button=high_score_button
        self.bg_color = (0, 0, 0)
        self.title="Space Invaders"
        self.alien1txt = " = 150 points"
        self.alien2txt = " = 100 points"
        self.alien3txt = " = 50 points"
        self.font = pygame.font.SysFont(None, 100)
        self.alien_font = pygame.font.SysFont(None, 50)
        self.alien1 = pygame.image.load('images/alienPaint.png')
        self.alien2 = pygame.image.load("images/alien2Paint.png")
        self.alien3 = pygame.image.load("images/alien3Paint.png")

    def start(self):
        self.screen.fill(self.bg_color)
        self.titlemsg()
        self.alien1msg()
        self.alien2msg()
        self.alien3msg()
        self.play_button.draw_button()
        self.high_score_button.draw_button()
        self.screen.blit(self.alien1, (self.ai_settings.screen_width/3,140))
        self.screen.blit(self.alien2, (self.ai_settings.screen_width/3, 190))
        self.screen.blit(self.alien3, (self.ai_settings.screen_width/3, 240))

    def titlemsg(self):
            """Turn msg into a rendered image, and center text on the button."""
            self.msg_image = self.font.render(self.title, True, (0, 255, 0))
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = (400, 90)
            self.screen.blit(self.msg_image, self.msg_image_rect)
    def alien1msg(self):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.alien_font.render(self.alien1txt, True, (230, 230, 230))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2+50,150)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def alien2msg(self):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.alien_font.render(self.alien2txt, True, (230, 230, 230))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2+50, 200)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def alien3msg(self):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.alien_font.render(self.alien3txt, True, (230, 230, 230))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width/2+50, 250)
        self.screen.blit(self.msg_image, self.msg_image_rect)


