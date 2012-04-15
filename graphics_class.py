import pygame, time, os
from pygame.locals import *

from constants import *
from interface_class import windows
from unit_class import unitlist
from engine_class import data
from gameboard import board

class Graphics(object):
    
    def __init__(self):
        self.display = pygame.display.set_mode(data.display_size)
        self.DIRTFLOOR = pygame.image.load(os.path.join("./art/brown_dirt.png")).convert()
        self.STONEWALL = pygame.image.load(os.path.join("./art/grey_wall.png")).convert()
        self.HUMAN = pygame.image.load(os.path.join("./art/dc-pl.png")).convert()
                        
    def draw(self):
        self.draw_start_time = time.time()
        self.draw_background()
        self.draw_square_images()
        self.draw_gameboard()
        self.draw_units()
        self.draw_square_numbers()
        self.draw_selected_square_highlight()
        self.draw_center_circle()
        if data.debug:
            self.debug_draw_pathfinding_route()
            self.debug_draw_pathfinding_info()
            self.debug_draw_pathfinding_final_route()
        if data.focus == "move":
            rect = data.selected_square.get_rect()
            rect.topleft = rect.bottomright
            text = ORBITRON(20).render("Moving", 1, WHITE, BLUE)
            self.display.blit(text, rect)
        self.draw_windows()
                
        self.update()
        self.draw_total_time = time.time() - self.draw_start_time
        
    def draw_center_circle(self):
        center = data.graphics.display.get_rect().center
        rect = pygame.rect.Rect((0,0), (4, 4))
        rect.center = center
        pygame.draw.rect(data.graphics.display, RED, rect)
        
    def draw_background(self):
        self.display.fill(DARK_GREY)
        
    def draw_square_images(self):
        dirt_surf = pygame.surface.Surface((data.base_square_size, data.base_square_size))
        dirt_surf.blit(self.DIRTFLOOR,(0,0))
        wall_surf = pygame.surface.Surface((data.base_square_size, data.base_square_size))
        wall_surf.blit(self.STONEWALL,(0,0))
        dirt_surf_scaled = pygame.surface.Surface((data.square_size, data.square_size))
        pygame.transform.scale(dirt_surf, (data.square_size, data.square_size), dirt_surf_scaled)
        wall_surf_scaled = pygame.surface.Surface((data.square_size, data.square_size))
        pygame.transform.scale(wall_surf, (data.square_size, data.square_size), wall_surf_scaled)
        for column in range(board.board_size[0]):
            for row in range(board.board_size[1]):
                square = board.get_square((column, row))
                pixel_x = square.xy[0] * data.square_size + data.camera_offset[0]
                pixel_y = square.xy[1] * data.square_size + data.camera_offset[1]
                if square.blocked:
                    self.display.blit(wall_surf_scaled,(pixel_x, pixel_y))
                else:
                    self.display.blit(dirt_surf_scaled,(pixel_x, pixel_y))
        
    def draw_square_numbers(self):
        font_size = zoom(14)
        if data.draw_square_numbers:
            font = DEJAVUSANS(font_size)
            off = data.camera_offset
            color = WHITE
            for y in range(board.board_size[1]):  
                for x in range(board.board_size[0]):
                    num = str(x) + ", " + str(y)
                    text = font.render(num, 1, color)
                    t_rect = text.get_rect()
                    s_rect = board.get_square((x,y)).get_rect()
                    t_rect.center = s_rect.center
                    self.display.blit(text, t_rect)   
                

    def draw_gameboard(self):
        if data.draw_square_lines:
            off = data.camera_offset
            color = (180, 255, 255)
            for i in range(board.board_size[1]+1):
                start = [off[0],i * data.square_size + off[1]]
                end = [board.board_size[0] * data.square_size + off[0], i * data.square_size + off[1]]
                pygame.draw.line(self.display, color, start, end)
            for i in range(board.board_size[0]+1):
                start = [i * data.square_size + off[0], off[1]]
                end = [i * data.square_size + off[0], board.board_size[1] * data.square_size + off[1]]
                pygame.draw.line(self.display, color, start, end)
            
    def draw_selected_square_highlight(self):
        color = (120,160,190)
        x, y = data.selected_square.xy[0], data.selected_square.xy[1]
        x = x * data.square_size + data.camera_offset[0] + 1
        y = y * data.square_size + data.camera_offset[1] + 1
        if data.selected_square.unit != None:
            if data.selected_square.unit.move_dest != None:
                x += data.selected_square.unit.move_offset[0]
                y += data.selected_square.unit.move_offset[1]
        surf = pygame.surface.Surface((data.square_size - 1, data.square_size - 1))
        surf.fill(color)
        surf.set_alpha(90)
        pygame.draw.rect(surf, color, surf.get_rect())
        self.display.blit(surf, (x,y))

    def draw_units(self):
        UNITSCALE = 2
        off = data.camera_offset
        for unit in unitlist:
            rect = unit.get_rect()
            rect.left += off[0]
            rect.top += off[1]
            surf = pygame.surface.Surface((data.base_unit_size, data.base_unit_size))
            surf.blit(self.HUMAN, (-32, 0))
            scaled_surf = pygame.surface.Surface((data.unit_size * UNITSCALE, data.unit_size * UNITSCALE))
            pygame.transform.scale(surf, (data.unit_size * UNITSCALE, data.unit_size * UNITSCALE), scaled_surf)
            new_rect = scaled_surf.get_rect()
            rect.height = new_rect.height
            rect.width = new_rect.width
            rect.center = unit.square.get_rect().center
            rect.left += unit.move_offset[0]
            rect.top += unit.move_offset[1]
            scaled_surf.set_colorkey(DC_ALPHA)
            self.display.blit(scaled_surf, rect)
            for item in unit.clothes:
                c_surf = pygame.surface.Surface((16, 32))
                c_surf.blit(self.HUMAN, item[0])
                c_surf_scaled = pygame.surface.Surface((zoom(16 * UNITSCALE),zoom(32 * UNITSCALE)))
                pygame.transform.scale(c_surf, (zoom(16 * UNITSCALE), zoom(32 * UNITSCALE)), c_surf_scaled)
                c_surf_scaled.set_colorkey(DC_ALPHA)
                rect.left += zoom(item[1][0])
                rect.top += zoom(item[1][1])
                self.display.blit(c_surf_scaled, rect)
            
    
    def draw_windows(self): # draws all windows in windows (list)
        for window in windows:
            if window.visible:
                surface = pygame.surface.Surface(window.rect.size)
                surface.fill(window.color)
                draw_window_contents(surface, window)  
                self.display.blit(surface, window.rect)        
        
    def update(self):
        pygame.display.update()
        
    #### debug draws
    def debug_draw_pathfinding_info(self):
        for row in board.grid:
            for square in row:
                if data.zoom >= 70:
                    if square.path_f:
                        rect = square.get_rect()
                        rect.top += 2
                        rect.left += 2
                        text = FONT.render("F " + str(square.path_f), 1, YELLOW)
                        self.display.blit(text, rect)
                    
                    if square.path_g:
                        rect = square.get_rect()
                        text = FONT.render("G " + str(square.path_g), 1, AQUA)
                        t_rect = text.get_rect()
                        t_rect.top = rect.bottom - t_rect.height
                        t_rect.left = rect.left + 2
                        self.display.blit(text, t_rect)
                        
                    if square.path_h:
                        rect = square.get_rect()
                        text = FONT.render("H " + str(square.path_h), 1, PURPLE)
                        t_rect = text.get_rect()
                        t_rect.right = rect.right
                        t_rect.top = rect.top + 2
                        self.display.blit(text, t_rect)
    
    def debug_draw_pathfinding_route(self):
        # This is broken at the moment. I broke it when rebuilding the path to be usable for movement.
        c = 1
        size = zoom(32)
        gap = zoom(16)
        font_size = zoom(18)
        for square in data.pathfinding_route:
            surf = pygame.surface.Surface((size,size))
            surf.set_alpha(127)
            rect = square.get_rect()
            rect.topleft = (0,0)
            pygame.draw.rect(surf, RED, rect)
            text = UBUNTUMONO(font_size).render(str(c), 0, WHITE)
            rect = text.get_rect()
            surf_rect = surf.get_rect()
            rect.center = surf_rect.center
            surf.blit(text, rect)
            dest = square.get_rect()
            dest.top += gap
            dest.left += gap
            self.display.blit(surf, dest)
            c += 1
            
    def debug_draw_pathfinding_final_route(self):
        if data.astar.draw_final_route:
            square = data.astar.goal
            base = zoom(32)
            border = zoom(4)
            size = base + border
            while square:
                s_rect = square.get_rect()
                rect = pygame.rect.Rect(0,0,0,0)
                rect.height = size
                rect.width = size
                rect.center = s_rect.center
                
                pygame.draw.rect(self.display, GREEN, rect, border)
                square = square.path_parent
    
def draw_window_contents(surface, window):
    """ goes through the list of strings in window.contents and renders them """
    left, top = 10, 10
    right = 0

    for item in window.contents:
        text = window.font.render(item, 1, WHITE)
        if text.get_rect().right > right:
            right = text.get_rect().right
        if text.get_rect().bottom + top > surface.get_rect().bottom:
            left += (right + 70)
            top = 10
            right = 0
        destination = (left, top)
        surface.blit(text,destination)
        top += text.get_rect().height + 10
    
def zoom(number):
    return (number * data.zoom) / 100