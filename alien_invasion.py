import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf
from pygame.sprite import Group

def run_game():
    """
    the main loop function
    """
    # init a window
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()

    # alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

        gf.update_aliens(ai_settings, aliens)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()