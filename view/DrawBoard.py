import pygame
from Board import Board

class DrawBoard:
    def __init__(self, screen, block_size):
        self.screen = screen
        self.BLOCK_SIZE = block_size
        self.BORDER_COLOUR = (28, 28, 28)
        self.EMPTY_CELL = 0
        self.BORDER_WIDTH = 2

    def draw_board(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                cell_color = board[y][x]
                if cell_color == self.EMPTY_CELL:
                    continue
                self._draw_block(x, y, cell_color)

    def _draw_block(self, x, y, color):
        rect = (
            x * self.BLOCK_SIZE,
            y * self.BLOCK_SIZE,
            self.BLOCK_SIZE,
            self.BLOCK_SIZE
        )
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, self.BORDER_COLOUR, rect, self.BORDER_WIDTH)

def test_draw_board():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    block_size = 40
    board = Board(screen, block_size)
    drawer = DrawBoard(screen, block_size)
    board.board[5][3] = (255, 0, 0)
    board.board[6][3] = (255, 0, 0)
    board.board[7][3] = (255, 0, 0)
    board.board[7][4] = (0, 255, 0)
    board.board[7][5] = (0, 0, 255)
    board.board[15][2] = (255, 255, 0)
    drawer.draw_board(board.board)
    pygame.display.flip()
    pygame.quit()
    assert drawer.BLOCK_SIZE == 40, "Розмір блоку має бути 40"
    assert drawer.BORDER_WIDTH == 2, "Товщина рамки має бути 2"
    print("Тест DrawBoard пройдено!")

if __name__ == "__main__":
    test_draw_board()