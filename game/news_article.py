import pygame
import json
import random
from .constants import FONTS, BLACK, ASSETS_PATH

class DraggableNewsArticle:
    def __init__(self):
        self.data = self._load_random_article()
        self.news_article_img = pygame.image.load(ASSETS_PATH['news_article']).convert_alpha()
        self.rect = self.news_article_img.get_rect(topleft=(100, 100))
        self.dragging = False

    @staticmethod
    def _load_random_article():
        with open('assets/news_articles/news_data.json', 'r') as file:
            news_data = json.load(file)
            level1_articles = news_data['level1']
            return random.choice(level1_articles)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                self.mouse_x, self.mouse_y = event.pos
                self.offset_x = self.rect.x - self.mouse_x
                self.offset_y = self.rect.y - self.mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.mouse_x, self.mouse_y = event.pos
                self.rect.x = self.mouse_x + self.offset_x
                self.rect.y = self.mouse_y + self.offset_y

    def display(self, surface):
        surface.blit(self.news_article_img, self.rect.topleft)
        self._render_text(surface)

    def _render_text(self, surface):
        line_y_offset = self.rect.y + 20
        news_line_spacing = 15
        max_text_width = self.news_article_img.get_width() - 20  # Margem dentro da folha

        for key, value in self.data.items():
            text = f'{value}'
            words = text.split()
            current_line = ''
            pos_x = self.rect.x + 10
            pos_y = line_y_offset

            if key == 'date':
                pos_x = self.rect.x + (self.news_article_img.get_width() - FONTS.small.size(text)[0]) / 2

            for word in words:
                test_line = current_line + word + ' '
                if FONTS.small.size(test_line)[0] > max_text_width and key not in ['date']:
                    if current_line:
                        rendered = FONTS.small.render(current_line, True, BLACK)
                        surface.blit(rendered, (pos_x, line_y_offset))
                        line_y_offset += news_line_spacing
                        current_line = word + ' '
                else:
                    current_line = test_line

            if current_line:
                rendered = FONTS.small.render(current_line, True, BLACK)
                surface.blit(rendered, (pos_x, line_y_offset))
                line_y_offset += news_line_spacing