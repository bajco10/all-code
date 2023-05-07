import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, rocket_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings

        # Load the alien images and set its rect attribute.
        self.image = pygame.image.load(r"C:\Users\Uzivatel\Desktop\alien_invasion\rocket_game\alien_downscaled_red.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact VERTICAL position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of scree."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True
    
    def update(self):
        """Move the alien top or bottom"""
        self.y += (self.settings.alien_speed * 
                        self.settings.fleet_direction)
        self.rect.y = self.y