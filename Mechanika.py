import random
from Piece import *
from View import View, Button
from Board import Board

class Mechanika:
    def __init__(self):
        self.view = View()
        self.board = Board(self.view)
        self.score = 0
        self.game_over = False
        self.current_piece = self.spawn_piece()
        self.clock = pygame.time.Clock()
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")
        self.move_delay = 100
        self.last_move_time = 0
        self.just_moved = False
        self.paused = False
        self.lock_time = 0

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        shape_class = random.choice(shapes)
        return shape_class([5, 0], (200, 200, 50))

    def drop_piece_to_bottom(self):
        while not self.board.check_collision(self.current_piece, dy=1):
            self.current_piece.move(dy=1)
        self.board.lock_piece(self.current_piece)
        self.score += self.board.clear_lines() * 100
        self.current_piece = self.spawn_piece()
        if self.board.is_game_over(self.current_piece):
            self.game_over = True

    def run(self):
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

        while not self.game_over:
            current_time = pygame.time.get_ticks()
            self.clock.tick(60)
            self.just_moved = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == self.view.FALL_EVENT and not self.paused:
                    if not self.board.check_collision(self.current_piece, dy=1):
                        self.current_piece.move(dy=1)
                    else:
                        if self.lock_time == 0:
                            self.lock_time = pygame.time.get_ticks()
                        elif pygame.time.get_ticks() - self.lock_time > 500:
                            self.board.lock_piece(self.current_piece)
                            self.score += self.board.clear_lines() * 100
                            self.current_piece = self.spawn_piece()
                            self.lock_time = 0
                            if self.board.is_game_over(self.current_piece):
                                self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if not self.paused and current_time - self.last_move_time > self.move_delay:
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
                        elif event.key == pygame.K_p:
                            self.paused = not self.paused
                            self.lock_time = 0
                    elif event.key == pygame.K_p and self.paused:
                        self.paused = False

            if not self.game_over:
                if not self.paused:
                    self.view.screen.fill((33, 33, 33))

                    self.view.screen.set_clip(0, 0, 600, self.view.GRID_HEIGHT) #область відсікання
                    self.view.draw_grid()
                    self.view.draw_piece(self.current_piece)
                    self.view.draw_board(self.board.board)
                    # self.view.draw_score(self.score)
                    self.view.screen.set_clip(None)  #скидаємо обмеження

                    #малювання платформи та рахунку
                    self.view.draw_platform()
                    self.view.draw_score(self.score)
                else:
                    font = pygame.font.Font(None, 48)
                    pause_text = font.render("Paused", True, (255, 255, 255))
                    self.view.screen.blit(pause_text, (250, 400))
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
                        self.__init__()
                        self.run()
                        return

if __name__ == "__main__":
    game = Mechanika()
    game.run()