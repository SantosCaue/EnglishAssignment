from .constants import FONTS, ASSETS_PATH, WHITE, UPDATE_TIMER_EVENT, GAME_OVER_EVENT
import pygame


class HUD:
    def __init__(self):
        self.hud_sprite = pygame.image.load(ASSETS_PATH['hud']).convert_alpha()
        self.error_sprite = pygame.image.load(ASSETS_PATH['error']).convert_alpha()

        self.mistakes = 0
        self.time_remaining = 90
        self.correct_stamps = 0

    @staticmethod
    def start_timer() -> None:
        pygame.time.set_timer(UPDATE_TIMER_EVENT, 1000)

    @staticmethod
    def stop_timer() -> None:
        pygame.time.set_timer(UPDATE_TIMER_EVENT, 0)

    def update_timer(self) -> None:
        if self.time_remaining > 0:
            self.time_remaining -= 1
        else:
            self.stop_timer()
            
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))

    def stamp_correct(self) -> None:
        self.correct_stamps += 1

    def stamp_incorrect(self) -> None:
        self.mistakes += 1
        if self.mistakes == 3:
            self.stop_timer()
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the HUD elements on the given surface."""
        surface.blit(self.hud_sprite, (0, 0))
        for i in range(self.mistakes):
            surface.blit(self.error_sprite, (40 + 52 * i, 44))

        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60

        timer_text = FONTS.title.render("Timer", True, WHITE)
        surface.blit(timer_text, (600, 16 - timer_text.get_height() / 2))

        time_text = FONTS.title.render(f"{minutes:02}:{seconds:02}", True, WHITE)
        surface.blit(time_text, (687 - time_text.get_width() / 2, 63 - time_text.get_height() / 2))

        correct_stamps_text = FONTS.title.render(f"{self.correct_stamps}", True, WHITE)
        surface.blit(correct_stamps_text, (190 - correct_stamps_text.get_width(), 16 - correct_stamps_text.get_height() / 2))