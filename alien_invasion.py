# pygame library for sounds, graphics, etc..
# Sys for functionality like closing the game 
import pygame
import sys

# Set WIDTH and HEIGHT of display surface. 
WIDTH, HEIGHT = 1200, 800

class AlienInvasion:
    """Main class of Alien Invasion computer game."""
    def __init__(self):
        # Initialize the game
        pygame.init()

        # Set screen size
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Set a caption
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Main game loop of Alien Invasion."""
        while True:
            # Captures all user events such as keyboard presses or mouse movement
            for event in pygame.event.get():
                # If the user event is click on the 'x', then the system closes the window. 
                if event.type == pygame.QUIT:
                    sys.exit()
            # This will display the most recent screen drawn.
            pygame.display.flip()    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

