import pygame


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'


def display_data(data, news, window):
    width = window.get_width()
    font = pygame.font.Font(None, 12)
    line_y_offset = 120
    news_line_spacing = 15

    sections = []
    for chave, valor in data.items():
        text = f'{chave}: {valor}'
        words = text.split()
        current_line = ''
        pos_x = (width / 2) - news.get_width() / 2 + 10
        max_text_width = news.get_width() - 20  # Margem dentro da folha
        pos_y = line_y_offset  # Guarda a posição inicial da caixa
        section_width = 0  # Largura máxima da caixa
        section_height = 0  # Altura acumulada da caixa

        for word in words:
            if font.size(current_line + word + " ")[0] > max_text_width:
                rendered = font.render(current_line, True, (0, 0, 0))
                window.blit(rendered, (pos_x, line_y_offset))
                section_width = max(section_width, rendered.get_width())
                section_height += rendered.get_height()
                line_y_offset += news_line_spacing
                section_height += news_line_spacing
                current_line = f'{word} '
                break
                
            if chave == 'date':
                pos_x = width/2 + 100
                
            current_line += f'{word} '

        if current_line:  # Renderiza a última linha
            rendered = font.render(current_line, True, (0, 0, 0))
            window.blit(rendered, (pos_x, line_y_offset))
            section_width = max(section_width, rendered.get_width())
            section_height = rendered.get_height() if section_height == 0 else section_height - news_line_spacing
            line_y_offset += news_line_spacing
            
        # Cria uma única caixa para todo o valor
        sections.append(pygame.Rect(pos_x, pos_y, section_width, section_height))
    return sections


def main():
    # Inicializa o pygame
    pygame.init()

    # Criação da janela
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    # Loop principal do jogo
    running = True

    background = pygame.image.load(r'sprites\background.png').convert()
    table = pygame.image.load(r'sprites\table.png').convert()
    window.blit(background, (0, 0))
    window.blit(table, (0, 340))

    data = {
        'date': '18/09/2007',
        'title': 'Bressan Mata 7 pessoas em Jundiaí',
        'author': 'Bressan Hater',
        'paragrafo1': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!',
        'paragrafo2': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!',
        'bibliography': 'Minoru Mineta'
    }

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        news = pygame.image.load(r'sprites\window.png').convert_alpha()

        window.blit(news, ((WINDOW_WIDTH / 2) - news.size[0] / 2, 100))
        news_sections = display_data(data, news, window)

        # Verifica cliques nas news_content
        if pygame.mouse.get_pressed()[0]: # Verifica se o botão esquerdo do mouse foi pressionado
            pos_mouse = pygame.mouse.get_pos()
            for i, section in enumerate(news_sections):
                if section.collidepoint(pos_mouse):
                    print(f'Clicou na caixa: {list(data.keys())[i]}')

        # Atualiza a tela
        pygame.display.flip()

    # Encerra o pygame
    pygame.quit()

if __name__ == '__main__':
    main()