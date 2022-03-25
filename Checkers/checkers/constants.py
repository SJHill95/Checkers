import pygame

# Board dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Colours
RED = (205, 83, 52)
RED_OUTLINE = (218, 130, 108)
BLACK = (46, 40, 42)
CREAM = (237, 184, 139)
BLUE = (23, 190, 187)
WHITE = (233, 236, 239)
WHITE_OUTLINE = (173, 181, 189)

CROWN_RED = pygame.transform.scale(pygame.image.load('assets/crown_red.png'), (40, 40))
CROWN_WHITE = pygame.transform.scale(pygame.image.load('assets/crown_white.png'), (40, 40))
