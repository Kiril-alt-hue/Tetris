from Piece import *
import random


class SpawnPiece:
    def __init__(self, theme_colors):
        self.theme_colors = theme_colors
        self.shape_class = SquareShape
        self.shape_color = (255, 255, 255)

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        self.shape_class = random.choice(shapes)
        self.shape_color = random.choice(self.theme_colors)
        return self.shape_class([5, 0], self.shape_color)


class SpawnNextPiece(SpawnPiece):
    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        self.shape_class = random.choice(shapes)
        self.shape_color = random.choice(self.theme_colors)
        return self.shape_class([3, 18], self.shape_color)

    def return_piece(self):
        piece = self.shape_class([5, 0], self.shape_color)
        return piece