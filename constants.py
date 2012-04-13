import pygame

# Fonts
#fontlist = pygame.font.get_fonts()
#for item in fontlist: print item
def get_font(fontname, size = 20):
    match = pygame.font.match_font(fontname)
    return pygame.font.Font(match, size)

def ORBITRON(size):
    return get_font("orbitron", size)

def DEJAVUSANS(size):
    return get_font("dejavusans", size)

def UBUNTUMONO(size):
    return get_font("ubuntumono", size)

def UBUNTUCONDENSED(size):
    return get_font("ubuntucondensed", size)

FONT = DEJAVUSANS(10)

#for graphics alpha color
DC_ALPHA = (71, 108, 108)

# CLICK AND DRAG CAMERA MOUSE BUTTON
DRAGBUTTON = 2

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