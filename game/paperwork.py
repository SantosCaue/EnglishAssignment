import pygame
from .constants import ASSETS_PATH, WINDOW_WIDTH

class Paperwork:
    def __init__(self) -> None:
        self.paperwork_sprite = pygame.image.load(ASSETS_PATH['paperwork']).convert_alpha()
        self.rect = self.paperwork_sprite.get_rect()
        self.rect.x = (WINDOW_WIDTH - self.rect.width) // 2
        self.rect.y = 476

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.paperwork_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event) -> None:
        pass