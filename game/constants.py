import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT_COLOR = (200, 100, 100)

ASSETS_PATH = {
    'background': 'assets/sprites/scenery/background.png',

    'news_article': 'assets/sprites/objects/news_article.png',
    'paperwork': 'assets/sprites/objects/paperwork.png',
    'red_stamp': 'assets/sprites/objects/red_stamp.png',
    'green_stamp': 'assets/sprites/objects/green_stamp.png',

    'heart': 'assets/sprites/icons/heart.png',

    'cursor': 'assets/sprites/cursors/cursor.png',
    'click': 'assets/sprites/cursors/click.png',
    'red_stamp_cursor': 'assets/sprites/cursors/red_stamp_cursor.png',
    'green_stamp_cursor': 'assets/sprites/cursors/green_stamp_cursor.png',
}

class FontManager:
    def __init__(self):
        font_path = 'assets/fonts/MinecraftStandard.otf'
        self.small = pygame.font.Font(font_path, 10)
        self.title = pygame.font.Font(font_path, 12)
        self.medium = pygame.font.Font(font_path, 24)
        self.large = pygame.font.Font(font_path, 36)

pygame.init()

FONTS = FontManager()