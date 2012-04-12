from constants import *
from gameboard import board
from engine_class import data

class Unit(object):
    def __init__(self, name="No Name", square = (4,4), color = BLUE):
        self.name = name
        self.square = board.get_square(square)
        self.color = color
        self.move_dest = None
        self.move_direction = [0, 0]
        self.move_offset = [0, 0]
        self.step = 0
        self.health = 60
        self.energy = 20
        self.max_ap = 100
        self.ap = self.max_ap
        self.moving = False
        self.move_route = []
        self.move_index = 0
        
    def get_rect(self):
        x = self.square[0] * data.square_size
        y = self.square[1] * data.square_size
        square_rect = pygame.rect.Rect(x, y, data.square_size, data.square_size)
        unit_rect = pygame.rect.Rect(x, y, data.unit_size, data.unit_size)
        unit_rect.center = square_rect.center
        unit_rect.left += self.move_offset[0]
        unit_rect.top += self.move_offset[1]
        return unit_rect
    
    def update(self):
        MOVESPEED = 4
        if self.step < data.square_size:
            self.move_offset[0] = self.step * self.move_direction[0]
            self.move_offset[1] = self.step * self.move_direction[1]
            self.step += MOVESPEED
            if self.step >= data.square_size:
                print self.name + " moved to " + str(self.move_dest) + " from " + str(self.square) 
                self.square.unit = None
                self.square = self.move_dest
                self.square.unit = self
                data.selected_square = self.move_dest
                self.step = 0
                self.move_dest = None
                self.move_direction = [0, 0]
                self.move_offset = [0, 0]
                self.moving = False
        if len(self.move_route) > 0:
            if self.moving == False:
                self.move_to_target()
            
                
                
    def move_to_target(self):
        self.move_index += 1
        self.move_route = data.pathfinding_route
        if self.square not in self.move_route:
            self.move_one_square(self.move_route[0])
            self.move_index = 0
        elif self.move_index < len(self.move_route):
            self.move_one_square(self.move_route[self.move_index])
        else:
            print "finished"
            self.move_route = []
            self.move_index = 0
            self.moving = False
        
    
    def move_one_square(self,dest):
        if dest.unit != None:
            print "Destination already has a unit in it"
        elif dest.blocked:
            print "Square is blocked"
        else:
            self.moving = True
            self.move_dest = dest
            x = dest.xy[0] - self.square.xy[0]
            y = dest.xy[1] - self.square.xy[1]
            self.move_direction = (x,y)
            self.step = 0
        
def create_unit(name="No Name", square = (0,0), color = WHITE):
    unit = Unit(name, square, color)
    if name != "DUMMY":
        unitlist.append(unit)
        board.get_square(square).unit = unit

unitlist = []
create_unit(name = "Alpha", square = (4, 4), color = GREEN)
create_unit(name = "Beta", square = (6, 1), color = BLUE)
create_unit(name = "Gamma", square = (10, 2), color = RED)

