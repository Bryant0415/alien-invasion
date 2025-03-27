class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # Black

        # Ship settings
        self.ship_speed = 1.5  # Floating-point precision movement
