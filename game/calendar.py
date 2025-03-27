import pygame
from .constants import ASSETS_PATH
from .news_article import NewsArticle
from .display_utils import DisplayUtils

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

    def handle_event(self, event: pygame.event.Event, surface: pygame.Surface, news_article: NewsArticle) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            self.dragging = True
            cursor_image = self.calendar_cursor
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), cursor_image))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging:
            self.dragging = False
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()))
            if news_article and news_article.rect.collidepoint(event.pos):
                news_article.set_selected(False)
                if news_article.hovered_section:
                    if news_article.hovered_section == 'date' and news_article.incogruences['calendar']:
                        DisplayUtils.display_message(surface, "Incongruence Detected")
                    else:
                        DisplayUtils.display_message(surface, "Incongruence Not Found")
