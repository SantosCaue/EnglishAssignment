import pygame
from .constants import FONTS, ASSETS_PATH

class DisplayUtils:
    @staticmethod
    def display_message(surface: pygame.Surface, message: str) -> None:
        # Renderiza o texto com contorno preto
        outline_color = (0, 0, 0)
        text_color = (255, 255, 255)
        font = FONTS.large
        message = message.replace("Incongruence", "Incongruence\n")
        lines = message.split('\n')

        # Calcula a altura total do texto
        total_height = len(lines) * font.get_height()

        for i, line in enumerate(lines):
            text = font.render(line, True, text_color)
            text_rect = text.get_rect(center=(surface.get_width() // 2, (surface.get_height() // 2 - total_height // 2) + i * font.get_height()))

            # Desenha o contorno
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        outline_text = font.render(line, True, outline_color)
                        outline_rect = outline_text.get_rect(center=(surface.get_width() // 2 + dx, (surface.get_height() // 2 - total_height // 2) + dy + i * font.get_height()))
                        surface.blit(outline_text, outline_rect)

            # Desenha o texto principal
            surface.blit(text, text_rect)

        pygame.display.update()
        pygame.time.wait(1500)