import pygame
import datetime

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'
LEVEL = 2

def display_data(data: dict, news: pygame.Surface, window: pygame.Surface) -> list:
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

        if chave == "image":
            img = pygame.image.load(valor).convert_alpha()     
            window.blit(img, (width/2 - img.get_width()/2, line_y_offset))
            sections.append(pygame.Rect(width/2 - img.get_width()/2, line_y_offset, width/2 + img.get_width()/2, pos_y + img.get_height()))
            line_y_offset += img.get_height() + news_line_spacing
            break
        
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

def animate_line(news_section: pygame.Rect, game_element: pygame.Rect, window: pygame.Surface):
    start_x, start_y = news_section.center
    end_x, end_y = game_element.center
    steps = 25
    for i in range(steps + 1):
        x = start_x + (end_x - start_x) * i / steps
        y = start_y
        pygame.draw.line(window, (0, 0, 0), (start_x, start_y), (x, y), 3)
        pygame.display.flip()
        pygame.time.delay(20)
        
    for i in range(steps + 1):
        x = end_x
        y = start_y + (end_y - start_y) * i / steps
        pygame.draw.line(window, (0, 0, 0), (x, start_y), (x, y), 3)
        pygame.display.flip()
        pygame.time.delay(20)
    
def player_alasys(news_section: str, game_element: str, window: pygame.Surface, data: dict):
    currentdate = datetime.datetime(2002, 9, 18)
    print(news_section, game_element)
    if news_section == "date" and game_element == "calendar":
        news_date = datetime.datetime.strptime(data["date"], "%d/%m/%Y")
        if news_date > currentdate:
            pygame.display.flip()
            pygame.time.delay(750)
    pygame.draw.line(window, (255, 0, 0), (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 - 20), (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 + 20), 5)
    pygame.draw.line(window, (255, 0, 0), (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 20), (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 + 20), 5)
def main():
    # Inicializa o pygame
    pygame.init()

    # Criação da janela
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)


    clock = pygame.time.Clock()

    # Loop principal do jogo
    running = True

    background = pygame.image.load(r'sprites\background.png').convert()
    table = pygame.image.load(r'sprites\table.png').convert()
    red_stamp = pygame.image.load(r'sprites\red_stamp.png').convert_alpha()
    green_stamp = pygame.image.load(r'sprites\green_stamp.png').convert_alpha()
    calendar = pygame.image.load(r'sprites\calendar.png').convert_alpha()
    news = pygame.image.load(r'sprites\window.png').convert_alpha()
    
    stamps = [pygame.Rect(40, 550, red_stamp.size[0], red_stamp.size[1]), pygame.Rect(WINDOW_WIDTH - 40 - green_stamp.size[0], 550, green_stamp.get_width(), green_stamp.size[1])]
    positions = {"calendar": pygame.Rect(WINDOW_WIDTH/2 + 250, 50, calendar.size[0], calendar.size[1])}
    
        
    data = {
        'date': '18/09/2007',
        'title': 'Bressan Mata 7 pessoas em Jundiaí',
        'author': 'Bressan Hater',
        'paragrafo1': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!',
        'paragrafo2': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Modi impedit voluptatibus saepe ad eum. Mollitia temporibus voluptatibus magni quo fugit, delectus velit libero praesentium, eligendi repellendus nesciunt tempora sequi. Nam!',
        'bibliography': 'Minoru Mineta'
    }
    
    selected_news_section = None
    selected_game_element = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
            window.blit(background, (0, 0))
        
        window.blit(table, (0, 340))
        window.blit(red_stamp, (40, 550))
        window.blit(green_stamp, (WINDOW_WIDTH - 40 - green_stamp.size[0], 550))
        window.blit(calendar, (WINDOW_WIDTH/2 + 250, 50))
        
        if LEVEL > 1:
            author_list = pygame.image.load(r'sprites\author_list.png').convert_alpha()
            window.blit(author_list, (40, 350))


        window.blit(news, ((WINDOW_WIDTH / 2) - news.size[0] / 2, 100))
        news_sections = display_data(data, news, window)


        hovered = False
        mouse_pos = pygame.mouse.get_pos()

        for rect in positions.values():
            if rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                hovered = True
                break

        if not hovered:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        # Verifica cliques nas news_content
        if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo do mouse foi pressionado
            pygame.time.delay(200)
            pos_mouse = pygame.mouse.get_pos()
            for i, section in enumerate(news_sections):
                if section.collidepoint(pos_mouse):
                    print(list(data.keys())[i])
                    selected_news_section = [list(data.keys())[i], section]
                    break
            for i, game_element in positions.items():
                if game_element.collidepoint(pos_mouse):
                    print(i)
                    selected_game_element = [i, game_element]
                    break
            
            if selected_news_section and selected_game_element:
                animate_line(selected_news_section[1], selected_game_element[1], window)
                player_alasys(selected_news_section[0], selected_game_element[0], window, data)
                selected_news_section = None
                selected_game_element = None                
        
        # Atualiza a tela
        pygame.display.flip()
        clock.tick(60)


    # Encerra o pygame
    pygame.quit()




if __name__ == '__main__':
    main()