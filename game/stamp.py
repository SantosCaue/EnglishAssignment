import pygame
from .constants import ASSETS_PATH
from .news_article import NewsArticle

class Stamp:
    def __init__(self, color: str) -> None:
        self.stamp_sprite = pygame.image.load(ASSETS_PATH['red_stamp']).convert_alpha() if color == 'red' else pygame.image.load(ASSETS_PATH['green_stamp']).convert_alpha()
        self.red_stamp_cursor = pygame.image.load(ASSETS_PATH['red_stamp_cursor']).convert_alpha()
        self.green_stamp_cursor = pygame.image.load(ASSETS_PATH['green_stamp_cursor']).convert_alpha()
        self.color = color
        self.rect = self.stamp_sprite.get_rect()
        self.rect.y = 506
        self.is_hovered = False
        self.dragging = False
        if self.color == 'green':
            self.rect.x = 88
        else:
            self.rect.x = 600

    def draw(self, surface: pygame.Surface) -> None:
        if not self.dragging:
            surface.blit(self.stamp_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event, news_article: NewsArticle) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            if self.dragging:
                if news_article.rect.collidepoint(event.pos):
                    news_article.set_selected(True)
                else:
                    news_article.set_selected(False)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            self.dragging = True
            cursor_image = self.red_stamp_cursor if self.color == 'red' else self.green_stamp_cursor
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), cursor_image))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging:
            self.dragging = False
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()))
            news_article.set_selected(False)