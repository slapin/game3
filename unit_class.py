from constants import *

class Unit(object):
    def __init__(self, name="No Name", square = (4,4), color = BLUE):
        self.name = name
        self.square = square
        self.color = color
        
    def get_rect(self):
        x = self.square[0] * SQUARE_SIZE
        y = self.square[1] * SQUARE_SIZE
        square_rect = pygame.rect.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        unit_rect = pygame.rect.Rect(x, y, UNIT_SIZE, UNIT_SIZE)
        unit_rect.center = square_rect.center
        return unit_rect
        
def create_unit(name="No Name", square = (4,4), color = BLUE):
    unitlist.append(Unit(name, square, color = GREEN))

unitlist = []
create_unit()    