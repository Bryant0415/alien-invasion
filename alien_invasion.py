# Built-in
import sys  # For clean program exit

# 3rd-party
import pygame  # Core game development library

# Custom modules
from settings import Settings  # Game configuration
from ship import Ship          # Player ship class

class AlienInvasion:
    """Main class to manage game assets and overall behavior."""

    def __init__(self):
        """Initialize the game, settings, screen, and ship."""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Set up the display surface
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")

        # Create the player's ship
        self.ship = Ship(self)
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()     # Handle input
            self.ship.update()       # Update ship position
            self._update_screen()    # Redraw screen
            self.clock.tick(60)      # Limit FPS
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _update_screen(self):
        """Redraw the screen and all game elements."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
