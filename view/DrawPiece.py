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


if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("DrawPiece Test")

    # Create a DrawPiece instance
    drawer = DrawPiece(screen)

    # Create a test piece (using SquareShape as an example)
    test_piece = Piece(SquareShape(), 5, 5)  # Positioned at (5, 5) in grid coordinates

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Draw the grid (assuming Grid class has a draw method)
        drawer.grid.draw()

        # Draw the piece
        drawer.draw_piece(test_piece)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

