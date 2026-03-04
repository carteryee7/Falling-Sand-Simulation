import pygame

class Button:
    def __init__(self, text: str, color: tuple, font_color: tuple, left, top, width, height):
        """Initialize a button with text, colors, and position.
        
        Args:
            text: The text to display on the button
            color: RGB color tuple for the button background
            font_color: RGB color tuple for the button text
            left: The left position of the button
            top: The top position of the button
            width: The width of the button
            height: The height of the button
        """
        self.text = text
        self.color = color
        self.rect = pygame.Rect(left, top, width, height)
        self.font = pygame.font.SysFont('Arial', 12)
        self.text_surface = self.font.render(text, True, font_color) # Text, anti-alias, color
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center
    
    def draw(self, surface):
        """Draw the button on the given surface.
        
        Args:
            surface: The pygame surface to draw the button on
        """
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, self.text_rect)