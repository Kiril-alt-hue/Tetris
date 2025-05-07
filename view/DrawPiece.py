import pygame

class DrawPiece:
    def __init__(self, screen):
        self.screen = screen
        self.BLOCK_SIZE = 40
        self.GRID_WIDTH = 600
        self.GRID_HEIGHT = 650

    def draw_piece(self, piece):
        px, py = piece.position
        BLOCK_SIZE = self.BLOCK_SIZE

        for dx, dy in piece.coordinates:
            x = (px + dx) * BLOCK_SIZE
            y = (py + dy) * BLOCK_SIZE

            if 0 <= x < self.GRID_WIDTH and 0 <= y < self.GRID_HEIGHT:
                #заповнений блок
                pygame.draw.rect(
                    self.screen,
                    piece.color,
                    (x, y, BLOCK_SIZE, BLOCK_SIZE)
                )
                #рамка
                pygame.draw.rect(
                    self.screen,
                    (28, 28, 28),
                    (x, y, BLOCK_SIZE, BLOCK_SIZE),
                    2
                )