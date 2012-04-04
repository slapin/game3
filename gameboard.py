from constants import *  
    
class Board(object):
    
    def __init__(self):
        self.grid = []
        for y in range(BOARD_SIZE[1]):
            row = []
            for x in range(BOARD_SIZE[0]):
                row.append(Square((x,y)))
            self.grid.append(row)
                   
class Square(object):
    
    def __init__(self, xy):
        self.xy = xy
        
board = Board()