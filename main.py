import pygame, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(200,50)

from constants import *
from engine_class import Engine

engine = Engine()

def main():
    while True:
        engine.run()
if __name__ == "__main__":
    main()