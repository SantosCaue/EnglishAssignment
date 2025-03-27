import pygame
from .constants import ASSETS_PATH, WINDOW_WIDTH
from .news_article import NewsArticle

class Paperwork:
    def __init__(self) -> None:
        self.paperwork_sprite = pygame.image.load(ASSETS_PATH['paperwork']).convert_alpha()
        self.empty_paperwork_sprite = pygame.image.load(ASSETS_PATH['empty_paperwork']).convert_alpha()
        self.rect = self.paperwork_sprite.get_rect()
        self.rect.x = (WINDOW_WIDTH - self.rect.width) // 2
        self.rect.y = 476
        self.is_hovered = False
        self.is_empty = False

    def draw(self, surface: pygame.Surface) -> None:
        if self.is_empty:
            surface.blit(self.empty_paperwork_sprite, self.rect.topleft)
        else:
            surface.blit(self.paperwork_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event, news_article: NewsArticle) -> None:
        if not self.is_empty:
            if event.type == pygame.MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
                self.is_empty = True  # Alterna para empty_paperwork
                news_article.is_visible = True  # Torna o artigo visível
                self.is_hovered = False

    def reset(self, red_stamp, green_stamp):
        self.is_empty = False
        return NewsArticle(red_stamp, green_stamp)
