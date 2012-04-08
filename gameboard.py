from constants import *  
    
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
        return self.grid[y][x]
                   
class Square(object):
    """ map square object """
    def __init__(self, xy):
        self.xy = xy
        
    def __str__(self):
        return " Square: " + str(self.xy)
    
board = Board()