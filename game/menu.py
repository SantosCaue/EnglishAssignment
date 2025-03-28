import pygame
from .button import Button
from .constants import WINDOW_WIDTH, WINDOW_TITLE, WHITE, FONTS, ASSETS_PATH


class Menu:
    def __init__(self):
        self.buttons = []
        self.background = pygame.image.load(ASSETS_PATH['menu']).convert()
        self._create_buttons()

    def _create_buttons(self):
        button_width, button_height = 200, 50
        start_x = (WINDOW_WIDTH - button_width) // 2

        self.buttons.extend([
            Button(start_x, 420, button_width, button_height, "Start", lambda: "start"),
            Button(start_x, 500, button_width, button_height, "Quit", lambda: "quit")
        ])

    def draw(self, surface):
        surface.blit(self.background, (0, 0))

        for button in self.buttons:
            button.draw(surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            for button in self.buttons:
                button.check_hover(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.is_hovered:
                    return button.execute_action()
        return None