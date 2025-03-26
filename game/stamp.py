import pygame
from .constants import ASSETS_PATH

class Stamp:
    def __init__(self, color: str) -> None:
        self.stamp_sprite = pygame.image.load(ASSETS_PATH['red_stamp']).convert_alpha() if color == 'red' else pygame.image.load(ASSETS_PATH['green_stamp']).convert_alpha()
        self.color = color
        self.rect = self.stamp_sprite.get_rect()
        self.rect.y = 506
        self.is_hovered = False
        if self.color == 'red':
            self.rect.x = 600
        else:
            self.rect.x = 88

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.stamp_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)