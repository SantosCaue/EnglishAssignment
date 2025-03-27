from .constants import FONTS, ASSETS_PATH, WHITE
import pygame

UPDATE_TIMER_EVENT = pygame.USEREVENT + 1
GAME_OVER_EVENT = pygame.USEREVENT + 2

class HUD:
    def __init__(self):
        self.HP = 3
        self.time_remaining = 90
        self.correct_stamps = 0
        self.incorrect_stamps = 0
        pygame.time.set_timer(UPDATE_TIMER_EVENT, 1000)
        
    def draw(self, surface: pygame.Surface) -> None:
        for i in range(self.HP):
            surface.blit(pygame.image.load(ASSETS_PATH['heart']).convert_alpha(), (10 + 60*(i), 70))
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        surface.blit(FONTS.medium.render(f"Time: {minutes:02}:{seconds:02}", True, WHITE), ( surface.get_width()- FONTS.medium.render(f"Time: {minutes:02}:{seconds:02}", True, WHITE).get_width() - 10, 10))
        surface.blit(FONTS.medium.render(f"Stamps: {self.correct_stamps}", True, WHITE), (10, 10))
        
    def update_timer(self) -> None:
        if self.time_remaining > 0:
            self.time_remaining -= 1
        else:
            self.stop_timer()
            
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))  
        
    def stop_timer(self) -> None:
        pygame.time.set_timer(UPDATE_TIMER_EVENT, 0)
        
    def stamp_correct(self) -> None:
        self.correct_stamps += 1
    
    def stamp_incorrect(self) -> None:
        self.incorrect_stamps += 1
        self.HP -= 1
        if self.HP == 0:
            self.stop_timer()
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))