import pygame
from .constants import FONTS, BLACK, ASSETS_PATH

class Stamp:
    def __init__(self, color: str):
        self.stamp_sprite = color == 'red' and pygame.image.load(ASSETS_PATH['red_stamp']).convert_alpha() or pygame.image.load(ASSETS_PATH['green_stamp']).convert_alpha()
        self.color = color
    
    def display(self, surface: pygame.Surface) -> None:
        if self.color == 'red':
            surface.blit(self.stamp_sprite, (100, 500))
        else:
            surface.blit(self.stamp_sprite, (surface.get_width() - 100 - self.stamp_sprite.get_width(), 500))