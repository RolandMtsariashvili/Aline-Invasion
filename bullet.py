import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class for managing bullets shoted bu the ship"""

    def __init__(self, ai_settings, screen, ship):
        """creates the new bullet in the position of the ship"""
        super().__init__()
        self.screen = screen

        # creating bullet in position (0, 0) and giving the right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # position of the bullet is saving in material format.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """dragging the bullet up"""
        # refreshing bullet position in material type
        self.y -= self.speed_factor
        # refreshing rect's position
        self.rect.y = self.y

    def draw_bullet(self):
        """showing the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
