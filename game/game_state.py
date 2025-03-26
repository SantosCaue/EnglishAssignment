import pygame
import sys
from .menu import Menu
from .news_article import DraggableNewsArticle  # Alterado para DraggableNewsArticle
from .stamp import Stamp
from .paperwork import Paperwork
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, ASSETS_PATH
from .hud import HUD, UPDATE_TIMER_EVENT

class GameState:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        # Carrega as imagens de fundo uma vez
        self.background = pygame.image.load(ASSETS_PATH['background']).convert()

        self.default_cursor = pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()
        self.click_cursor = pygame.image.load(ASSETS_PATH['click']).convert_alpha()
        self.cursor = pygame.cursors.Cursor((0, 0), self.default_cursor)
        pygame.mouse.set_cursor(self.cursor)

        self.menu = Menu()
        self.news_article = DraggableNewsArticle()
        self.red_stamp = Stamp('red')
        self.green_stamp = Stamp('green')
        self.paperwork = Paperwork()
        self.current_state = "menu"
        self.running = True
        self.game_hud = HUD()

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._render()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == UPDATE_TIMER_EVENT:
                self.game_hud.update_timer()
                
            if event.type == pygame.QUIT:
                self.running = False

            if self.current_state == "menu":
                action = self.menu.handle_event(event)
                if action == "start":
                    self.current_state = "game"
                elif action == "quit":
                    self.running = False
            elif self.current_state == "game":
                self.news_article.handle_event(event)
                self.green_stamp.handle_event(event, self.news_article)
                self.red_stamp.handle_event(event, self.news_article)
                self.paperwork.handle_event(event)

    def _update(self):
        if self.current_state == "menu":
            self.hovering = any(button.is_hovered for button in self.menu.buttons)
        elif self.current_state == "game":
            # Verifica se o cursor está sobre o news_article
            if self.news_article.rect.collidepoint(pygame.mouse.get_pos()):
                self.hovering = False
            else:
                self.hovering = (
                        self.red_stamp.is_hovered or
                        self.green_stamp.is_hovered or
                        self.paperwork.is_hovered
                )
        if not (self.red_stamp.dragging or self.green_stamp.dragging):
            new_cursor = self.click_cursor if self.hovering else self.default_cursor
            if pygame.mouse.get_cursor() != new_cursor:
                pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), new_cursor))


    def _render(self):
        # Desenha o background em qualquer estado
        self.window.blit(self.background, (0, 0))

        if self.current_state == "menu":
            self.menu.draw(self.window)
        elif self.current_state == "game":
            self.red_stamp.draw(self.window)
            self.green_stamp.draw(self.window)
            self.paperwork.draw(self.window)
            self.game_hud.draw(self.window)
            self.news_article.display(self.window)