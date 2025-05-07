import pygame
from Platform import *
from Grid import *
from DrawBoard import *
from DrawPiece import *
from  DrawScore import *
from  Button import *


class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('icon.png'))
        pygame.display.set_caption("Тетріс")
        self.BLOCK_SIZE = 40
        self.GRID_HEIGHT = 650
        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, 1500)

