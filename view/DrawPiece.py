# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pygame
from view.Grid import Grid
from Piece import Piece, SquareShape

class DrawPiece:
    def __init__(self, screen):
        self.screen = screen
        self.grid = Grid(screen)
        self.block_size = 40

    def draw_piece(self, piece: Piece):
        piece.draw(self.screen, self.block_size)

def test_draw_piece():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    draw_piece = DrawPiece(screen)
    piece = SquareShape([5, 5], (255, 0, 0))
    draw_piece.draw_piece(piece)
    pygame.display.flip()
    pygame.quit()
    assert draw_piece.grid.BLOCK_SIZE == 40, "Розмір блоку має бути 40"
    assert draw_piece.block_size == 40, "Розмір блоку DrawPiece має бути 40"
    print("Тест DrawPiece пройдено!")

if __name__ == "__main__":
    test_draw_piece()