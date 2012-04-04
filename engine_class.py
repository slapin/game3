import pygame
from constants import *

from graphics_class import Graphics
from interface_class import Interface

graphics = Graphics()
interface = Interface()

class Engine(object):
    
    def __init__(self):
        pass
    
    def run(self):
        graphics.draw_background()
        graphics.draw_gameboard(interface.offset)
        graphics.draw_square_numbers(interface.offset)
        graphics.draw_windows(interface.windows)
        graphics.update(interface.offset)
        interface.run()
