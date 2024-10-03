import pygame
from copy import deepcopy
from random import choice, randrange

width, height = 10, 15  # Width and Height of the game grid
tile = 45  # Size of a tile
game_res = width * tile, height * tile  # Game surface resolution
res = 750, 940  # Window resolution
FPS = 60

pygame.init()
sc = pygame.display.set_mode(res)  # Main screen
game_sc = pygame.Surface(game_res)  # Game surface (grid area)
clock = pygame.time.Clock()