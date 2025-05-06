import random
from Piece import *
from View import View, Button
from Board import Board

class Mechanika:
    def __init__(self):
        self.view = View()
        self.board = Board(self.view)
        self.score = 0             # Початковий рахунок
        self.game_over = False     # Прапорець завершення гри
        self.current_piece = self.spawn_piece()  # Створення початкової фігури
        self.clock = pygame.time.Clock()  # Ініціалізація таймера
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")
        self.move_delay = 100      # Затримка між рухами
        self.last_move_time = 0    # Час останнього руху
        self.just_moved = False    # Прапорець останнього руху
        self.paused = False        # Прапорець паузи
        self.lock_time = 0         # Час для фіксації фігури

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        shape_class = random.choice(shapes)  # Випадковий вибір фігури
        return shape_class([5, 0], (200, 200, 50))

    def drop_piece_to_bottom(self):
        while not self.board.check_collision(self.current_piece, dy=1):  # Перевірка колізій при падінні
            self.current_piece.move(dy=1)  # Рух фігури вниз
        self.board.lock_piece(self.current_piece)  # Фіксація фігури на дошку
        self.score += self.board.clear_lines() * 100  # Додавання балів за очищення рядків
        self.current_piece = self.spawn_piece()  # Створення нової фігури
        if self.board.is_game_over(self.current_piece):  # Перевірка завершення гри
            self.game_over = True

    def run(self):
        in_menu = True
        while in_menu:  # Цикл меню
            self.view.screen.fill((33, 33, 33))  # Заповнення екрану чорним
            self.start_button.draw_button(self.view.screen)  # Малювання кнопки
            pygame.display.flip()  # Оновлення екрану

            for event in pygame.event.get():  # Обробка подій
                if event.type == pygame.QUIT:  # Вихід із гри
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Натискання миші
                    if self.start_button.is_clicked(event.pos):  # Початок гри
                        in_menu = False

        while not self.game_over:  # Основний цикл гри
            current_time = pygame.time.get_ticks()  # Поточний час
            self.clock.tick(60)  # Обмеження FPS
            self.just_moved = False
            for event in pygame.event.get():  # Обробка подій
                if event.type == pygame.QUIT:  # Вихід із гри
                    self.game_over = True
                elif event.type == self.view.FALL_EVENT and not self.paused:  # Подія падіння
                    if not self.board.check_collision(self.current_piece, dy=1):  # Перевірка колізій
                        self.current_piece.move(dy=1)# Рух вниз
                        self.lock_time = 0 # Додав для можливого вирішення багу (воно працює!!!!)
                    else:  # Фіксація при колізії
                        if self.lock_time == 0:
                            self.lock_time = pygame.time.get_ticks()
                        elif pygame.time.get_ticks() - self.lock_time > 500:
                            self.board.lock_piece(self.current_piece)
                            self.score += self.board.clear_lines() * 100
                            self.current_piece = self.spawn_piece()
                            self.lock_time = 0
                            if self.board.is_game_over(self.current_piece):
                                self.game_over = True
                elif event.type == pygame.KEYDOWN:  # Обробка клавіш
                    if not self.paused and current_time - self.last_move_time > self.move_delay:
                        if event.key == pygame.K_LEFT:  # Рух вліво
                            if not self.board.check_collision(self.current_piece, dx=-1):
                                self.current_piece.move(dx=-1)
                                self.last_move_time = current_time
                                self.just_moved = True
                        elif event.key == pygame.K_RIGHT:  # Рух вправо
                            if not self.board.check_collision(self.current_piece, dx=1):
                                self.current_piece.move(dx=1)
                                self.last_move_time = current_time
                                self.just_moved = True
                        elif event.key == pygame.K_UP:  # Обертання
                            if not isinstance(self.current_piece, SquareShape):
                                original_coords = self.current_piece.coordinates
                                original_pos = self.current_piece.position.copy()
                                self.current_piece.coordinates = self.current_piece.rotate()
                                if self.board.check_collision(self.current_piece):
                                    self.current_piece.coordinates = original_coords
                                    self.current_piece.position = original_pos
                        elif event.key == pygame.K_DOWN:  # Швидке падіння
                            self.drop_piece_to_bottom()
                            self.last_move_time = current_time
                        elif event.key == pygame.K_p:  # Пауза
                            self.paused = not self.paused
                            self.lock_time = 0
                    elif event.key == pygame.K_p and self.paused:  # Вихід із паузи
                        self.paused = False

            if not self.game_over:
                if not self.paused:  # Малювання гри
                    self.view.screen.fill((33, 33, 33))
                    self.view.screen.set_clip(0, 0, 600, self.view.GRID_HEIGHT)
                    self.view.draw_grid()
                    self.view.draw_piece(self.current_piece)
                    self.view.draw_board(self.board.board)
                    self.view.screen.set_clip(None)
                    self.view.draw_platform()
                    self.view.draw_score(self.score)
                else:  # Малювання паузи
                    font = pygame.font.Font(None, 48)
                    pause_text = font.render("Paused", True, (255, 255, 255))
                    self.view.screen.blit(pause_text, (250, 400))
                pygame.display.flip()

        self.show_game_over_screen()  # Показ екрану завершення гри
        pygame.quit()

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        self.view.screen.fill((33, 33, 33))  # Заповнення екрану
        self.view.screen.blit(game_over_text, (150, 300))
        self.view.screen.blit(score_text, (150, 350))
        self.view.screen.blit(restart_text, (150, 400))
        pygame.display.flip()
        waiting = True
        while waiting:  # Цикл очікування перезапуску
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Вихід
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Перезапуск
                        self.__init__()
                        self.run()
                        return

if __name__ == "__main__":
    game = Mechanika()
    game.run()