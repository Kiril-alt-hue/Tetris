# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pygame
from view.Grid import Grid
from view.DrawPiece import DrawPiece
from view.DrawBoard import DrawBoard
from view.Platform import Platform
from view.DrawScore import DrawScore
from Board import Board
from Piece import SquareShape

class DrawPauseOnOff:
    def __init__(self, screen, grid: Grid, draw_piece: DrawPiece, draw_board: DrawBoard, platform: Platform, draw_score: DrawScore):
        self.screen = screen
        self.grid = grid
        self.draw_piece = draw_piece
        self.draw_board = draw_board
        self.platform = platform
        self.draw_score = draw_score
        self.GRID_HEIGHT = 650

    def draw_pause_on_off(self, paused, piece, board, score):
        if not paused:
            self.screen.fill((33, 33, 33))
            self.screen.set_clip(0, 0, 600, self.GRID_HEIGHT)
            self.grid.draw_grid()
            self.draw_piece.draw_piece(piece)
            self.draw_board.draw_board(board)
            self.screen.set_clip(None)
            self.platform.draw_platform()
            self.draw_score.draw_score(score)
        else:
            font = pygame.font.SysFont('jokerman', 50)
            pause_text = font.render("Pause", True, (240, 240, 240))
            self.screen.blit(pause_text, (230, 330))
        pygame.display.flip()

def test_draw_pause_on_off():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    grid = Grid(screen)
    draw_piece = DrawPiece(screen)
    draw_board = DrawBoard(screen, 40)
    platform = Platform(screen)
    draw_score = DrawScore(screen)
    draw_pause = DrawPauseOnOff(screen, grid, draw_piece, draw_board, platform, draw_score)
    board = Board(screen, 40)
    piece = SquareShape([5, 5], (255, 0, 0))
    draw_pause.draw_pause_on_off(False, piece, board.board, 0)
    draw_pause.draw_pause_on_off(True, piece, board.board, 0)
    pygame.quit()
    assert draw_pause.GRID_HEIGHT == 650, "GRID_HEIGHT має бути 650"
    print("Тест DrawPauseOnOff пройдено!")

if __name__ == "__main__":
    test_draw_pause_on_off()