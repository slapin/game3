import pygame
from constants import *

class Data(object):
    def __init__(self):
        self.draw_square_numbers = True
        self.debug = True
        self.camera_offset = [0,0]
        self.image = pygame.image.load("momo.png")
        
        
data = Data()

from graphics_class import Graphics
from interface_class import Interface
from unit_class import unitlist

graphics = Graphics()
interface = Interface()

class Engine(object):
    
    def __init__(self):
        self.clock = pygame.time.Clock()
    
    def run(self):
        self.clock.tick(60)
        data.fps = self.clock.get_fps()
        graphics.draw_background()
        graphics.draw_gameboard()
        graphics.draw_units(unitlist)
        graphics.draw_square_numbers()
        graphics.draw_selected_square_highlight()
        graphics.draw_windows()
        graphics.update()
        interface.run()
