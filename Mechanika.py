import pygame
import random
from Piece import *
from View import View
from Board import Board

class Mechanika:
    def __init__(self):
        self.view = View()
        self.board = Board()
        self.score = 0
        self.game_over = False
        self.current_piece = self.spawn_piece()
        self.clock = pygame.time.Clock()
        self.move_delay = 100  # Затримка в мс між рухами
        self.last_move_time = 0  # Час останнього руху
        self.just_moved = False  # Флаг, що шматок щойно рухався

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        shape_class = random.choice(shapes)
        return shape_class([5, 0], (200, 200, 50))  # Центр для поля шириною 10

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
            current_time = pygame.time.get_ticks()
            self.clock.tick(60)
            self.just_moved = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == self.view.FALL_EVENT and not self.just_moved:
                    if not self.board.check_collision(self.current_piece, dy=1):
                        self.current_piece.move(dy=1)
                    else:
                        self.board.lock_piece(self.current_piece)
                        self.score += self.board.clear_lines() * 100
                        self.current_piece = self.spawn_piece()
                        if self.board.is_game_over(self.current_piece):
                            self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if current_time - self.last_move_time > self.move_delay:
                        if event.key == pygame.K_LEFT:
                            if not self.board.check_collision(self.current_piece, dx=-1):
                                self.current_piece.move(dx=-1)
                                self.last_move_time = current_time
                                self.just_moved = True
                        elif event.key == pygame.K_RIGHT:
                            if not self.board.check_collision(self.current_piece, dx=1):
                                self.current_piece.move(dx=1)
                                self.last_move_time = current_time
                                self.just_moved = True
                        elif event.key == pygame.K_UP:
                            original_coords = self.current_piece.coordinates
                            original_pos = self.current_piece.position.copy()
                            self.current_piece.coordinates = self.current_piece.rotate()
                            if self.board.check_collision(self.current_piece):
                                self.current_piece.coordinates = original_coords
                                self.current_piece.position = original_pos
                        elif event.key == pygame.K_DOWN:
                            self.drop_piece_to_bottom()
                            self.last_move_time = current_time

            self.view.screen.fill((33, 33, 33))
            self.view.draw_grid()
            self.view.draw_piece(self.current_piece)
            self.view.draw_board(self.board.board)
            self.view.draw_score(self.score)
            pygame.display.flip()

        self.show_game_over_screen()
        pygame.quit()

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        self.view.screen.fill((33, 33, 33))
        self.view.screen.blit(game_over_text, (150, 300))
        self.view.screen.blit(score_text, (150, 350))
        self.view.screen.blit(restart_text, (150, 400))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()  # Перезавантаження гри
                        self.run()
                        return

if __name__ == "__main__":
    game = Mechanika()
    game.run()