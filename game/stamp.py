import pygame
from .news_article import DraggableNewsArticle
from .constants import FONTS, BLACK, ASSETS_PATH

class Stamp:
    def __init__(self, color: str):
        self.stamp_sprite = color == 'red' and pygame.image.load(ASSETS_PATH['red_stamp']).convert_alpha() or pygame.image.load(ASSETS_PATH['green_stamp']).convert_alpha()
        self.color = color
        self.coordinates = 'green' and (100, 500) or (540 - self.stamp_sprite.get_width(), 500)
    
    
    def display(self, surface: pygame.Surface) -> None:
        self.surface.blit(self.stamp_sprite, self.coordinates)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.coordinates.collidepoint(event.pos):   
                match self.color:
                    case 'red':
                        raise NotImplementedError()
                    case 'green':
                        raise NotImplementedError()