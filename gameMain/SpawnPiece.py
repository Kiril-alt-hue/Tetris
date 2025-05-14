from Piece import *
import random


class SpawnPiece:
    def __init__(self, theme_colors):
        self.theme_colors = theme_colors

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        shape_class = random.choice(shapes)
        shape_color = random.choice(self.theme_colors)
        return shape_class([5, 0], shape_color)