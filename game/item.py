import pygame
from .news_article import NewsArticle
from .constants import ASSETS_PATH, BANNED_AUTHORS_LIST, BANNED_BIBLIOGRAPHY_LIST
from .display_utils import DisplayUtils

class Item:
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.item_sprite = pygame.image.load(ASSETS_PATH[name]).convert_alpha()
        self.cursor_item_sprite = pygame.image.load(ASSETS_PATH[name]).convert_alpha()
        self.rect = self.item_sprite.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.is_hovered = False
        self.dragging = False

    def draw(self, surface: pygame.Surface) -> None:
        if not self.dragging:
            surface.blit(self.item_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event, surface: pygame.Surface, news_article: NewsArticle = None) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            if self.dragging and news_article:
                if news_article.rect.collidepoint(event.pos):
                    news_article.set_selected(True)
                else:
                    news_article.set_selected(False)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            self.dragging = True
            cursor_image = self.cursor_item_sprite
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), cursor_image))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging:
            self.dragging = False
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()))
            if news_article and news_article.rect.collidepoint(event.pos):
                news_article.set_selected(False)
                if self.name == 'formatting':
                    if news_article.incogruences['formatting']:
                        DisplayUtils.display_message(surface, "Incongruence Detected")
                    else:
                        DisplayUtils.display_error_icon(surface)