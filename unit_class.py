from constants import *
from gameboard import board
from engine_class import data
import random
import items

class Faction(object):
    def __init__(self, name = "Derp"):
        self.name = name
       
    def __str__(self):
        return self.name
    
friend = Faction('Friend')
enemy = Faction('Enemy')
friend.hostiles = [enemy]
enemy.hostiles = [friend]
data.factions.append(friend)
data.factions.append(enemy)


class Unit(object):
    def __init__(self, name="No Name", faction = data.factions[0], square = (4,4), stats = {}):
        self.name = name
        self.faction = faction
        self.square = board.get_square(square)
        self.move_dest = None
        self.move_direction = [0, 0]
        self.move_offset = [0, 0]
        self.highlight_move = False
        self.step = 0
        self.moving = False
        self.move_route = []
        self.move_index = 0
        self.base_stats = stats
        self.initialize_stats()
        self.stats = self.base_stats
        self.equipped = [
                         random.choice(items.robelist),
                         random.choice(items.weaponlist)
                         ]
        self.recalculate_equipment_bonuses()
        self.backpack = []
        self.square.unit = self
        
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
        if self.stats['health'] <= 0:
            self.square.unit = None
            unitlist.remove(self)
        elif self.move_dest != None:
            MOVESPEED = data.adjust_for_zoom(2)
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
        self.move_route = data.pathfinding_route
        if self.highlight_move == False:
            self.highlight_move = True
        else:
            self.move_index += 1
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
                self.highlight_move = False
        
    
    def move_one_square(self,dest):
        if dest.unit != None:
            if dest.unit.faction in self.faction.hostiles:
                self.attack(dest.unit)
            else:
                print "cannot attack friendly unit."
            
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
            
    def attack(self, unit):
        equipment_bonus = 0
        for item in self.equipped:
            if 'damage' in item.stats.keys():
                equipment_bonus += item.stats['damage']
        damage = 0 + equipment_bonus - unit.stats['armor']
        unit.stats['health'] -= damage
        data.create_damage_result(self, unit, damage)
        self.stats['ap'] = 0
        
    def initialize_stats(self):
        statlist = ['max_ap', 'armor', 'damage', 'strength', 'intellect', 'agility']
        for key in statlist:
            if key not in self.base_stats.keys():
                self.base_stats[key] = 0
        
    def recalculate_equipment_bonuses(self):
        self.stats = self.base_stats
        for item in self.equipped:
            for k,v in item.stats.items():
                self.stats[k] += v
            
    def new_turn(self):
        self.stats['ap'] = self.stats['max ap']
        
def create_unit(name="No Name", faction = data.factions[0], square = (0,0),stats = {}):
    unit = Unit(name, faction, square, stats)
    if name != "DUMMY":
        unitlist.append(unit)
        board.get_square(square).unit = unit
        
def create_random_unit(faction = random.choice(data.factions)):
    global random_unit_number
    random_unit_number += 1
    faction = random.choice(data.factions)
    name = "Random " + str(random_unit_number)
    open_squares = board.get_unblocked_squares()
    for square in open_squares:
        if square.unit != None:
            open_squares.remove(square)
    square = random.choice(open_squares)
    stats = {}
    low, high = 8, 15
    t = ["str", "agi", "int"]
    for item in t:
        stats[item] = random.randint(low, high)
    max_ap = 10
    stats["max ap"] = max_ap
    stats["ap"] = max_ap
    stats["health"] = 3
    stats["energy"] = 20
    stats["armor"] = 1
    stats["deflect"] = 10
    stats["resist"] = 0
    stats["status"] = []
    create_unit(name, faction, square, stats)

unitlist = []
random_unit_number = 0
for i in range(10):
    fac = random.choice(data.factions)
    create_random_unit(fac)

