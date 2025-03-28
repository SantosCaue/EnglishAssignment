import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT_COLOR = (200, 100, 100)

ASSETS_PATH = {
    'background': 'assets/sprites/scenery/background.png',
    'menu': 'assets/sprites/scenery/menu.png',
    'hud': 'assets/sprites/scenery/hud.png',
    'clock_sheet': 'assets/sprites/scenery/clock_sheet.png',
    'game_over_background': 'assets/sprites/scenery/game_over_background.png',

    'news_article': 'assets/sprites/objects/news_article.png',
    'selected_news_article': 'assets/sprites/objects/selected_news_article.png',
    'approved_article': 'assets/sprites/objects/approved_article.png',
    'denied_article': 'assets/sprites/objects/denied_article.png',
    'red_stamp': 'assets/sprites/objects/red_stamp.png',
    'green_stamp': 'assets/sprites/objects/green_stamp.png',
    'paperwork': 'assets/sprites/objects/paperwork.png',
    'empty_paperwork': 'assets/sprites/objects/empty_paperwork.png',
    'calendar': 'assets/sprites/objects/calendar.png',

    'error': 'assets/sprites/icons/error.png',
    'bibliography': 'assets/sprites/icons/bibliography.png',
    'formatting': 'assets/sprites/icons/formatting.png',
    'ai_detector': 'assets/sprites/icons/ai_detector.png',
    'banned_authors': 'assets/sprites/icons/banned_authors.png',
    'locked': 'assets/sprites/icons/locked.png',

    'cursor': 'assets/sprites/cursors/cursor.png',
    'click': 'assets/sprites/cursors/click.png',
    'red_stamp_cursor': 'assets/sprites/cursors/red_stamp_cursor.png',
    'green_stamp_cursor': 'assets/sprites/cursors/green_stamp_cursor.png',
    'calendar_cursor': 'assets/sprites/cursors/calendar_cursor.png',
    'imgs_dir': 'assets/news_articles/imgs/',
    'ai_imgs_dir': 'assets/news_articles/ai_imgs/'
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

class DisplayUtils:
    @staticmethod
    def display_message(surface: pygame.Surface, message: str) -> None:
        text = FONTS.large.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
        surface.blit(text, text_rect)

    @staticmethod
    def display_error_icon(surface: pygame.Surface) -> None:
        error_icon = pygame.image.load(ASSETS_PATH['error']).convert_alpha()
        icon_rect = error_icon.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
        surface.blit(error_icon, icon_rect)

UPDATE_TIMER_EVENT = pygame.USEREVENT + 1
GAME_OVER_EVENT = pygame.USEREVENT + 2
BANNED_AUTHORS_LIST = ['Benjamin Lee', 'Isabella Hall', 'Alexander Young', 'Amelia King', 'Henry Scott', 'Charlotte Green', 'Oliver Adams', 'Mia Roberts']
BANNED_BIBLIOGRAPHY_LIST = ['Psychology Today Journal', 'AI Technology Magazine', 'Marine Conservation Journal', 'Literary News Magazine', 'Journal of Public Health', 'Tech Industry News', 'Journal of Psychology']
