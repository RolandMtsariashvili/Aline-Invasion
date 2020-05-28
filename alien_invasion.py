import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # initializes the game, settings and creates screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # creating exemplare to save game statistics
    stats = GameStats(ai_settings)

    # creates the ship.
    ship = Ship(ai_settings, screen)
    # creating the groups for saving bullets and aliens.
    bullets = Group()
    aliens = Group()

    # creating alien fleet
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # start of the main loop
    while True:
        # detects the events of keyboard and mouse event.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()