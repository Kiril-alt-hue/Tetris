import pygame
import random
from Piece import Piece, SquareShape, TShape
from View import View
from Board import Board

class Mechanika:
    def __init__(self):
        self.view = View()
        self.board = Board()
        self.score = 0
        self.game_over = False
        self.current_piece = self.spawn_piece()

    def spawn_piece(self):
        shapes = [SquareShape, TShape]
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
