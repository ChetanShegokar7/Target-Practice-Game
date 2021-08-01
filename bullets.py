import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """Class to create Bullets."""
    def __init__(self, tp):
        """Initializing the attributes."""
        super().__init__()
        self.screen = tp.screen
        self.settings = tp.settings
        self.screen_rect = self.screen.get_rect()

        self.bullet = pygame.Rect(0, 0, 
            self.settings.bullet_width, self.settings.bullet_height)
        self.rect = self.bullet
        self.bullet.midright = tp.ship.rect.midright

        self.x = float(self.bullet.x)

    def update(self):
        """Move the bullets to the right side of the screen."""
        self.x += self.settings.bullet_speed
        self.bullet.x = self.x

    def display_bullets(self):
        """Display the bullets to the screen."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.bullet)