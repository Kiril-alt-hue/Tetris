import pygame
import random
from Piece import *
from View import View, Button
from Board import Board

class Mechanika:
    def __init__(self):
        self.view = View()
        self.board = Board()
        self.score = 0
        self.game_over = False
        self.current_piece = self.spawn_piece()
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        shape_class = random.choice(shapes)
        return shape_class([7, 0], (200, 200, 50))

    def drop_piece_to_bottom(self):
        while not self.board.check_collision(self.current_piece, dy=1):
            self.current_piece.move(dy=1)
        self.board.lock_piece(self.current_piece)
        self.score += self.board.clear_lines() * 100
        self.current_piece = self.spawn_piece()
        if self.board.is_game_over(self.current_piece):
            self.game_over = True

    def run(self):
                                                                # start menu script
        in_menu = True
        while in_menu:
            self.view.screen.fill((33, 33, 33))
            self.start_button.draw_button(self.view.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_clicked(event.pos):
                        in_menu = False
                                                                # end menu script
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == self.view.FALL_EVENT:
                    if not self.board.check_collision(self.current_piece, dy=1):
                        self.current_piece.move(dy=1)
                    else:
                        self.board.lock_piece(self.current_piece)
                        self.score += self.board.clear_lines() * 100
                        self.current_piece = self.spawn_piece()
                        if self.board.is_game_over(self.current_piece):
                            self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.board.check_collision(self.current_piece, dx=-1):
                            self.current_piece.move(dx=-1)
                    elif event.key == pygame.K_RIGHT:
                        if not self.board.check_collision(self.current_piece, dx=1):
                            self.current_piece.move(dx=1)
                    elif event.key == pygame.K_UP:
                        original_coords = self.current_piece.coordinates
                        self.current_piece.coordinates = self.current_piece.rotate()
                        if self.board.check_collision(self.current_piece):
                            self.current_piece.coordinates = original_coords
                    elif event.key == pygame.K_DOWN:
                        self.drop_piece_to_bottom()

            self.view.screen.fill((33, 33, 33))
            self.view.draw_grid()
            self.view.draw_piece(self.current_piece)
            self.view.draw_board(self.board.board)
            self.view.draw_score(self.score)
            pygame.display.flip()


        pygame.quit()

if __name__ == "__main__":
    game = Mechanika()
    game.run()
