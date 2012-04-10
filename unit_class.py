from constants import *
from gameboard import board
from engine_class import data

class Unit(object):
    def __init__(self, name="No Name", square = (4,4), color = BLUE):
        self.name = name
        self.square = board.get_square(square)
        self.color = color
        self.health = 60
        self.energy = 20
        self.speed = 4
        
    def get_rect(self):
        x = self.square[0] * data.square_size
        y = self.square[1] * data.square_size
        square_rect = pygame.rect.Rect(x, y, data.square_size, data.square_size)
        unit_rect = pygame.rect.Rect(x, y, data.unit_size, data.unit_size)
        unit_rect.center = square_rect.center
        return unit_rect
        
def create_unit(name="No Name", square = (0,0), color = WHITE):
    unit = Unit(name, square, color)
    if name != "DUMMY":
        unitlist.append(unit)
        board.get_square(square).unit = unit

unitlist = []
create_unit(name = "Alpha", square = (4, 4), color = GREEN)
create_unit(name = "Beta", square = (6, 1), color = BLUE)

