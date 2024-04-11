import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0
active_color = 'white'
figure_size = 20  # Default figure size

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []


def draw_menu(color):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    brush_list = [circle_brush, rect_brush]

    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    eraser = pygame.Surface((25, 25))
    eraser.fill((255, 255, 255))
    pygame.draw.rect(eraser, 'black', [0, 0, 25, 25], 3)
    screen.blit(eraser, [WIDTH - 150, 7, 25, 25])

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    plus_button = pygame.draw.rect(screen, 'black', [10, 90, 20, 20])  # Plus button
    minus_button = pygame.draw.rect(screen, 'black', [40, 90, 20, 20])  # Minus button
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser.get_rect(topleft=(WIDTH - 150, 7))]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list, plus_button, minus_button


def draw_painting(paints):
    for color, pos, figure, size in paints:
        if color == (255, 255, 255):
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, size, 2)
            elif figure == 1:
                pygame.draw.rect(screen, color, [pos[0] - size, pos[1] - size, size * 2, size * 2], 2)


run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs, plus_button, minus_button = draw_menu(active_color)

    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure, figure_size))
    draw_painting(painting)

    if mouse[1] > 85:
        if active_color == (255, 255, 255):
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20])
        else:
            if active_figure == 0:
                pygame.draw.circle(screen, active_color, mouse, figure_size, 2)
            elif active_figure == 1:
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

            if plus_button.collidepoint(event.pos):  # Plus button clicked
                figure_size += 5
            elif minus_button.collidepoint(event.pos):  # Minus button clicked
                figure_size = max(5, figure_size - 5)

    pygame.display.flip()

pygame.quit()
