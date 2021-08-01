import pygame

class Target:
    """Create a target and set its position to midright of the screen."""
    def __init__(self, tp):
        """Initialize the attributes."""
        self.screen = tp.screen
        self.settings = tp.settings

        self.screen_rect = self.screen.get_rect()
        self.target_width = self.settings.target_width
        self.target_height = self.settings.target_height

        self.target = pygame.Rect(0, 0,
            self.target_width, self.target_height)

        self.rect = self.target
        self.target.midright = self.screen_rect.midright

    def update_target(self):
        """Continiously move the target to up and down."""
        self.target.y += 1 * self.settings.target_direction

        if self.target.top <= self.screen_rect.top:
            self.settings.target_direction = 1

        if self.target.bottom >= self.screen_rect.bottom:
            self.settings.target_direction = -1 

    def display_target(self):
        """display the target to the screen."""
        pygame.draw.rect(self.screen, self.settings.target_color, self.target)