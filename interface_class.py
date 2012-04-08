import sys
from pygame.locals import *

from constants import *
from engine_class import data
from gameboard import board

windows = []

class Interface(object):
    
    def __init__(self):
        pass
        self.debug = True
        self.debug_window = self.create_debug_window("Debug", size = ((DISPLAY_SIZE[0]) - 100,200), pos = ((50),(DISPLAY_SIZE[1] - 250)), font = DEJAVUSANS12)
        self.dragging_camera = False
        self.drag_camera_startpos = None
        self.drag_camera_endpos = None
        data.camera_offset = self.initialize_offset()
        self.old_camera_offset = self.initialize_offset()
        data.selected_square = board.get_square((0,0))

    
    def run(self):
        self.event_manager()
        for window in windows:
            window.update_contents()
        if self.dragging_camera:
            self.drag_end = pygame.mouse.get_pos()
            self.update_camera_offset()
    
    def event_manager(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            if data.input_mode == "normal":
                if event.type == KEYDOWN:
                    if event.key == K_F1:
                        pass
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT: # move data.selected_square with arrow keys
                        if event.key == K_DOWN or event.key == K_RIGHT: inc = 1
                        if event.key == K_UP or event.key == K_LEFT: inc = -1
                        xy = list(data.selected_square.xy)
                        if event.key == K_DOWN or event.key == K_UP: xy[1] += inc
                        if event.key == K_RIGHT or event.key == K_LEFT: xy[0] += inc
                        if 0 <= xy[0] <= (BOARD_SIZE[0] - 1):
                            if 0 <= xy[1] <= (BOARD_SIZE[1] - 1):
                                data.selected_square = board.get_square(xy)
                    if event.key == K_SPACE:
                        self.center_on_selected_square()
                    if event.key == K_F2:
                        data.draw_square_numbers = toggle_boolvar(data.draw_square_numbers)
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
            if data.input_mode == "menu1":
                pass
                    
    def create_window(self, name = "No name", size = (400,200), color = GREY, pos = (100,100), visible = True, font = ORBITRON12):
        win = Window(name, size, color, pos, visible, font)
        windows.append(win)
        win.interface = self
        return win
    
    def create_debug_window(self, name = "No name", size = (400,200), color = GREY, pos = (100,100), visible = True, font = ORBITRON12):
        debug_win = DebugWindow(name, size, color, pos, visible, font)
        windows.append(debug_win)
        debug_win.interface = self
        return debug_win
  
    def drag_camera_start(self):
        self.dragging_camera = True
        self.drag_camera_startpos = pygame.mouse.get_pos()

    def drag_camera_end(self):
        self.dragging_camera = False
        self.old_camera_offset[0] = data.camera_offset[0]
        self.old_camera_offset[1] = data.camera_offset[1]
        
    def initialize_offset(self): # centers offset
        board_rect = board.get_rect()
        disp_rect = data.get_display_rect()
        board_rect.centerx = disp_rect.centerx
        top,left = board_rect.topleft
        return [top, left]
    
    def center_on_selected_square(self):
        data.selected_square
        square_rect = data.selected_square.get_rect()
        disp_rect = data.get_display_rect()
        square_rect.center = disp_rect.center
        square_rect.left -= data.selected_square.xy[0] * SQUARE_SIZE
        square_rect.top -= data.selected_square.xy[1] * SQUARE_SIZE 
        data.camera_offset = square_rect.topleft

        
    def update_camera_offset(self):
        self.drag_camera_endpos = pygame.mouse.get_pos()
        x = self.drag_camera_endpos[0] - self.drag_camera_startpos[0]
        y = self.drag_camera_endpos[1] - self.drag_camera_startpos[1]
        data.camera_offset[0] = self.old_camera_offset[0] + x
        data.camera_offset[1] = self.old_camera_offset[1] + y
                    
class Window(object):
    """ Should only be created using Graphics.create_window, to make sure it is added to the graphics object .windows list
        therefore, the default arg values are laid out in the create_window func and not here.
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
    
    def add_to_contents(self, str):
        self.contents.append(str)
        
class DebugWindow(Window):
    """ debug window"""
    def __init__(self, name, size, color, pos, visible, font):
        Window.__init__(self, name, size, color, pos, visible, font)
        self.visible = False
        
    def update_contents(self):
        contents = []
        contents.extend([ ########## DEBUG WINDOW CONTENTS
                        "Mouse Pos: " + str(pygame.mouse.get_pos()),
                        "Dragging Cam: " + str(self.interface.dragging_camera),
                        "I.Offset: " + str(data.camera_offset),
                        "Draw square numbers: " + str(data.draw_square_numbers),
                        "FPS: " + str(int(data.fps)),
                        "Selected square:" + str(data.selected_square)
                        ])
        self.contents = contents
                           
def toggle_boolvar(var):
    if var: var = False
    elif not var: var = True
    return var


def quit_game():
    pygame.quit()
    sys.exit()            