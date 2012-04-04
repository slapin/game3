import pygame, gameboard
from constants import *

board = gameboard.board
class Graphics(object):
    
    def __init__(self):
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
    
    def update(self):
        pygame.display.update()
        
    def draw_background(self):
        self.display.fill(DARK_GREY)
        
#    def draw_gameboard(self): # DEPRECATED BOX-STYLE DRAW GAMEBOARD FUNCTION
#        top, left = 0, 0
#        for row in board.grid:
#            left = 0
#            for square in row:
#                rect = pygame.rect.Rect(left, top, SQUARE_SIZE, SQUARE_SIZE)
#                pygame.draw.rect(self.display, BLUE, rect, 1)
#                left += SQUARE_SIZE
#            top += SQUARE_SIZE
    def draw_gameboard(self):
        x, y = 0, 0
        end_x = BOARD_SIZE[0] * SQUARE_SIZE
        end_y = BOARD_SIZE[1] * SQUARE_SIZE
        for i in range(BOARD_SIZE[1]):
            pygame.draw.line(self.display, RED, (x, i * SQUARE_SIZE), (end_x, i * SQUARE_SIZE))
        for i in range(BOARD_SIZE[0]):
            pygame.draw.line(self.display, RED, (i * SQUARE_SIZE, y), (i * SQUARE_SIZE, end_y))
                  
                
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
