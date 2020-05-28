import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """initializes the ship and gives start pozition"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load image and getting rect.
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # every new ship appears in the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # saving material coordinate of ships center.
        self.center = float(self.rect.centerx)
        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """refreshes position of the ship depends on flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # updating rect attribute because of self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draws the ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """adds the ship in the center"""
        self.center = self.screen_rect.centerx

