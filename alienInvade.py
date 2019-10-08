import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import Button_high
from ship import Ship
from startscreen import Startscreen
from ufo import ufo
import game_functions as gf
from random import randint


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    high_score_button = Button_high(ai_settings, screen, "High Score")
    startsc = Startscreen(ai_settings, screen, play_button, high_score_button)

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #UFO = ufo(ai_settings, screen)

    ufo_respawn_time = randint(10, 18) * 1000  # 10-18s at level 1
    ufo_timer = ufo_respawn_time
    delta_time = 0

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()
          #  gf.create_ufo(ai_settings,screen,aliens)

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
            gf.update_ufo(ai_settings, screen, ufo_respawn_time, ufo_timer, aliens, delta_time)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button, high_score_button, startsc)


run_game()
