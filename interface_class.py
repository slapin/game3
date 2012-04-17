from constants import *
from engine_class import data
from gameboard import board
from pygame.locals import *
import sys
from unit_class import unitlist
import unit_class

windows = []

class Interface(object):
    
    def __init__(self):
        
        # Windows - This determines the DRAW ORDER in GRAPHICS, FIRST IN - FIRST DRAWN
        self.menu1 = self.create_window(Window, "Menu1", color = DARK_BROWN, visible = False)
        self.bottom = self.create_window(BottomWindow, "Bottom", color = BLACK, font = DEJAVUSANS(20))
        self.debug_window = self.create_window(DebugWindow, "Debug", font=DEJAVUSANS(12), visible = False)
        self.inventory = InventoryWindow("Inventory", rect = get_centered_window_rect((150,150)), color = (40,40,40), visible = False, font = DEJAVUSANS(16))
        windows.append(self.inventory)

        self.resize_windows()
        # End Windows
        
        self.dragging_camera = False
        self.drag_camera_startpos = None
        self.drag_camera_endpos = None
        self.init_offset()
        self.zoom_square = data.selected_square
        
    
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
                    data.debug = toggle_boolvar(data.debug)
                    self.debug_window.visible = data.debug
                    
            if data.focus == "inventory":
                if event.type == KEYDOWN:
                    if event.key == K_i:
                        self.inventory.visible = False
                        data.focus = "normal"
                    
            elif data.focus == "move":
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
                    if event.key == K_i:
                        data.focus = "inventory"
                        self.inventory.visible = True
                    if event.key == K_t: # LET"S TEST SOME JUNK HERE, SONS.
                        unit_class.create_random_unit()
                    if event.key == K_l:
                        data.draw_square_lines = toggle_boolvar(data.draw_square_lines)
                    if event.key == K_MINUS:
                        unit = data.selected_square.unit
                        if unit:
                            cur_i = data.itemlist.index(unit.equipped[0])
                            if cur_i <= 0:
                                unit.equipped = [data.itemlist[-1]]
                            else:
                                unit.equipped = [data.itemlist[cur_i - 1]]
                            print data.itemlist.index(unit.equipped[0]) + 1
                    if event.key == K_EQUALS:
                        unit = data.selected_square.unit
                        if unit:
                            cur_i = data.itemlist.index(unit.equipped[0])
                            if cur_i < len(data.itemlist) - 1:
                                unit.equipped = [data.itemlist[cur_i + 1]]
                            else:
                                unit.equipped = [data.itemlist[0]]
                            print data.itemlist.index(unit.equipped[0]) + 1    
                    if event.key == K_m:
                        if data.selected_square.unit != None:
                            data.focus = "move"
                    if event.key == K_F1:
                        data.end_turn()            
                        
                    if event.key == K_F10:
                        data.focus = "menu1"
                        self.menu1.visible = True
                        
                    if event.key == K_F2:
                        pass
                        
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT: # move data.selected_square with arrow keys
                        if event.key == K_DOWN or event.key == K_RIGHT: inc = 1
                        if event.key == K_UP or event.key == K_LEFT: inc = -1
                        xy = list(data.selected_square.xy)
                        if event.key == K_DOWN or event.key == K_UP: xy[1] += inc
                        if event.key == K_RIGHT or event.key == K_LEFT: xy[0] += inc
                        if 0 <= xy[0] <= (board.board_size[0] - 1):
                            if 0 <= xy[1] <= (board.board_size[1] - 1):
                                data.selected_square = board.get_square(xy)
                                
                    if event.key == K_c:
                        self.center_on_square(data.selected_square)
                        
                    if event.key == K_F3:
                        data.draw_square_numbers = toggle_boolvar(data.draw_square_numbers)
                        
                    if event.key == K_ESCAPE:
                        quit_game()
                    
                        
                #MOUSE
                        
                if event.type == MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        data.selected_square = get_square_under_mouse()
                    
                    if event.button == 3:
                        if data.selected_square.unit != None:
                            data.astar.start_pathfinding(data.selected_square, get_square_under_mouse())
                                
                            
                    if event.button == DRAGBUTTON:
                        self.drag_camera_start()
                        
                        
                    if event.button == 4:
                        self.zoom_in()
                        
                    if event.button == 5:
                        self.zoom_out()
                        
                if event.type == MOUSEBUTTONUP:
                    
                    if event.button == DRAGBUTTON:
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
        
    def zoom_out(self):
        o = data.camera_offset
        x, y = data.graphics.display.get_rect().center
        x -= o[0]
        y -= o[1]
        self.zoom_square = get_square_under_pixel((x, y))
        if data.square_size >= 32:
            data.square_size -= 2 * data.zoom_step
            data.unit_size -= 1 * data.zoom_step
            data.zoom = (data.square_size * 100) / (data.base_square_size)
            self.zoom_center()
    
    def zoom_in(self):
        o = data.camera_offset
        x, y = data.graphics.display.get_rect().center
        x -= o[0]
        y -= o[1]
        self.zoom_square = get_square_under_pixel((x, y))
        if data.square_size < 128:
            data.square_size += 2 * data.zoom_step
            data.unit_size += 1 * data.zoom_step
            data.zoom = (data.square_size * 100) / (data.base_square_size)
            self.zoom_center()
            
    def zoom_center(self):
        self.center_on_square(self.zoom_square)

    def create_window(self, window_type, name="No name", rect = None, color=GREY, pos=(100, 100), visible=True, font=ORBITRON(12)):
        win = window_type(name, rect, color, visible, font)
        windows.append(win)
        return win
  
    def drag_camera_start(self):
        self.old_camera_offset = data.camera_offset[:]
        self.dragging_camera = True
        self.drag_camera_startpos = pygame.mouse.get_pos()

    def drag_camera_end(self):
        self.dragging_camera = False
        self.old_camera_offset = data.camera_offset[:]
    
    def center_on_square(self, square):
        square_rect = square.get_rect()
        disp_rect = data.get_display_rect()
        square_rect.center = disp_rect.center
        square_rect.left -= square.xy[0] * data.square_size
        square_rect.top -= square.xy[1] * data.square_size
        self.old_camera_offset = list(data.camera_offset)        
        data.camera_offset = list(square_rect.topleft)

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
            item_debug = "None"
            if data.selected_square.unit:
                item_debug = "Robe:" + str(data.selected_square.unit.equipped[1].name)

            contents.extend([ ########## DEBUG WINDOW CONTENTS
                            "Focus:" + data.focus,
                            "Board Size:" + str(board.board_size),
                            "Mouse Pos: " + str(pygame.mouse.get_pos()),
                            "FPS: " + str(int(data.fps)),
                            "Selected square: " + str(data.selected_square),
                            robe_debug,
                            "Visible windows: " + str(visible_windows),
                            "Not Visible: " + str(not_visible),
                            "data.camera_offset: " + str(data.camera_offset),
                            "data.zoom: " + str(data.zoom) + "%",
                            "data.square_size: " + str(data.square_size),
                            "graphics.draw() time: " + str(data.graphics.draw_total_time)[:6],
                            "damage results: " + str(len(data.damage))
                            ])
            self.contents = contents
        
class BottomWindow(Window):
    def __init__(self, name, rect, color, visible, font):
        Window.__init__(self, name, rect, color, visible, font)
    
    def update_contents(self):
        self.contents = []
        unit = data.selected_square.unit
        if unit != None:  # BOTTOM WINDOW CONTENTS
            self.contents.extend([unit.name + " - " + unit.faction.name[0].upper() + unit.faction.name[1:],
                                  "Health:  " + str(unit.stats['health']),
                                  "Energy:  " + str(unit.stats['energy']),
                                  "AP:  " + str(unit.stats['ap']) + "/" + str(unit.stats['max ap']),
                                  "Strength: " + str(unit.stats['str']),
                                  "Agility: " + str(unit.stats['agi']),
                                  "Intellect: " + str(unit.stats['int']),
                                  "Attack: " + str(unit.stats['damage']),
                                  "Armor: " + str(unit.stats['armor']),
                                  "M.Resist: " + str(unit.stats['resist'])
                                  ])
        
class InventoryWindow(Window):
    def __init__(self, name, rect, color, visible, font):
        Window.__init__(self, name, rect, color, visible, font)
        
    def update_contents(self):
        self.contents = ["Equipped Items:"]
        if data.selected_square.unit:     
            for item in data.selected_square.unit.equipped:
                line = item.name + "    "
                for k, v in item.stats.items():
                    if k == 'str': k = 'strength'
                    if k == 'int': k = 'intellect'
                    if k == 'agi': l = 'agility'
                    if v >= 0: posneg = "+"
                    if v <0 : posneg = ""
                    line += k[0].upper() + k[1:] + ": " + posneg + str(v) + "  "
                self.contents.append(line)
            
class Menu(Window):
    def __init__(self, name, rect, color, visible, font):
        Window.__init__(self, name, rect, color, visible, font)
    
    def update_contents(self): # MENU1 CONTENTS
        self.contents = ["F1 - exit this menu",
                            "1 - 1024x768",
                            "2 - 1280x800"
                            ]
                           
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
    
def get_square_under_pixel((x,y)):
    x = x / data.square_size
    y = y / data.square_size
    square = board.get_square((x,y))
    if square:
        return square
    else:
        return data.selected_square
    
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

def zoom(number):
    return (number * data.zoom) / 100
        
def quit_game():
    pygame.quit()
    sys.exit()            
