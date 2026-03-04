import pygame

class Button:
    def __init__(self, text: str, color: tuple, font_color: tuple, left, top, width, height):
        self.text = text
        self.color = color
        self.rect = pygame.Rect(left, top, width, height)
        self.font = pygame.font.SysFont('Arial', 12)
        self.text_surface = self.font.render(text, True, font_color) # Text, anti-alias, color
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, self.text_rect)