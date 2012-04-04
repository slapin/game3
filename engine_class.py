import pygame, time
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
        start = time.time()
        graphics.draw_gameboard()
        print "squares: " + str(time.time() - start)
        start = time.time()
        graphics.dg2()
        print "lines: " + str(time.time() - start)
        graphics.draw_windows(interface.windows)
        graphics.update()
        interface.run()
