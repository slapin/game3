from constants import *
from engine_class import data  
    
class Board(object):
    """ map board object """
    def __init__(self):
        self.BOARD_SIZE = BOARD_SIZE
        self.grid = []
        self.blocked_squares = []
        self.create_grid()
        self.block_list = []
        self.load_map("testmap.map")
        for xy in self.block_list:
            self.block_square(xy)
        self.update_blocked_square_list()
            
    def get_square(self, (x,y)):
        if 0 <= x < BOARD_SIZE[0] and 0 <= y < BOARD_SIZE[1]:
            square = self.grid[y][x]
            return square            
    
    def get_rect(self):
        width = BOARD_SIZE[0] * SQUARE_SIZE
        height = BOARD_SIZE[1] * SQUARE_SIZE
        return pygame.rect.Rect(0, 0, width, height)
    
    def create_grid(self):
        for y in range(BOARD_SIZE[1]):
            row = []
            for x in range(BOARD_SIZE[0]):
                row.append(Square((x,y)))
            self.grid.append(row)
    
    def update_blocked_square_list(self):
        self.blocked = []
        for row in self.grid:
            for square in row:
                if square.blocked:
                    self.blocked_squares.append(square)
                    
    def get_blocked_squares(self):
        blocklist = []
        for row in self.grid:
            for square in row:
                if square.blocked:
                    blocklist.append(square)
        return blocklist
    
    def block_square(self, (x, y)):
        square = self.get_square((x, y))
        square.blocked = True
        
    def load_map(self, file):
        f = open(file)
        x,y = 0,0
        for row in f:
            x = 0
            for square in row:
                if square == '#':
                    self.get_square((x,y)).blocked = True
                x += 1
            y += 1
                    
        
        f.close()
    
class Square(object):
    """ map square object """
    def __init__(self, xy):
        self.xy = xy
        self.unit = None
        self.blocked = False
        self.path_parent = None
        self.path_g = None
        self.path_h = None
        self.path_f = None
        
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