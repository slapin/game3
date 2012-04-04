import pygame
from constants import *

class Graphics(object):
    
    def __init__(self):
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        self.offset = [100,100]
    
    def update(self, offset):
        self.offset[0] += offset[0]
        self.offset[1] += offset[1]
        pygame.display.update()
        
    def draw_background(self):
        self.display.fill(DARK_GREY)
        
    def draw_square_numbers(self, offset):
        off = offset
        color = WHITE
        buffer = 4
        for y in range(BOARD_SIZE[1]):
            top = y * SQUARE_SIZE + buffer   
            for x in range(BOARD_SIZE[0]):
                left = x * SQUARE_SIZE + buffer
                num = str(x) + ", " + str(y)
                text = ORBITRON.render(num, 1, color)
                dest = (left, top)
                self.display.blit(text, dest)   
                

    def draw_gameboard(self, offset):
        off = offset
        color = YELLOW
        for i in range(BOARD_SIZE[1]+1):
            start = [off[0],i * SQUARE_SIZE + off[1]]
            end = [BOARD_SIZE[0] * SQUARE_SIZE + off[0], i * SQUARE_SIZE + off[1]]
            pygame.draw.line(self.display, color, start, end)
        for i in range(BOARD_SIZE[0]+1):
            start = [i * SQUARE_SIZE + off[0], off[1]]
            end = [i * SQUARE_SIZE + off[0], BOARD_SIZE[1] * SQUARE_SIZE + off[1]]
            pygame.draw.line(self.display, color, start, end)

                  
                
    def draw_windows(self, windows):
        for window in windows:
            if window.visible:
                surface = pygame.surface.Surface(window.size)
                surface.fill(window.color)
                draw_window_contents(surface, window)
                dest = window.pos
                self.display.blit(surface, dest)
    
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
