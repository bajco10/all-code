import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    """A class to manage rain falling from the sky."""

    def __init__(self, rain_program):
        """Create a raindrop object at the top of the screen."""
        super().__init__()
        self.screen = rain_program.screen
        self.settings = rain_program.settings
        self.color = self.settings.raindrop_color
        self.raindrop_x_coordinate = self.settings.raindrop_x_coordinate

        # Create a raindrop at (0, 0) and then set correct position.
        self.rect = pygame.Rect(self.raindrop_x_coordinate, 0, self.settings.raindrop_width, self.settings.raindrop_height)

        # Store the raindrop's position as a decimal value.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the raindrop down the screen."""
        # Update the decimal position of the raindrop.
        self.y += self.settings.raindrop_speed
        # Update the rect position.
        self.rect.y = self.y
        # print(self.y)
    
    def draw_raindrop(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)






