import pygame

class Button:
    """Create a Button with a speciofic message."""
    def __init__(self, tp, msg):
        """Initialize the attributes."""
        self.screen = tp.screen
        self.screen_rect = self.screen.get_rect()

        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont('None', 32)

        self._prep_button(msg)

    def _prep_button(self, msg):
        """Convert the message string to an image."""
        self.button_img = self.font.render(msg, True, self.font_color)
        self.button_rect = self.button_img.get_rect()
        self.button_rect.center = self.screen_rect.center

    def display_button(self):
        """Display the button on the screen."""
        self.screen.blit(self.button_img, self.button_rect)

