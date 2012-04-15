from constants import *
from gameboard import board
from engine_class import data
from clothes import *
import random

class Unit(object):
    def __init__(self, name="No Name", square = (4,4), stats = {}):
        self.name = name
        self.square = board.get_square(square)
        self.move_dest = None
        self.move_direction = [0, 0]
        self.move_offset = [0, 0]
        self.step = 0
        self.moving = False
        self.move_route = []
        self.move_index = 0
        self.stats = stats
        self.other_clothes = [ROBE_1, ROBE_2, ROBE_3, ROBE_4, ROBE_5, ROBE_6, ROBE_7,
                               ROBE_8, ROBE_9, ROBE_10, ROBE_11, ROBE_12, ROBE_13, ROBE_14,
                                ROBE_15, ROBE_16, ROBE_17, ROBE_18
                              ]
        self.clothes = [random.choice(self.other_clothes)]
        
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
        MOVESPEED = 1
        if self.step < data.square_size:
            self.move_offset[0] = self.step * self.move_direction[0]
            self.move_offset[1] = self.step * self.move_direction[1]
            self.step += MOVESPEED
            if self.step >= data.square_size:
#                print self.name + " moved to " + str(self.move_dest) + " from " + str(self.square) 
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
        elif self.stats['ap'] >= dest.ap_cost:
            self.stats['ap'] -= dest.ap_cost
            self.moving = True
            self.move_dest = dest
            x = dest.xy[0] - self.square.xy[0]
            y = dest.xy[1] - self.square.xy[1]
            self.move_direction = (x,y)
            self.step = 0
        else:
            print "not enough AP"
            self.move_route = []
            self.move_index = 0
            self.moving = False
            
    def new_turn(self):
        self.ap = self.max_ap
        
def create_unit(name="No Name", square = (0,0),stats = {}):
    unit = Unit(name, square, stats)
    if name != "DUMMY":
        unitlist.append(unit)
        board.get_square(square).unit = unit
        
def create_random_unit():
    global random_unit_number
    random_unit_number += 1
    name = "Random " + str(random_unit_number)
    open_squares = board.get_unblocked_squares()
    for item in open_squares:
        if item.unit != None:
            open_squares.remove(item)
    square = random.choice(open_squares)
    stats = {}
    min, max = 10, 15
    t = ["str", "agi", "int"]
    for item in t:
        stats[item] = random.randint(min, max)
    max_ap = 10
    stats["max ap"] = max_ap
    stats["ap"] = max_ap
    stats["health"] = 30
    stats["energy"] = 20
    stats["armor"] = 1
    stats["deflect"] = 10
    stats["resist"] = 0
    stats["status"] = []
    create_unit(name, square, stats)

unitlist = []
random_unit_number = 0
create_random_unit()

