import pygame
from copy import deepcopy
from random import choice, randrange

# Creating the game Window
width, height = 10, 15  
tile = 45  
game_res = width * tile, height * tile  
res = 750, 940  # Window resolution
FPS = 60

pygame.init()
sc = pygame.display.set_mode(res)  # Main screen
game_sc = pygame.Surface(game_res)  # Game surface (grid area)
clock = pygame.time.Clock()

# Creating the grid structure
grid = [pygame.Rect(x * tile, y * tile, tile, tile) for x in range(width) for y in range(height)]

# Tetris figures positions
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

# Create the figures from positions
figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, tile - 2, tile - 2)
field = [[0 for i in range(width)] for j in range(height)]  # Game field for occupied cells

anim_count, anim_speed, anim_limit = 0, 60, 2000

# Colors for background and game area
bg_color = (0, 0, 0)  # Black background
game_bg_color = (40, 40, 40)  # Dark gray for game area

# Fonts (using default system fonts)
main_font = pygame.font.Font(None, 65)
font = pygame.font.Font(None, 45)

# Titles
title_tetris = main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = font.render('score:', True, pygame.Color('green'))
title_record = font.render('record:', True, pygame.Color('purple'))

# Function to generate random colors for figures
get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}


def check_borders():
    if figure[i].x < 0 or figure[i].x > width - 1:
        return False
    elif figure[i].y > height - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True


def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')


def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))


while True:
    record = get_record()
    dx, rotate = 0, False

    # Fill the main screen and game surface with their background colors
    sc.fill(bg_color)  # Fill the main screen with background color
    game_sc.fill(game_bg_color)  # Fill the game surface with the game area color

    # Delay for full lines
    for i in range(lines):
        pygame.time.wait(200)

# PLAYER MOVEMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True

    # Move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

    # Move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000
                break

    # Rotate figure
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break

    # Check lines
    line, lines = height - 1, 0
    for row in range(height - 1, -1, -1):
        count = 0
        for i in range(width):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < width:
            line -= 1
        else:
            anim_speed += 3
            lines += 1