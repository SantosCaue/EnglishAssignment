import datetime
import pygame
import json
import random
from .constants import FONTS, BLACK, ASSETS_PATH, WINDOW_WIDTH, WINDOW_HEIGHT, BANNED_AUTHORS_LIST, BANNED_BIBLIOGRAPHY_LIST

class NewsArticle:
    def __init__(self, red_stamp, green_stamp):
        self.data = self._load_random_article()
        self.news_article_img = pygame.image.load(ASSETS_PATH['news_article']).convert_alpha()
        self.selected_news_article_img = pygame.image.load(ASSETS_PATH['selected_news_article']).convert_alpha()
        self.approved_img = pygame.image.load(ASSETS_PATH['approved_article']).convert_alpha()
        self.denied_img = pygame.image.load(ASSETS_PATH['denied_article']).convert_alpha()
        self.rect = self.news_article_img.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        self.red_stamp = red_stamp
        self.green_stamp = green_stamp

        self.dragging = False
        self.hovered_section = None
        self.section_rects = {}
        self.is_selected = False
        self.is_visible = False
        self.is_approved = None
        self.animation_in_progress = False
        self.animation_start_time = None

        

    def set_selected(self, selected):
        self.is_selected = selected
        if self.is_selected:
            self.news_article_img = self.selected_news_article_img
        else:
            self.news_article_img = pygame.image.load(ASSETS_PATH['news_article']).convert_alpha()

    @staticmethod
    def _load_random_article():
        with open('assets/news_articles/news_data.json', 'r') as file:
            news_data = json.load(file)
            news_articles = news_data
            return random.choice(news_articles)

    def handle_event(self, event):
        if not self.animation_in_progress:
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
                    new_x = self.mouse_x + self.offset_x
                    new_y = self.mouse_y + self.offset_y

                    if new_x < 0:
                        new_x = 0
                    elif new_x + self.rect.width > WINDOW_WIDTH:
                        new_x = WINDOW_WIDTH - self.rect.width

                    if new_y < 0:
                        new_y = 0
                    elif new_y + self.rect.height > WINDOW_HEIGHT:
                        new_y = WINDOW_HEIGHT - self.rect.height

                    self.rect.x = new_x
                    self.rect.y = new_y
                else:
                    self._check_hover(event.pos)



    def _check_hover(self, mouse_pos):
        self.hovered_section = None
        for section, rect in self.section_rects.items():
            if rect.collidepoint(mouse_pos):
                self.hovered_section = section
                break

    def start_animation(self, approved):
        self.is_approved = approved
        self.animation_in_progress = True
        self.animation_start_time = pygame.time.get_ticks()


    def update_animation(self):
        if self.animation_in_progress:
            current_time = pygame.time.get_ticks()
            if current_time - self.animation_start_time > 500:
                direction = -1 if self.is_approved else 1
                self.rect.x += direction * 10
                if self.rect.right < -15 or self.rect.left > WINDOW_WIDTH + 15:
                    self.is_visible = False
                    self.animation_in_progress = False

    def display(self, surface):
        if self.is_visible:
            if self.animation_in_progress:
                if self.animation_in_progress:
                    surface.blit(self.approved_img if self.is_approved else self.denied_img, self.rect.topleft)
            else:
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
            pos_x = self.rect.x + 20

            if key == 'title':
                font = FONTS.title
            else:
                font = FONTS.small

            if key == 'date':
                pos_x = self.rect.x + self.news_article_img.get_width() - font.size(text)[0] - 10

            # Inicializa o retângulo da seção com largura e altura zero
            section_rect = pygame.Rect(pos_x, line_y_offset, 0, 0)

            for word in words:
                test_line = current_line + word + ' '
                if font.size(test_line)[0] > max_text_width and key not in ['date']:
                    if current_line:
                        rendered = font.render(current_line, True, BLACK)
                        surface.blit(rendered, (pos_x, line_y_offset))
                        line_width, line_height = font.size(current_line)
                        # Expande o retângulo da seção para incluir a linha renderizada
                        section_rect.union_ip(pygame.Rect(pos_x, line_y_offset, line_width, line_height))
                        line_y_offset += news_line_spacing
                        current_line = word + ' '
                else:
                    current_line = test_line

            if current_line:
                rendered = font.render(current_line, True, BLACK)
                surface.blit(rendered, (pos_x, line_y_offset))
                line_width, line_height = font.size(current_line)
                # Expande o retângulo da seção para incluir a última linha renderizada
                section_rect.union_ip(pygame.Rect(pos_x, line_y_offset, line_width, line_height))
                line_y_offset += news_line_spacing

            # Adiciona espaçamento extra após a data, título e parágrafo 2
            if key in ['title', 'date', 'author', 'paragrafo2']:
                line_y_offset += 15
                if key != 'title':
                    line_y_offset += 15

            self.section_rects[key] = section_rect  # Armazena o retângulo da seção

            # Desenha o contorno se o mouse estiver sobre a seção
            if self.hovered_section == key and not (self.red_stamp.dragging or self.green_stamp.dragging):
                pygame.draw.rect(surface, BLACK, section_rect, 2)  # Desenha o contorno em volta da seção
                
            def verify(self, news_article: NewsArticle) -> dict[str: bool]:
                incongruences = {}
                incongruences["banned_authors"] = self.data["author"] in BANNED_AUTHORS_LIST
                incongruences["bibliography"] = self.data["bibliography"] in BANNED_BIBLIOGRAPHY_LIST
                incongruences["formatting"] = False
                for i, val in self.data:
                    if val.empty():
                        incongruences["formatting"] = True
                incongruences["calendar"] = datetime.strptime("07/03/2006", "%d/%m/%Y") < datetime.strptime(self.data["date"], "%d/%m/%Y")                
                incongruences["ia_detector"] = self.data["image"] == "AI"  
                return incongruences