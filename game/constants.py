import pygame

# Configurações da janela
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT_COLOR = (200, 100, 100)

# Caminhos dos assets
ASSETS_PATH = {
    'background': 'assets/sprites/background.png',
    'table': 'assets/sprites/table.png',
    'news_window': 'assets/sprites/window.png'
}


class _FontManager:
    def __init__(self):
        self._small = None
        self._medium = None
        self._large = None

    @property
    def SMALL(self):
        if self._small is None:
            self._initialize()
        return self._small

    @property
    def MEDIUM(self):
        if self._medium is None:
            self._initialize()
        return self._medium

    @property
    def LARGE(self):
        if self._large is None:
            self._initialize()
        return self._large

    def _initialize(self):
        try:
            self._small = pygame.font.Font(None, 12)
            self._medium = pygame.font.Font(None, 24)
            self._large = pygame.font.Font(None, 36)
        except:
            self._small = pygame.font.SysFont('arial', 12)
            self._medium = pygame.font.SysFont('arial', 24)
            self._large = pygame.font.SysFont('arial', 36)


FONTS = _FontManager()