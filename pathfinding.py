from engine_class import data
from gameboard import board
import time

class AStar():
    def __init__(self):
        pass
    
    def find_path(self, start, goal):
        self.start_time = time.time()
        self.start = start
        self.goal = goal
        self.open = []
        self.closed = board.get_blocked_squares()
        self.route = []
        square = self.start
        c = 0
        while square != self.goal:
            square = self.continue_path(square) 
            c += 1
            if square == self.goal:
                self.finish_time = time.time() - self.start_time
                print "GOAL reached, steps: " + str(c) + "  Time: " + str(self.finish_time)
        data.pathfinding_route = self.route
        self.finish_pathfinding()
        
    def continue_path(self, this_square):
        self.route.append(this_square)
        self.closed.append(this_square)
        adj_list = self.get_adjacent_squares(this_square)
        self.open = []
        for adj_square in adj_list:
            if adj_square not in self.open:
                self.open.append(adj_square)
        for square in self.open:
            square.path_g = self.get_square_to_square_dist(self.start, square)
        f_list = []
        for square in self.open:
            square.path_h = self.get_square_to_square_dist(square, self.goal)
            square.path_f = square.path_g + square.path_h
            if square not in self.closed:
                f_list.append([square.path_f, square])
        f_list.sort()
        if len(f_list) < 1:
            print "f_list is empty, cannot continue."
            for item in self.route: print item
        else:
            next_square = f_list[0][1]
            return next_square
        
    def get_adjacent_squares(self, square):
        x,y = square.xy
        north = board.get_square((x,y-1))
        east = board.get_square((x+1, y))
        south = board.get_square((x, y+1))
        west = board.get_square((x-1, y))
        results = []
        for sq in [north, east, south, west]:
            if sq != None:
                results.append(sq)
        return results
    
    def get_square_to_square_dist(self, square1, square2):
        x1, y1 = square1.xy
        x2, y2 = square2.xy
        dist = abs(x1 - x2)
        dist += abs(y1 - y2)
        return dist
    
    def get_g_score(self, square):
        score = 0
        while self.path_parent != None:
            score += self.get_square_to_square_dist(square, square.path_parent)
        return score
        
    def finish_pathfinding(self):
        for row in board.grid:
            for square in row:
                square.path_parent = None
  
astar = AStar()
