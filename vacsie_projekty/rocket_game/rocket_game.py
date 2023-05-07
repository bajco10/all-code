import sys
import pygame
from time import sleep

from game_stats import GameStats
from rocket_settings import Settings
from rocket import Rocket
from rocket_bullet import RocketBullet
from alien_enemy import Alien

class RocketGame:

        
    """Overall  class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket game")
        self.stats = GameStats(self)
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.rocket.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            
    
    def _check_events(self):
        """REspond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _fire_bullet(self):
        """Create a new rocket bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet   = RocketBullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have been disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
    
    def _rocket_hit(self):
        """Respond to rocket being hit by alien"""
        if self.stats.rockets_left > 0:
            # Decrement rocket_left.
            self.stats.rockets_left -= 1
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.rocket.center_rocket()
            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_aliens(self):
        # chceck if fleet at edge -> update position of all aliens
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-shp collisions.
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()
        
        # Look for aliens hitting the left side of the screen.
        self._check_aliens_left()
    
    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2* alien_height)
        # Determine the number of rows of aliens that fit on the screen.
        rocket_width = self.rocket.rect.width
        available_space_x = (self.settings.screen_width - (3*alien_width) - rocket_width)
        number_rows = available_space_x // (4 * alien_width)
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.rect.x = alien.rect.width + 2 * alien.rect.width * row_number + 700
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _check_aliens_left(self):
        """Check if any aliens have reached the left edge of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                # Treat this the same as if the ship got hit.
                self._rocket_hit()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= - 1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        pygame.display.flip()
    


if __name__ == "__main__":
    # make a game instance, and run the game
    rg = RocketGame()
    rg.run_game()
