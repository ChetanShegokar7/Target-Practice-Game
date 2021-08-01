import pygame

class Ship:
    """Class to create ship."""
    def __init__(self, tp):
        """Creating a ship and set its position to midleft of the screen."""
        self.screen = tp.screen
        self.settings = tp.settings

        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('images/ship.png').convert_alpha()
        self.rect = self.ship.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        # Flags to move the ship.
        self.moving_up = False
        self.moving_down = False

    def update_ship(self):
        """Move the ship up and down responding to the key pressed."""
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def display_ship(self):
        """Display the ship to the screen."""
        self.screen.blit(self.ship, self.rect)