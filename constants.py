import pygame

# Display Surface
DISPLAY_SIZE = (1024,768)


# Fonts
#fontlist = pygame.font.get_fonts()
#for item in fontlist: print item
font_name = pygame.font.match_font("orbitron")
ORBITRON = pygame.font.Font(font_name, 14)
font_name = pygame.font.match_font("ubuntumono")
UBUNTUMONO = pygame.font.Font(font_name,18)
FONT = pygame.font.Font(None, 18)

# Game Board
BOARD_SIZE = (10,10)
SQUARE_SIZE = 64
UNIT_SIZE = 32

# Colors
BROWN = (120, 75, 25)
AQUA = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (190, 0, 190)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (70, 70, 70)
DARK_GREY = (30, 30, 30)