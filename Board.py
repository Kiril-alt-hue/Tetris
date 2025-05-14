import pygame

class Board:
    def __init__(self, screen, BLOCK_SIZE=40):
        self.board = [[0] * 15 for _ in range(16)]  # Ініціалізація дошки 16x15 із нулями
        self.screen = screen
        self.BLOCK_SIZE = BLOCK_SIZE

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
                self.board[board_y][board_x] = piece.color   # Позначає клітинку як зайняту

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(cell != 0 for cell in row)]  # Знаходження повних рядків
        if lines_to_clear:
            for _ in range(5):                     # Анімація очищення (5 кадрів)
                for y in lines_to_clear:
                    for x in range(15):
                        if self.board[y][x]:
                            pygame.draw.rect(self.screen, (255, 194, 236),  # Малювання білих прямокутників, тепер рожевий
                                           (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
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

#додала новий метод

    def draw(self, piece):
        for y in range(16):
            for x in range(15):
                if self.board[y][x]:
                    pygame.draw.rect(self.screen, self.board[y][x],
                                     (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
        px, py = piece.position
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_y >= 0 and board_y < 16 and board_x >= 0 and board_x < 15:
                pygame.draw.rect(self.screen, piece.color,
                                 (board_x * self.BLOCK_SIZE, board_y * self.BLOCK_SIZE, self.BLOCK_SIZE,
                                  self.BLOCK_SIZE))


if __name__ == "__main__":
    #TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 650))
    BLOCK_SIZE = 40

    board = Board(screen, BLOCK_SIZE)


    # Тестовий клас фігури
    class TestPiece:
        def __init__(self, position, coordinates, color):
            self.position = position
            self.coordinates = coordinates
            self.color = color


    print("Початок тестування класу Board:")

    # Тест 1: Перевірка колізій
    test_piece1 = TestPiece([5, 5], [(0, 0), (1, 0), (0, 1), (1, 1)], (255, 0, 0))  # Квадрат 2x2
    print("1. Тест check_collision():", "Пройдено" if not board.check_collision(test_piece1) else "Не пройдено")

    # Тест 2: Перевірка фіксації фігури
    board.lock_piece(test_piece1)
    print("2. Тест lock_piece():", "Пройдено" if board.board[5][5] != 0 else "Не пройдено")

    # Тест 3: Перевірка очищення рядків
    # Заповнюємо рядок для очищення
    for x in range(15):
        board.board[10][x] = (0, 255, 0)
    lines_cleared = board.clear_lines()
    print("3. Тест clear_lines():",
          f"Пройдено ({lines_cleared} рядків очищено)" if lines_cleared > 0 else "Не пройдено")

    # Тест 4: Перевірка кінця гри
    test_piece2 = TestPiece([5, 0], [(0, 0), (1, 0), (0, 1), (1, 1)], (0, 0, 255))
    print("4. Тест is_game_over():", "Пройдено" if not board.is_game_over(test_piece2) else "Не пройдено")

    # Візуалізація дошки для наглядності
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Відображення дошки
        screen.fill((0, 0, 0))
        for y in range(16):
            for x in range(15):
                if board.board[y][x]:
                    pygame.draw.rect(screen, board.board[y][x],
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()

    pygame.quit()
    print("Тестування завершено!")