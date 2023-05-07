from cmath import rect
from random import randint

from raindrop import Raindrop
class Settings:
    """A class to store all settings for Rain program."""

    def __init__(self):
        """Initialize settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Raindrop settings
        self.raindrop_speed = 1
        self.raindrop_width = 3
        self.raindrop_height = 15
        self.raindrop_color = (0, 230, 0)
        self.raindrops_allowed = 60
        self.raindrop_x_coordinate = randint(0, float(self.screen_width))
    
    def generate_x_coordinate(self):
        """"""
    
