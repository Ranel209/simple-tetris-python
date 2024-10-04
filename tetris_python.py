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