import pygame
from constants import *

from graphics_class import Graphics
from interface_class import Interface
from unit_class import unitlist

graphics = Graphics()
interface = Interface()

class Engine(object):
    
    def __init__(self):
        pass
    
    def run(self):
        graphics.draw_background()
        graphics.draw_gameboard()
        graphics.draw_units(unitlist)
        graphics.draw_square_numbers()
        graphics.draw_windows()
        graphics.update()
        interface.run()
