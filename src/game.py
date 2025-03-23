import pygame

LARGURA, ALTURA = 800, 640
TITULO = "Minha Janela com Pygame-CE"

def __main__():
# Inicializa o pygame
    pygame.init()

    # Configurações da janela
    largura, altura = LARGURA, ALTURA
    titulo = TITULO
    cor_fundo = (0, 0, 0)  # Preto

    # Criação da janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption(titulo)

    # Loop principal do jogo
    rodando = True

    CENARIO = pygame.image.load("src/sprites/cenario.png").convert()
    MESA = pygame.image.load("src/sprites/mesa.png") .convert()
    tela.blit(CENARIO, (0, 0))
    tela.blit(MESA, (0, 340))   

    DADOS = {"data": "18/09/2007", "titulo":"Bressan Mata 7 pessoas em Jundiaí", "autor": "Bressan Hater", "paragrafo1": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!", "paragrafo2": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!", "bibliografia": "Minoru Mineta"}

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        folha = pygame.image.load("src/sprites/folha.png").convert_alpha()
        
        tela.blit(folha, ((largura/2)-folha.size[0]/2, 100))
        caixas = displayData(DADOS, folha, tela)

        # Verifica cliques nas caixas
        if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo do mouse foi pressionado
            pos_mouse = pygame.mouse.get_pos()
            for i, caixa in enumerate(caixas):
                if caixa.collidepoint(pos_mouse):
                    print(f"Clicou na caixa: {list(DADOS.keys())[i]}")
        
        # Atualiza a tela
        pygame.display.flip()


    # Encerra o pygame
    pygame.quit()

def displayData(data, folha, tela):
    largura = tela.get_width()
    fonte = pygame.font.Font(None, 12)
    y_offset = 120 
    espaco = 15
    caixas = []
    for chave, valor in data.items():
        texto = f"{chave}: {valor}"
        palavras = texto.split()
        linha_atual = ""
        pos_x = (largura / 2) - folha.get_width() / 2 + 10
        largura_maxima = folha.get_width() - 20  # Margem dentro da folha
        caixa_inicio_y = y_offset  # Guarda a posição inicial da caixa
        largura_caixa = 0  # Largura máxima da caixa
        altura_caixa = 0  # Altura acumulada da caixa

        for palavra in palavras:
            if fonte.size(linha_atual + palavra + " ")[0] > largura_maxima:
                renderizado = fonte.render(linha_atual, True, (0, 0, 0)) 
                tela.blit(renderizado, (pos_x, y_offset))
                largura_caixa = max(largura_caixa, renderizado.get_width())
                altura_caixa += renderizado.get_height()
                y_offset += espaco
                altura_caixa += espaco
                linha_atual = palavra + " "
                
            else:
                if chave == "data":
                    pos_x = largura/2 + 100
                linha_atual += palavra + " "

        if linha_atual:  # Renderiza a última linha
            renderizado = fonte.render(linha_atual, True, (0, 0, 0))
            tela.blit(renderizado, (pos_x, y_offset))
            largura_caixa = max(largura_caixa, renderizado.get_width())
            altura_caixa = renderizado.get_height() if altura_caixa == 0 else altura_caixa - espaco
            y_offset += espaco
            
        # Cria uma única caixa para todo o valor
        caixas.append(pygame.Rect(pos_x, caixa_inicio_y, largura_caixa, altura_caixa))
    return caixas    

__main__()