import pygame


class Rocket:
    """A class to manage the rocket."""

    def __init__(self, rocket_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()
        self.settings = rocket_game.settings
        # load the rocket image and its rect
        self.image = pygame.image.load(r"C:\Users\Uzivatel\Desktop\alien_invasion\rocket_game\rocket_downscaled_2.png")
        self.rect = self.image.get_rect()
        # start each new rocket in the middle of the screen
        self.rect.midleft = self.screen_rect.midleft
        # store a decimal value for the rocket's horizontal position
        self.x = float(self.rect.x)
        # store a decimal value for the rocket's vertical position
        self.y = float(self.rect.y)
        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # update the rect object form from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def center_rocket(self):
        """Center the rocket on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)