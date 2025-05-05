from Piece import *


#Лєра, це все твоє, внизу прикріплю ще видозмінене і воно НЕ буде закоментоване


# class View:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((600, 800))
#         pygame.display.set_icon(pygame.image.load('icon.png'))
#         pygame.display.set_caption("Тетрiс")
#
#         # checking if it works xd
#         self.falling_piece = SquareShape([5, 0], (200, 200, 50))
#         self.BLOCK_SIZE = 40
#
#         self.FALL_EVENT = pygame.USEREVENT + 1
#         pygame.time.set_timer(self.FALL_EVENT, 1000)
#         # checking if it works xd
#
#         self.play()
#
#     def draw_grid(self):
#         cell = 40
#         for x in range(0, 600, cell):
#             pygame.draw.line(self.screen, (28, 28, 28), (x, 0), (x, 800), width= 3)
#
#         for y in range(0, 800, cell):
#             pygame.draw.line(self.screen, (28, 28, 28), (0, y), (600, y), width= 3)
#
#
# #Написав Кіріло Батрачіло для виведення екранчику
#
#
#     def draw_piece(self, piece):
#         piece.draw(self.screen, self.BLOCK_SIZE)
#
#     def draw_board(self, board):
#         for y in range(20):
#             for x in range(10):
#                 if board[y][x]:
#                     pygame.draw.rect(
#                         self.screen,
#                         (200, 200, 50),
#                         (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
#                     )
#                     pygame.draw.rect(
#                         self.screen,
#                         (0, 0, 0),
#                         (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE),
#                         2
#                     )
#
#     def draw_score(self, score):
#         font = pygame.font.Font(None, 36)
#         score_text = font.render(f"Score: {score}", True, (255, 255, 255))
#         self.screen.blit(score_text, (10, 10))
#
# ########################################################
#
#     # def play(self):
#     #     running = True
#     #     while running:
#     #
#     #         self.screen.fill((33, 33, 33))
#     #
#     #         self.draw_grid()
#     #
#     #         # checking if it works xd
#     #         self.falling_piece.draw(self.screen, self.BLOCK_SIZE)
#     #         # checking if it works xd
#     #
#     #         pygame.display.update()
#     #
#     #         for event in pygame.event.get():
#     #
#     #             # checking if it works xd
#     #             if event.type == self.FALL_EVENT:
#     #                 self.falling_piece.move()
#     #             # checking if it works xd
#     #
#     #             if event.type == pygame.QUIT:
#     #                 running = False
#     #
#     #     pygame.quit()
#
#
# # if __name__ == '__main__':
# #     game = View()

import pygame
from Piece import *

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('icon.png'))
        pygame.display.set_caption("Тетріс")
        self.BLOCK_SIZE = 40
        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, 1000)

    def draw_grid(self):
        for x in range(0, 600, self.BLOCK_SIZE):  # 15 columns = 600 pixels
            pygame.draw.line(self.screen, (28, 28, 28), (x, 0), (x, 800), width=2)
        for y in range(0, 800, self.BLOCK_SIZE):  # 20 rows = 800 pixels
            pygame.draw.line(self.screen, (28, 28, 28), (0, y), (600, y), width=2)

    def draw_piece(self, piece):
        piece.draw(self.screen, self.BLOCK_SIZE)

    def draw_board(self, board):
        for y in range(20):
            for x in range(15):  # Змінено з 10 на 15 для відображення повного поля
                if board[y][x]:
                    pygame.draw.rect(
                        self.screen,
                        (200, 200, 50),
                        (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
                    )
                    pygame.draw.rect(
                        self.screen,
                        (0, 0, 0),
                        (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE),
                        2
                    )

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))