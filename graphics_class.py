import pygame
from pygame.locals import *

from constants import *
from interface_class import windows
from unit_class import unitlist
from engine_class import data


class Graphics(object):
    
    def __init__(self):
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        
        self.offset = [100,100]
        
    def draw_background(self):
        self.display.fill(DARK_GREY)
        
    def draw_square_numbers(self):
        font = ORBITRON10
        if data.draw_square_numbers:
            off = data.camera_offset
            color = WHITE
            offset = 4
            for y in range(BOARD_SIZE[1]):
                top = y * SQUARE_SIZE + offset   
                for x in range(BOARD_SIZE[0]):
                    left = x * SQUARE_SIZE + offset
                    num = str(x) + ", " + str(y)
                    text = font.render(num, 1, color)
                    dest = (left + off[0], top + off[1])
                    self.display.blit(text, dest)   
                

    def draw_gameboard(self):
        off = data.camera_offset
        color = (180, 255, 255)
        for i in range(BOARD_SIZE[1]+1):
            start = [off[0],i * SQUARE_SIZE + off[1]]
            end = [BOARD_SIZE[0] * SQUARE_SIZE + off[0], i * SQUARE_SIZE + off[1]]
            pygame.draw.line(self.display, color, start, end)
        for i in range(BOARD_SIZE[0]+1):
            start = [i * SQUARE_SIZE + off[0], off[1]]
            end = [i * SQUARE_SIZE + off[0], BOARD_SIZE[1] * SQUARE_SIZE + off[1]]
            pygame.draw.line(self.display, color, start, end)
            
    def draw_selected_square_highlight(self):
        color = (180,180,120)
        x, y = data.selected_square.xy[0], data.selected_square.xy[1]
        x = x * SQUARE_SIZE + data.camera_offset[0] + 1
        y = y * SQUARE_SIZE + data.camera_offset[1] + 1
        surf = pygame.surface.Surface((SQUARE_SIZE - 1, SQUARE_SIZE - 1))
        surf.fill(color)
        surf.set_alpha(100)
        pygame.draw.rect(surf, color, surf.get_rect())
        self.display.blit(surf, (x,y))


    def draw_units(self, unitlist):
        off = data.camera_offset
        for unit in unitlist:
            rect = unit.get_rect()
            rect.left += off[0]
            rect.top += off[1]
            pygame.draw.rect(self.display, unit.color, rect)
    
    def draw_windows(self):
        for window in windows:
            if window.visible:
                surface = pygame.surface.Surface(window.size)
                surface.fill(window.color)
                draw_window_contents(surface, window)
                dest = window.pos
                self.display.blit(surface, dest)        
        
    def update(self):
        off = data.camera_offset
        self.offset[0] += off[0]
        self.offset[1] += off[1]
        pygame.display.update()
    
def draw_window_contents(surface, window):
    """ goes through the list of strings in window.contents and renders them """
    left, top = 5, 5
    right = 0

    for item in window.contents:
        text = window.font.render(item, 1, WHITE)
        if text.get_rect().right > right:
            right = text.get_rect().right
        if text.get_rect().bottom + top > surface.get_rect().bottom:
            left += right + 5
            top = 5
            right = 0
        destination = (left, top)
        surface.blit(text,destination)
        top += text.get_rect().height + 5
