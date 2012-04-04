import pygame, sys
from pygame.locals import *

from constants import *

class Interface(object):
    
    def __init__(self):
        pass
        self.debug = True
        self.windows = []
        self.debug_window = self.create_debug_window("Debug", size = ((DISPLAY_SIZE[0]) - 100,200), pos = ((50),(DISPLAY_SIZE[1] - 250)), font = UBUNTUMONO)
        self.old_offset = [0,0]
        self.offset = [0,0]
        self.dragging_camera = False
        self.drag_start = None
        self.drag_end = None
    
    def run(self):
        self.input()
        for window in self.windows:
            window.update_contents()
        if self.dragging_camera:
            self.drag_end = pygame.mouse.get_pos()
            self.update_camera_offset()
    
    def input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game()
                if event.key == K_d:
                    self.debug_window.visible = toggle_boolvar(self.debug_window.visible)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.drag_camera_start()
            if event.type == MOUSEBUTTONUP:
                if event.button == 3:
                    self.drag_camera_end()
                    
    def create_window(self, name = "No name", size = (400,200), color = GREY, pos = (100,100), visible = True, font = ORBITRON):
        win = Window(name, size, color, pos, visible, font)
        self.windows.append(win)
        win.interface = self
        return win
    
    def create_debug_window(self, name = "No name", size = (400,200), color = GREY, pos = (100,100), visible = True, font = ORBITRON):
        debug_win = DebugWindow(name, size, color, pos, visible, font)
        self.windows.append(debug_win)
        debug_win.interface = self
        return debug_win
  
    def drag_camera_start(self):
        self.dragging_camera = True
        self.drag_start = pygame.mouse.get_pos()

    def drag_camera_end(self):
        self.dragging_camera = False
        self.old_offset[0] = self.offset[0]
        self.old_offset[1] = self.offset[1]
    
    def update_camera_offset(self):
        x = self.drag_end[0] - self.drag_start[0]
        y = self.drag_end[1] - self.drag_start[1]
        self.offset[0] = self.old_offset[0] + x
        self.offset[1] = self.old_offset[1] + y
                    
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
                        "Mouse Pos: " + str(pygame.mouse.get_pos()),
                        "Dragging Cam: " + str(self.interface.dragging_camera),
                        "I.Offset: " + str(self.interface.offset)
                        ])
        self.contents = contents

                           
def toggle_boolvar(var):
    if var: var = False
    elif not var: var = True
    return var

def quit_game():
    pygame.quit()
    sys.exit()            