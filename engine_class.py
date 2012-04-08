import pygame
from constants import *

class Data(object):
    def __init__(self):
        self.draw_square_numbers = True
        self.focus = "normal"
        self.display_size = (1280, 800)
        
    def get_display_rect(self):
        return pygame.rect.Rect((0, 0), self.display_size) 

     

data = Data()

from graphics_class import Graphics
from interface_class import Interface
from unit_class import unitlist
from gameboard import board
data.selected_square = board.get_square((0, 0))

graphics = Graphics()
interface = Interface()
data.interface = interface
data.graphics = graphics



class Engine(object):
    
    def __init__(self):
        self.clock = pygame.time.Clock()
    
    def run(self):
        self.clock.tick(60)
        data.fps = self.clock.get_fps()
        graphics.draw()
        interface.run()
