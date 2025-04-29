import pygame
from random import *
from Piece import *

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('icon.png'))
        pygame.display.set_caption("Тетрiс")

        # checking if it works xd
        self.falling_piece = SquareShape([5, 0], (200, 200, 50))
        self.BLOCK_SIZE = 40

        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, 1000)
        # checking if it works xd

        self.play()

    def draw_grid(self):
        cell = 40
        for x in range(0, 600, cell):
            pygame.draw.line(self.screen, (28, 28, 28), (x, 0), (x, 800), width= 3)

        for y in range(0, 800, cell):
            pygame.draw.line(self.screen, (28, 28, 28), (0, y), (600, y), width= 3)


    def play(self):
        running = True
        while running:

            self.screen.fill((33, 33, 33))

            self.draw_grid()

            # checking if it works xd
            self.falling_piece.draw(self.screen, self.BLOCK_SIZE)
            # checking if it works xd

            pygame.display.update()

            for event in pygame.event.get():

                # checking if it works xd
                if event.type == self.FALL_EVENT:
                    self.falling_piece.move()
                # checking if it works xd

                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


if __name__ == '__main__':
    game = View()