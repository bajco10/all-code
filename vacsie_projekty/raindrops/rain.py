import sys
import pygame
from raindrop import Raindrop

from settings import Settings
from random import randint

class Rain:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize and create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain Simulator")
        
        self.raindrops = pygame.sprite.Group()

    
    def run_game(self):
        """Start the main loop for the program."""
        while True:
            self._check_events()
            self._update_screen()
            # self._add_raindrop()
            self._update_raindrops()
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if len(self.raindrops) < 12:
                    self._change_x_coordinate()
                    self._add_raindrop()
                 


    def _add_raindrop(self):
        """Create a new raindrop and add it to the raindrops group."""
        if len(self.raindrops) < self.settings.raindrops_allowed:
            new_raindrop = Raindrop(self)
            self.raindrops.add(new_raindrop)

    def _update_raindrops(self):
        """Update position of raindrops and get rid of old raindrops."""
        # Update raindrop positions.
        self.raindrops.update()

        # Get rid of raindrops that have been disappeared.(hit the bottom)
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.settings.screen_height:
                self.raindrops.remove(raindrop)
                self._change_x_coordinate()
    
    def _change_x_coordinate(self):
        self.settings.raindrop_x_coordinate = randint(0, float(self.settings.screen_width))

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    def _check_keydown_events(self,event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._add_raindrop()
            self._change_x_coordinate()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for raindrop in self.raindrops.sprites():
            raindrop.draw_raindrop()
        # print(self.settings.raindrop_x_coordinate)
        print(len(self.raindrops))
        # print(rain._update_raindrops())
        pygame.display.flip()
    
if __name__ == "__main__":
    # make a program instance, and run the program
    rain = Rain()
    rain.run_game()