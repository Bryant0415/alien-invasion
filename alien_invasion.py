import pygame
import sys
from settings import Settings 

class AlienInvasion:
    """Overall class to store all assets and behavior."""
    def __init__(self):
        """Initialize game"""
        pygame.init()

        #Set clock and settings
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Screen settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()