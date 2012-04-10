from constants import *
from engine_class import data
from gameboard import board
from pygame.locals import *
import sys


windows = []

class Interface(object):
    
    def __init__(self):
        
        # Windows - This determines the DRAW ORDER in GRAPHICS, FIRST IN - FIRST DRAWN
        self.menu1 = self.create_window(Window, "Menu1", color = DARK_BROWN, visible = False)
        self.bottom = self.create_window(BottomWindow, "Bottom", color = BLACK, font = ORBITRON20)
        self.debug_window = self.create_window(DebugWindow, "Debug", font=DEJAVUSANS12, visible = False)

        self.resize_windows()
        # End Windows
        
        self.dragging_camera = False
        self.drag_camera_startpos = None
        self.drag_camera_endpos = None
        self.init_offset()
        
    
    def resize_windows(self):  # Every window initializes and resets its size(rect) here.
        ds = data.display_size
        self.menu1.rect = get_centered_window_rect((200, 20), (0,get_percent_of_display("y",-20)))
        self.debug_window.rect = get_centered_window_rect((10,10), (0, get_percent_of_display("y",80)))
        self.bottom.rect = pygame.rect.Rect((0,ds[1] - 200),(ds[0],200))

    def init_offset(self): # centers offset
        board_rect = board.get_rect()
        disp_rect = data.get_display_rect()
        board_rect.centerx = disp_rect.centerx
        top, left = board_rect.topleft
        self.old_camera_offset = [top, left]
        data.camera_offset = [top, left]
    
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
            if event.type == KEYDOWN:               
                if event.key == K_d:
                    self.debug_window.visible = toggle_boolvar(self.debug_window.visible)
                    
            if data.focus == "move":
                if event.type == KEYDOWN:
                    if event.key == K_m:
                        data.focus = "normal"
                        
                    if event.key == K_UP:
                        move_unit_one_square("north")
                    if event.key == K_RIGHT:
                        move_unit_one_square("east")
                    if event.key == K_DOWN:
                        move_unit_one_square("south")
                    if event.key == K_LEFT:
                        move_unit_one_square("west")
                    
            elif data.focus == "normal":
                if event.type == KEYDOWN:
                    if event.key == K_t: # LET"S TEST SOME JUNK HERE, SONS.
                        data.astar.start_pathfinding(data.selected_square)
                    if event.key == K_l:
                        data.astar.take_step = True
                    if event.key == K_m:
                        if data.selected_square.unit != None:
                            data.focus = "move"
                    
                    if event.key == K_F1:
                        data.focus = "menu1"
                        self.menu1.visible = True
                        
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT: # move data.selected_square with arrow keys
                        if event.key == K_DOWN or event.key == K_RIGHT: inc = 1
                        if event.key == K_UP or event.key == K_LEFT: inc = -1
                        xy = list(data.selected_square.xy)
                        if event.key == K_DOWN or event.key == K_UP: xy[1] += inc
                        if event.key == K_RIGHT or event.key == K_LEFT: xy[0] += inc
                        if 0 <= xy[0] <= (BOARD_SIZE[0] - 1):
                            if 0 <= xy[1] <= (BOARD_SIZE[1] - 1):
                                select_square(board.get_square(xy))
                                
                    if event.key == K_c:
                        self.center_on_selected_square()
                        
                    if event.key == K_F2:
                        data.draw_square_numbers = toggle_boolvar(data.draw_square_numbers)
                        
                    if event.key == K_ESCAPE:
                        quit_game()
                        
                #MOUSE
                        
                if event.type == MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        select_square(get_square_under_mouse())
                        
                    if event.button == 3:
                        self.drag_camera_start()
                        
                if event.type == MOUSEBUTTONUP:
                    
                    if event.button == 3:
                        self.drag_camera_end()
                        
            elif data.focus == "menu1":
                if event.type == KEYDOWN:
                    
                    if event.key == K_F1:
                        data.focus = "normal"
                        self.menu1.visible = False
                        
                    if event.key == K_1:
                        pygame.display.set_mode((1024, 768))
                        data.display_size = (1024,768)
                        self.resize_windows()
                        
                    if event.key == K_2:
                        pygame.display.set_mode((1280, 800))
                        data.display_size = (1280,800)
                        self.resize_windows()
                    
    def create_window(self, window_type, name="No name", rect = None, color=GREY, pos=(100, 100), visible=True, font=ORBITRON12):
        win = window_type(name, rect, color, visible, font)
        windows.append(win)
        return win
  
    def drag_camera_start(self):
        self.dragging_camera = True
        self.drag_camera_startpos = pygame.mouse.get_pos()

    def drag_camera_end(self):
        self.dragging_camera = False
        self.old_camera_offset[0] = data.camera_offset[0]
        self.old_camera_offset[1] = data.camera_offset[1]
    
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
    def __init__(self, name, rect, color, visible, font):
        self.name = name
        self.color = color
        self.visible = visible
        self.contents = []
        self.font = font
        if rect == None:
            rect = get_centered_window_rect()
        self.rect = rect
        
    def update_contents(self):
        pass
        
class DebugWindow(Window):
    """ debug window"""
    def __init__(self, name, rect, color, visible, font):
        Window.__init__(self, name, rect, color, visible, font)
        
    def update_contents(self):
        if self.visible:
            contents = []
            visible_windows = []
            not_visible = []
            for win in windows:
                if win.visible:
                    visible_windows.append(win.name)
                else:
                    not_visible.append(win.name)

            contents.extend([ ########## DEBUG WINDOW CONTENTS
                            "Focus:" + data.focus,
                            "Mouse Pos: " + str(pygame.mouse.get_pos()),
                            "Dragging Cam: " + str(data.interface.dragging_camera),
                            "I.Offset: " + str(data.camera_offset),
                            "Draw square numbers: " + str(data.draw_square_numbers),
                            "FPS: " + str(int(data.fps)),
                            "Selected square: " + str(data.selected_square),
                            "Visible windows: " + str(visible_windows),
                            "Not Visible: " + str(not_visible),
                            "debug rect: " + str(self.rect),
                            "data.graphics.display_size" + str(data.display_size)
                            ])
            self.contents = contents
        
class BottomWindow(Window):
    def __init__(self, name, rect, color, visible, font):
        Window.__init__(self, name, rect, color, visible, font)
    
    def update_contents(self):
        self.contents = []
        unit = data.selected_square.unit
        if unit != None:  # BOTTOM WINDOW CONTENTS
            self.contents.extend(["Unit name:  " + unit.name,
                                  "Health:  " + str(unit.health),
                                  "Energy:  " + str(unit.energy),
                                  "Speed:  " + str(unit.speed)
                                  ])
        self.contents.extend(["Empty square:  " + str(data.selected_square),
                              "Blocked?: " + str(data.selected_square.blocked),
                              "path_parent: " + str(data.selected_square.path_parent),
                              "path_g: " + str(data.selected_square.path_g),
                              "path_h: " + str(data.selected_square.path_h),
                              "path_f: " + str(data.selected_square.path_f)                              
                              ])
        
        
class Menu(Window):
    def __init__(self, name, rect, color, visible, font):
        Window.__init__(self, name, rect, color, visible, font)
    
    def update_contents(self): # MENU1 CONTENTS
        self.menu1.contents.extend(["F1 - exit this menu",
                            "1 - 1024x768",
                            "2 - 1280x800"
                            ])
                           
def toggle_boolvar(var):
    if var: var = False
    elif not var: var = True
    return var

def get_centered_window_rect(border = (50, 50), (x_offset,y_offset) = (0,0)):
        d_rect = data.get_display_rect()
        height = d_rect.height - (border[1] * 2)
        width = d_rect.width - (border[0] * 2)
        w_rect = pygame.rect.Rect(0, 0, width, height)
        w_rect.center = d_rect.center
        w_rect.top += y_offset
        w_rect.left += x_offset
        w_rect = w_rect.clip(d_rect)
        return w_rect 
    
def get_percent_of_display(axis, percent):
    if axis == "x":
        x = (data.display_size[0] * percent) / 100
        return x
    if axis == "y":
        y = (data.display_size[1] * percent) / 100
        return y

def get_square_under_mouse():
    result = None
    for row in board.grid:
        for square in row:
            if square.get_rect().collidepoint(pygame.mouse.get_pos()):
                result = square
    if result == None:
        return data.selected_square
    else:
        return result

def select_square(square):
    data.selected_square = square
    
def move_unit_one_square(direction):
    if direction == 'north': mod = (0,-1)
    if direction == 'east': mod = (1, 0)
    if direction == 'south': mod = (0, 1)
    if direction == 'west': mod = (-1, 0)
    if data.selected_square.unit != None:
        unit = data.selected_square.unit
        x,y = unit.square.xy
        x += mod[0]
        y += mod[1]
        new_square = board.get_square((x,y))
        if new_square != None:
            relocate_unit(unit, new_square)
            data.selected_square = new_square
        else:
            print "You cannot move off the board."
            
def relocate_unit(unit, dest):
    unit.square.unit = None
    unit.square = dest
    unit.square.unit = unit
    
         

def quit_game():
    pygame.quit()
    sys.exit()            
