from constants import *
from engine_class import data  
    
class Board(object):
    """ map board object """
    def __init__(self):
        self.BOARD_SIZE = BOARD_SIZE
        self.grid = []
        for y in range(BOARD_SIZE[1]):
            row = []
            for x in range(BOARD_SIZE[0]):
                row.append(Square((x,y)))
            self.grid.append(row)
            
    def get_square(self, (x,y)):
        if 0 <= x < BOARD_SIZE[0] and 0 <= y < BOARD_SIZE[1]:
            square = self.grid[y][x]
            return square
            
    
    def get_rect(self):
        width = BOARD_SIZE[0] * SQUARE_SIZE
        height = BOARD_SIZE[1] * SQUARE_SIZE
        return pygame.rect.Rect(0, 0, width, height)
                   
class Square(object):
    """ map square object """
    def __init__(self, xy):
        self.xy = xy
        self.unit = None
        
    def __str__(self):
        return str(self.xy)
    
    def __getitem__(self, index):
        return self.xy[index]
    
    def get_rect(self):
        left = self.xy[0] * SQUARE_SIZE + data.camera_offset[0]
        top = self.xy[1] * SQUARE_SIZE + data.camera_offset[1]
        width = SQUARE_SIZE
        height = SQUARE_SIZE
        return pygame.rect.Rect(left, top, width, height)
    
board = Board()