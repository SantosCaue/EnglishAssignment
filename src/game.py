import pygame

# Inicializa o pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
titulo = "Minha Janela com Pygame-CE"
cor_fundo = (0, 0, 0)  # Preto

# Criação da janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o pygame
pygame.quit()