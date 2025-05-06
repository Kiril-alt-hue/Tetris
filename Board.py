import pygame

class Board:
    def __init__(self, view):
        self.board = [[0] * 15 for _ in range(16)]  # Ініціалізація дошки 20x15 із нулями
        self.view = view

    def check_collision(self, piece, dx=0, dy=0):
        px, py = piece.position                    # Отримання позиції фігури
        px += dx                                   # Додавання зміщення по x
        py += dy                                   # Додавання зміщення по y
        for x, y in piece.coordinates:             # Перевірка кожної координати фігури
            board_x = px + x                       # Обчислення позиції на дошку по x
            board_y = py + y                       # Обчислення позиції на дошку по y
            if board_x < 0 or board_x > 14 or board_y >= 16:  # Перевірка меж
                return True                        # Повернення True при виході за межі
            if board_y < 0:                        # Ігнорування від'ємних значень y
                continue
            if self.board[board_y][board_x] != 0:  # Перевірка на колізію з фіксованими блоками
                return True
        return False                               # Повернення False, якщо колізії немає

    def lock_piece(self, piece):
        px, py = piece.position                    # Отримання позиції фігури
        for x, y in piece.coordinates:             # Перевірка кожної координати фігури
            board_x = px + x                       # Обчислення позиції на дошку по x
            board_y = py + y                       # Обчислення позиції на дошку по y
            if board_y >= 16 or board_x < 0 or board_x > 14:  # Перевірка верхньої межі (вирішення багу)
                piece.position[1] -= 1              # Підняття фігури на 1 вгору
                return self.lock_piece(piece)       # Рекурсивний виклик
            if board_y >= 0 and self.board[board_y][board_x] != 0:  # Перевірка колізії
                piece.position[1] -= 1              # Підняття фігури на 1 вгору
                return self.lock_piece(piece)       # Рекурсивний виклик
        for x, y in piece.coordinates:             # Фіксація фігури на дошку
            board_x = px + x                       # Обчислення позиції по x
            board_y = py + y                       # Обчислення позиції по y
            if board_y >= 0 and board_y < 20 and board_x >= 0 and board_x < 15:
                self.board[board_y][board_x] = 1   # Позначає клітинку як зайняту

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(cell != 0 for cell in row)]  # Знаходження повних рядків
        if lines_to_clear:
            for _ in range(5):                     # Анімація очищення (5 кадрів)
                for y in lines_to_clear:
                    for x in range(15):
                        if self.board[y][x]:
                            pygame.draw.rect(self.view.screen, (255, 255, 255),  # Малювання білих прямокутників
                                           (x * self.view.BLOCK_SIZE, y * self.view.BLOCK_SIZE, self.view.BLOCK_SIZE, self.view.BLOCK_SIZE))
                pygame.display.flip()               # Оновлення екрану
                pygame.time.delay(100)              # Затримка 100 мс
            new_board = [row for i, row in enumerate(self.board) if i not in lines_to_clear]  # Створення нової дошки
            lines_cleared = 16 - len(new_board)    # Кількість очищених рядків
            while len(new_board) < 16:             # Додавання порожніх рядків зверху (вирішення багу)
                new_board.insert(0, [0] * 15)
            self.board = new_board                 # Оновлення дошки
            return lines_cleared                   # Повернення кількості очищених рядків
        return 0                                   # Повернення 0, якщо рядки не очищені

    def is_game_over(self, piece):
        return self.check_collision(piece)