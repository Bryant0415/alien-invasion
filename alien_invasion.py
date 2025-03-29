# Built-in
import sys

# 3rd-party
import pygame

# Custom modules
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Main class to manage game assets and overall behavior."""
    def __init__(self):
        """Initialize the game, settings, screen, and ship."""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared. 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """Create a triangular fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        num_rows = 6  # Adjust the number of rows as needed
        screen_center_x = self.settings.screen_width // 2  # Center point of the screen``

        for row in range(num_rows, 0, -1):  # Start with the widest row at the top
            num_aliens = row  # Decrease number of aliens per row as we go down
            row_width = num_aliens * (alien_width * 2)  # Calculate row width
            start_x = screen_center_x - (row_width // 2)  # Center row horizontally
            y_position = (num_rows - row) * (alien_height * 1.5)  # Stagger rows downward

            for i in range(num_aliens):
                x_position = start_x + i * (alien_width * 2)
                self._create_alien(x_position, y_position)



    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()