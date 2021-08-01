class Settings:
    """All the settings for Target Practice are stored here."""
    def __init__(self):
        """Initalize the attributes."""
        # Screen or Display settings.
        self.screen_width = 0
        self.screen_height = 0
        self.bgcolor = (0, 0, 0)

        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 3 
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 2

        # Target settings.
        self.target_width = 15      
        self.target_color = (255, 0, 0)
        self.target_direction = 1

        self.default_settings()

    def default_settings(self):
        """Set the default values."""
        self.ship_speed = 2
        self.bullet_speed = 3.5
        self.target_height = 250

    def speed_up(self):
        """Increase the Target Practice speed as the game progress."""
        self.ship_speed += 0.1
        self.bullet_speed += 0.3

