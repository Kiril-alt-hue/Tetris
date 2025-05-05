import pygame
import sys

class Piece:
    def __init__(self, coordinates : list, position : list, color):
        self.coordinates = coordinates
        self.position = position
        self.color = color

    def draw(self, surface, block_size):
        px, py = self.position
        for dx, dy in self.coordinates:
            x = (px + dx) * block_size
            y = (py + dy) * block_size
            pygame.draw.rect(surface, self.color, (x, y, block_size, block_size))
            pygame.draw.rect(surface, (0, 0, 0), (x, y, block_size, block_size), 2)

    def rotate(self):
        return [(-y, x) for x, y in self.coordinates] # expected list of coordinates :
                                                      # [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

    def move(self, dx=0, dy=1):
        self.position[0] += dx
        self.position[1] += dy     # expected position : [x, y]


class SquareShape(Piece):
    def __init__(self, position: list, color):
        coordinates = [(0, 0), (1, 0), (0, 1), (1, 1)]
        super().__init__(coordinates, position, color)


class TShape(Piece):
    def __init__(self, position: list, color):
        coordinates = [(0, -1), (-1, 0), (0, 0), (1, 0)]
        super().__init__(coordinates, position, color)



