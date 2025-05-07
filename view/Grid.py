import pygame

class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.GRID_HEIGHT = 650
        self.BLOCK_SIZE = 40

    def draw_grid(self):
        #сітка
        for x in range(0, 600, self.BLOCK_SIZE):
            pygame.draw.line(self.screen, (28, 28, 28), (x, 0), (x, self.GRID_HEIGHT), 3) #змінила товщину на 3
        for y in range(0, self.GRID_HEIGHT, self.BLOCK_SIZE):
            pygame.draw.line(self.screen, (28, 28, 28), (0, y), (600, y), 3) #змінила товщину на 3
