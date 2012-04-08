import pygame

# Fonts
#fontlist = pygame.font.get_fonts()
#for item in fontlist: print item
def get_font(fontname, size = 20):
    match = pygame.font.match_font(fontname)
    return pygame.font.Font(match, size)
ORBITRON10   = get_font("orbitron", 10)
ORBITRON12   = get_font("orbitron", 12)
ORBITRON20   = get_font("orbitron", 20)
DEJAVUSANS10 = get_font("dejavusans", 10)
DEJAVUSANS12 = get_font("dejavusans", 12)
UBUNTUMONO18 = get_font("ubuntumono", 18)

# Game Board
BOARD_SIZE = (8,8)
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
DARK_BROWN = (30, 20, 0)
LIGHT_TAN = (255, 245, 225)