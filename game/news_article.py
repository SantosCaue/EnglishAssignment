import pygame
from .constants import FONTS, BLACK, ASSETS_PATH


class NewsArticle:
    def __init__(self):
        self.data = {
            'date': '18/09/2007',
            'title': 'Bressan Mata 7 pessoas em Jundiaí',
            'author': 'Bressan Hater',
            'paragraph1': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!',
            'paragraph2': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!',
            'bibliography': 'Minoru Mineta'
        }
        self.window_img = pygame.image.load(ASSETS_PATH['news_window']).convert_alpha()

    def display(self, surface):
        width = surface.get_width()
        window_x = (width / 2) - self.window_img.get_width() / 2
        surface.blit(self.window_img, (window_x, 100))

        sections = self._render_text(surface, window_x)
        return sections

    def _render_text(self, surface, window_x):
        line_y_offset = 120
        news_line_spacing = 15
        sections = []
        max_text_width = self.window_img.get_width() - 20  # Margem dentro da folha

        for key, value in self.data.items():
            text = f'{key}: {value}'
            words = text.split()
            current_line = ''
            pos_x = window_x + 10  # Margem esquerda dentro da janela
            pos_y = line_y_offset
            section_height = 0

            if key == 'date':
                pos_x = (surface.get_width() / 2) + 100

            for word in words:
                test_line = current_line + word + ' '
                if FONTS.SMALL.size(test_line)[0] > max_text_width and key not in ['date']:
                    if current_line:
                        rendered = FONTS.SMALL.render(current_line, True, BLACK)
                        surface.blit(rendered, (pos_x, line_y_offset))
                        sections.append(pygame.Rect(pos_x, pos_y, rendered.get_width(),
                                                    line_y_offset - pos_y + rendered.get_height()))
                        line_y_offset += news_line_spacing
                        current_line = word + ' '
                else:
                    current_line = test_line

            if current_line:
                rendered = FONTS.SMALL.render(current_line, True, BLACK)
                surface.blit(rendered, (pos_x, line_y_offset))
                sections.append(
                    pygame.Rect(pos_x, pos_y, rendered.get_width(), line_y_offset - pos_y + rendered.get_height()))
                line_y_offset += news_line_spacing

        return sections