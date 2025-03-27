import pygame
from .constants import ASSETS_PATH
from .news_article import NewsArticle

class Calendar:
    def __init__(self) -> None:
        self.calendar_sprite = pygame.image.load(ASSETS_PATH['calendar']).convert_alpha()
        self.calendar_cursor = pygame.image.load(ASSETS_PATH['calendar_cursor']).convert_alpha()
        self.rect = self.calendar_sprite.get_rect()
        self.rect.y = 122
        self.rect.x = 618
        self.is_hovered = False
        self.dragging = False


    def draw(self, surface: pygame.Surface) -> None:
        if not self.dragging:
            surface.blit(self.calendar_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            self.dragging = True
            cursor_image = self.calendar_cursor
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), cursor_image))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging:
            self.dragging = False
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()))
