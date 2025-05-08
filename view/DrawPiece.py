import pygame
from Grid import *

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


if __name__ == "__main__":
    #TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("DrawPiece Test")
    clock = pygame.time.Clock()


    #Test Piece class
    class TestPiece:
        def __init__(self, position, coordinates, color):
            self.position = position
            self.coordinates = coordinates
            self.color = color

    square_piece = TestPiece(
        [5, 5],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        (255, 0, 0)  #ЧЕРВОНИЙ
    )

    line_piece = TestPiece(
        [3, 2],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        (0, 255, 0)  #ЗЕЛЕНИЙ
    )

    l_piece = TestPiece(
        [7, 4],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        (0, 0, 255)  #СИНІЙ
    )

    drawer = DrawPiece(screen)
    grid = Grid(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))
        grid.draw_grid()

        drawer.draw_piece(square_piece)
        drawer.draw_piece(line_piece)
        drawer.draw_piece(l_piece)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print("Тестування завершено успішно!")