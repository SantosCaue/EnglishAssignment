from .constants import FONTS, ASSETS_PATH, WHITE
import pygame

UPDATE_TIMER_EVENT = pygame.USEREVENT + 1
GAME_OVER_EVENT = pygame.USEREVENT + 2

class HUD:  
    def __init__(self):
        self.mistakes = 3
        self.time_remaining = 3
        self.correct_stamps = 0
        self.incorrect_stamps = 0

        
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(pygame.image.load(ASSETS_PATH['hud']).convert_alpha(), (0, 0))
        for i in range(self.mistakes):
            surface.blit(pygame.image.load(ASSETS_PATH['error']).convert_alpha(), (40 + 52*(i), 44))
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
    
        surface.blit(FONTS.title.render("Timer", True, WHITE), (600, 16 - FONTS.title.render("Timer", True, WHITE).get_height()/2))      
        time_text = FONTS.title.render(f"{minutes:02}:{seconds:02}", True, WHITE)
        surface.blit(time_text, (687 - time_text.get_width()/2, 63 - time_text.get_height()/2))
        surface.blit(FONTS.title.render(f"{self.correct_stamps}", True, WHITE), (190 - FONTS.title.render(f"{self.correct_stamps}", True, WHITE).get_width(), 16 - FONTS.title.render(f"{self.correct_stamps}", True, WHITE).get_height()/2))
        
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
    
    def start_timer(self) -> None:
        pygame.time.set_timer(UPDATE_TIMER_EVENT, 1000)
    
    def stamp_incorrect(self) -> None:
        self.incorrect_stamps += 1
        self.HP -= 1
        if self.HP == 0:
            self.stop_timer()
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))