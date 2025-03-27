import pygame
from .constants import FONTS, ASSETS_PATH

class DisplayUtils:
    @staticmethod
    def display_message(surface: pygame.Surface, message: str) -> None:
        text = FONTS.large.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
        surface.blit(text, text_rect)

    @staticmethod
    def display_error_icon(surface: pygame.Surface) -> None:
        error_icon = pygame.image.load(ASSETS_PATH['error']).convert_alpha()
        icon_rect = error_icon.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
        surface.blit(error_icon, icon_rect)