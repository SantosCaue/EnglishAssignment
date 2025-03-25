import pygame
import sys
from .menu import Menu
from .news_article import DraggableNewsArticle  # Alterado para DraggableNewsArticle
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, ASSETS_PATH


class GameState:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        # Carrega as imagens de fundo uma vez
        self.background = pygame.image.load(ASSETS_PATH['background']).convert()

        cursor_image = pygame.image.load(ASSETS_PATH['cursor']).convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), cursor_image)
        pygame.mouse.set_cursor(cursor)

        self.menu = Menu()
        self.news_article = DraggableNewsArticle()  # Alterado para DraggableNewsArticle
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
            elif self.current_state == "game":
                self.news_article.handle_event(event)  # Adicionado para lidar com eventos de arrastar

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