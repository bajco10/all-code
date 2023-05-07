class Settings:
    """A class to store all settings for rocket_test_game"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0 )

        # Rocket settings
        self.rocket_speed = 1.3
        self.rocket_limit = 3
        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (236, 220, 43, 1)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents down; -1 represents up
        self.fleet_direction = 1

