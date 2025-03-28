import pygame # We need pygame's tools and functionalities to draw images position them

class Ship:
    """A class to store al the player's ship assets and behaviors. """
    def __init__(self, ai_game):
        """Initialize pygame, screen, settings, and load image"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Define  starting location for that image
        self.rect.midbottom = self.screen_rect.midbottom #Move the boxes, not the image or the screen. The rects determine location of image/screen

        # Precision motion
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False 
    def update(self):
        """Update the ships locaton depending on user events"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect from self.x
        # Why is this necessary? 
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship on the screen"""
        self.screen.blit(self.image, self.rect)