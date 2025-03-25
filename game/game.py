import pygame
import datetime
import math

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
WINDOW_TITLE = 'News Please'
LEVEL = 99


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
            window.blit(img, (width / 2 - img.get_width() / 2, line_y_offset))
            sections.append(pygame.Rect(width / 2 - img.get_width() / 2, line_y_offset, width / 2 + img.get_width() / 2,
                                        pos_y + img.get_height()))
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
                pos_x = width / 2 + 100

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

    steps = math.ceil(0.1 * abs(end_x - start_x))
    for i in range(steps + 1):
        x = start_x + (end_x - start_x) * i / steps
        y = start_y
        pygame.draw.line(window, (0, 0, 0), (start_x, start_y), (x, y), 3)
        pygame.display.flip()
        pygame.time.delay(20)

    steps = math.ceil(0.05 * abs(end_y - start_y))
    for i in range(steps + 1):
        x = end_x
        y = start_y + (end_y - start_y) * i / steps
        pygame.draw.line(window, (0, 0, 0), (x, start_y), (x, y), 3)
        pygame.display.flip()
        pygame.time.delay(20)


def player_analysis(news_section: str, game_element: str, window: pygame.Surface, data: dict) -> bool:
    trusted_sources = ["Minoru Mineta", "Bressan Hater", "Bressan Fan"]
    banned_authors = ["Bressan Hater", "Bressan Fan"]
    currentdate = datetime.datetime(2018, 9, 18)

    if news_section == "date" and game_element == "calendar":  # Erro de data
        news_date = datetime.datetime.strptime(data["date"], "%d/%m/%Y")
        if news_date > currentdate:
            pygame.display.flip()
            pygame.time.delay(750)
            return True
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2),
                         (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20), 5)
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
                         (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 10), 5)
        pygame.display.flip()
        pygame.time.delay(750)
        return False

    if news_section == "news" and game_element == "format_table":  # Erro de formatação
        if data.items.length() != 6 and data.items().__contains__("image") or data.items().length() != 7:
            pygame.display.flip()
            pygame.time.delay(750)
            return True
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2),
                         (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20), 5)
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
                         (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 10), 5)
        pygame.display.flip()
        pygame.time.delay(750)
        return False

    if news_section == "author" and game_element == "author_list":  # Erro de authoe
        if data["author"] in banned_authors:
            pygame.display.flip()
            pygame.time.delay(750)
            return True
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2),
                         (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20), 5)
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
                         (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 10), 5)
        pygame.display.flip()
        pygame.time.delay(750)
        return False

    if news_section == "bibliography" and game_element == "sources_list":  # Erro de bibliografia
        if data["bibliography"] not in trusted_sources:
            pygame.display.flip()
            pygame.time.delay(750)
            return True
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2),
                         (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20), 5)
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
                         (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 10), 5)
        pygame.display.flip()
        pygame.time.delay(750)
        return False

    if news_section == "image" and game_element == "magnifying_glass":  # Erro de imagem
        if data["image"][:2] == "AI":
            pygame.display.flip()
            pygame.time.delay(750)
            return True
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2),
                         (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20), 5)
        pygame.draw.line(window, (0, 255, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
                         (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 10), 5)
        pygame.display.flip()
        pygame.time.delay(750)
        return False

    pygame.draw.line(window, (255, 0, 0), (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 - 20),
                     (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 + 20), 5)
    pygame.draw.line(window, (255, 0, 0), (WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT // 2 - 20),
                     (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 + 20), 5)
    pygame.display.flip()
    pygame.time.delay(500)
    return False


def onclick(news_sections: list, positions: dict, selected_news_section: list, selected_game_element: list,
            window: pygame.Surface, data: dict) -> tuple[pygame.Rect, pygame.Rect]:
    pos_mouse = pygame.mouse.get_pos()
    pygame.time.delay(200)
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
        print(selected_game_element[0], selected_news_section[0])
        animate_line(selected_news_section[1], selected_game_element[1], window)
        player_analysis(selected_news_section[0], selected_game_element[0], window, data)
        selected_news_section = None
        selected_game_element = None

    return selected_news_section, selected_game_element


def get_data() -> list[dict]:
    # TODO: Implementar a leitura de um arquivo JSON
    raise NotImplementedError()


def main():
    # Inicializa o pygame
    pygame.init()

    # Criação da janela
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()

    # Loop principal do jogo
    running = True

    background = pygame.image.load(r'../sprites\background.png').convert()
    table = pygame.image.load(r'sprites\table.png').convert()
    red_stamp = pygame.image.load(r'sprites\red_stamp.png').convert_alpha()
    green_stamp = pygame.image.load(r'sprites\green_stamp.png').convert_alpha()
    calendar = pygame.image.load(r'sprites\calendar.png').convert_alpha()
    news = pygame.image.load(r'sprites\window.png').convert_alpha()

    positions = {"calendar": pygame.Rect(WINDOW_WIDTH / 2 + 250, 50, calendar.size[0], calendar.size[1])}
    fake_news = False
    health_points = 3
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
            window.blit(background, (0, 0))

        window.blit(table, (0, 340))
        window.blit(red_stamp, (40, 550))
        window.blit(green_stamp, (WINDOW_WIDTH - 40 - green_stamp.size[0], 550))
        window.blit(calendar, (WINDOW_WIDTH / 2 + 250, 50))
        window.blit(news, ((WINDOW_WIDTH / 2) - news.size[0] / 2, 100))
        news_sections = display_data(data, news, window)

        if LEVEL > 1:
            author_list = pygame.image.load(r'sprites\author_list.png').convert_alpha()
            window.blit(author_list, (40, 350))
            positions["author_list"] = pygame.Rect(40, 350, author_list.size[0], author_list.size[1])
        if LEVEL > 2:
            magnifying_glass = pygame.image.load(r'sprites\magnifying_glass.png').convert_alpha()
            window.blit(magnifying_glass, ((WINDOW_WIDTH - magnifying_glass.width) / 2, 550))
            positions["magnifying_glass"] = pygame.Rect((WINDOW_WIDTH - magnifying_glass.width) / 2, 550,
                                                        magnifying_glass.width, magnifying_glass.height)

        if LEVEL > 3:
            sources_list = pygame.image.load(r'sprites\sources_list.png').convert_alpha()
            window.blit(sources_list, (WINDOW_WIDTH - 40 - sources_list.width, 350))
            positions["sources_list"] = pygame.Rect(WINDOW_WIDTH - 40 - sources_list.width, 350, sources_list.width,
                                                    sources_list.height)

        hovered = False
        mouse_pos = pygame.mouse.get_pos()

        for rect in positions.values():
            if rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                hovered = True
                break

        if not hovered:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        if pygame.mouse.get_pressed()[0]:
            selected_news_section, selected_game_element = onclick(news_sections, positions, selected_news_section,
                                                                   selected_game_element, window, data)

            # Atualiza a tela
        pygame.display.flip()
        clock.tick(60)

    # Encerra o pygame
    pygame.quit()


if __name__ == '__main__':
    main()