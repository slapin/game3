import pygame, sys, gameboard
from pygame.locals import *

from constants import *

class Interface(object):
    
    def __init__(self):
        pass
        self.debug = True
        self.windows = []
        self.debug_window = self.create_debug_window("Debug", size = ((DISPLAY_SIZE[0]) - 100,200), pos = ((50),(DISPLAY_SIZE[1] - 250)), font = UBUNTUMONO)
    
    def run(self):
        self.input()
        for window in self.windows:
            window.update_contents()
    
    def input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game()
                if event.key == K_d:
                    self.debug_window.visible = toggle_boolvar(self.debug_window.visible)
                    
    def create_window(self, name = "No name", size = (400,200), color = GREY, pos = (100,100), visible = True, font = ORBITRON):
        win = Window(name, size, color, pos, visible, font)
        self.windows.append(win)
        return win
    
    def create_debug_window(self, name = "No name", size = (400,200), color = GREY, pos = (100,100), visible = True, font = ORBITRON):
      debug_win = DebugWindow(name, size, color, pos, visible, font)
      self.windows.append(debug_win)
      return debug_win
                    
class Window(object):
    """ Should only be created using Graphics.create_window, to make sure it is added to the graphics object .windows list
        therefore, the defualt arg values are laid out in the create_window func and not here.
    """
    def __init__(self, name, size, color, pos, visible, font):
        self.name = name
        self.size = size
        self.color = color
        self.pos = pos
        self.visible = visible
        self.contents = []
        self.font = font
        
    def update_contents(self):
        pass
        
class DebugWindow(Window):
    """ debug window"""
    def __init__(self, name, size, color, pos, visible, font):
        Window.__init__(self, name, size, color, pos, visible, font)
        
    def update_contents(self):
        contents = []
        contents.extend([
                        "Mouse Pos: " + str(pygame.mouse.get_pos())
                        ])
        self.contents = contents

                           
def toggle_boolvar(var):
    if var: var = False
    elif not var: var = True
    return var

def quit_game():
    pygame.quit()
    sys.exit()            