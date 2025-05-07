import pygame


class DrawBoard:
    def __init__(self, screen, block_size):
        self.screen = screen
        self.BLOCK_SIZE = block_size
        self.BORDER_COLOUR = (28, 28, 28) #замінила чорний на більш світлий
        self.EMPTY_CELL = 0 #порожня клітинка
        self.BORDER_WIDTH = 2 #товщина рамки

#усе інше покращила
    def draw_board(self, board):
        for y in range(len(board)): #замінила рандомні числа
            for x in range(len(board[0])): #замінила рандомні числа
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

        # Заповнення кольором
        pygame.draw.rect(self.screen, color, rect)
        # Рамка
        pygame.draw.rect(self.screen, self.BORDER_COLOUR, rect, self.BORDER_WIDTH)