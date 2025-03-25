import pygame
import sys
from .menu import Menu
from .news_article import NewsArticle
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, ASSETS_PATH
from .stamp import Stamp

class GameState:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        # Carrega as imagens de fundo uma vez
        self.background = pygame.image.load(ASSETS_PATH['background']).convert()

        self.menu = Menu()
        self.news_article = NewsArticle()
        self.red_stamp = Stamp('red')
        self.green_stamp = Stamp('green')
        self.current_state = "menu"
        self.running = True

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
            if event.type == pygame.QUIT:
                self.running = False

            if self.current_state == "menu":
                action = self.menu.handle_event(event)
                if action == "start":
                    self.current_state = "game"
                elif action == "quit":
                    self.running = False

    def _update(self):
        pass

    def _render(self):
        # Desenha o background em qualquer estado
        self.window.blit(self.background, (0, 0))

        if self.current_state == "menu":
            self.menu.draw(self.window)
        elif self.current_state == "game":
            # Desenha a mesa e o artigo
            self.news_article.display(self.window)
            self.red_stamp.display(self.window)
            self.green_stamp.display(self.window)
            