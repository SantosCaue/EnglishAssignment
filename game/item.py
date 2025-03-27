import pygame
from .constants import ASSETS_PATH
from .news_article import DraggableNewsArticle

class Item:
    def __init__(self, name: str) -> None:
        self.item_sprite = pygame.image.load(ASSETS_PATH[name]).convert_alpha()
        self.item_cursor = pygame.image.load(ASSETS_PATH[f"{name}_cursor"]).convert_alpha()
        self.rect = self.item_sprite.get_rect()
        self.rect.y = 122
        self.rect.x = 618
        self.is_hovered = False
        self.dragging = False


    def draw(self, surface: pygame.Surface) -> None:
        if not self.dragging:
            surface.blit(self.item_sprite, self.rect.topleft)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            self.dragging = True
            cursor_image = self.item_cursor
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), cursor_image))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging:
            self.dragging = False
            pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()))