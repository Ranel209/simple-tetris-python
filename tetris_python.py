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