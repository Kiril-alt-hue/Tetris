import pygame

class Platform:
    def __init__(self, screen):
        self.screen = screen
        self.GRID_HEIGHT = 650

    def draw_platform(self):
        pygame.draw.rect(self.screen, (50, 50, 50), (0, self.GRID_HEIGHT, 600, 150))
        pygame.draw.rect(self.screen, (255, 194, 236), (0, self.GRID_HEIGHT, 600, 150), 3)
