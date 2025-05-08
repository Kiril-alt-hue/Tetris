import random

from Board import Board
from Piece import *
from View import View


class Mechanika:
    def __init__(self):
        self.view = View()
        self.board = Board(self.view)
        self.score = 0             # Початковий рахунок
        self.game_over = False     # Прапорець завершення гри
        self.current_piece = self.spawn_piece()  # Створення початкової фігури
        self.clock = pygame.time.Clock()  # Ініціалізація таймера
        self.move_delay = 120      # Затримка між рухами
        self.last_move_time = 0    # Час останнього руху
        self.just_moved = False    # Прапорець останнього руху
        self.paused = False        # Прапорець паузи
        self.lock_time = 0         # Час для фіксації фігури

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        colors = [(255, 0, 0), (0, 128, 0), (0, 255, 255), (128, 0, 128), (255, 165, 0), (255, 255, 0), (0, 255, 0)]
        shape_color = random.choice(colors)
        shape_class = random.choice(shapes)  # Випадковий вибір фігури
        return shape_class([5, 0], shape_color)

    def drop_piece_to_bottom(self):
        while not self.board.check_collision(self.current_piece, dy=1):  # Перевірка колізій при падінні
            self.current_piece.move(dy=1)  # Рух фігури вниз
        self.board.lock_piece(self.current_piece)  # Фіксація фігури на дошку
        self.score += self.board.clear_lines() * 100  # Додавання балів за очищення рядків
        self.current_piece = self.spawn_piece()  # Створення нової фігури
        if self.board.is_game_over(self.current_piece):  # Перевірка завершення гри
            self.game_over = True

    def run(self):
        self.view.draw_menu()

        while not self.game_over:  # Основний цикл гри
            current_time = pygame.time.get_ticks()  # Поточний час
            self.clock.tick(60)  # Обмеження FPS
            self.just_moved = False

            # Перевірка на утримання клавіш для руху
            keys = pygame.key.get_pressed()
            if not self.paused and current_time - self.last_move_time > self.move_delay:
                if keys[pygame.K_LEFT]:  # Рух вліво
                    if not self.board.check_collision(self.current_piece, dx=-1):
                        self.current_piece.move(dx=-1)
                        self.last_move_time = current_time
                        self.just_moved = True
                if keys[pygame.K_RIGHT]:  # Рух вправо
                    if not self.board.check_collision(self.current_piece, dx=1):
                        self.current_piece.move(dx=1)
                        self.last_move_time = current_time
                        self.just_moved = True
                if keys[pygame.K_DOWN]:  # Прискорене падіння
                    if not self.board.check_collision(self.current_piece, dy=1):
                        self.current_piece.move(dy=1)
                        self.last_move_time = current_time
                        self.just_moved = True

            for event in pygame.event.get():  # Обробка подій
                if event.type == pygame.QUIT:  # Вихід із гри
                    self.game_over = True
                elif event.type == self.view.FALL_EVENT and not self.paused:  # Подія падіння
                    if not self.board.check_collision(self.current_piece, dy=1):  # Перевірка колізій
                        self.current_piece.move(dy=1)
                        self.lock_time = 0
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
                    if event.key == pygame.K_p:  # Пауза/вихід із паузи
                        self.paused = not self.paused
                        self.lock_time = 0
                    elif not self.paused:
                        if event.key == pygame.K_UP:  # Обертання
                            original_coords = self.current_piece.coordinates
                            original_pos = self.current_piece.position.copy()
                            self.current_piece.coordinates = self.current_piece.rotate()
                            if self.board.check_collision(self.current_piece):
                                self.current_piece.coordinates = original_coords
                                self.current_piece.position = original_pos
                        elif event.key == pygame.K_SPACE:  # Швидке падіння
                            self.drop_piece_to_bottom()
                            self.last_move_time = current_time

            if not self.game_over:
                self.view.draw_pause_on_off(self.paused, self.current_piece, self.board.board, self.score)

        self.show_game_over_screen()  # Показ екрану завершення гри
        pygame.quit()

    def show_game_over_screen(self):
        self.view.draw_game_over_screen()
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