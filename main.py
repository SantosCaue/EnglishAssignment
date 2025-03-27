import pygame
import os
from game.game_state import GameState

def main():
    # Inicializa o Pygame
    pygame.init()

    # Carrega a imagem do ícone
    icon_path = os.path.join('assets', 'sprites', 'logo_icon.png')
    icon_image = pygame.image.load(icon_path)

    # Define a imagem como ícone do jogo
    pygame.display.set_icon(icon_image)

    # Cria a instância do jogo
    game = GameState()
    game.run()

if __name__ == '__main__':
    main()