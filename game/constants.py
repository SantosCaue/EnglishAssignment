import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT_COLOR = (200, 100, 100)

ASSETS_PATH = {
    'background': 'assets/sprites/background.png',
    'news_article': 'assets/sprites/news_article.png',
    'cursor': 'assets/sprites/cursor.png',
}

class FontManager:
    def __init__(self):
        font_path = 'assets/fonts/MinecraftStandard.otf'
        self.small = pygame.font.Font(font_path, 12)
        self.medium = pygame.font.Font(font_path, 24)
        self.large = pygame.font.Font(font_path, 36)

pygame.init()

FONTS = FontManager()