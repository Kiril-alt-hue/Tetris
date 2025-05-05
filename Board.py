class Board:
    def __init__(self):
        self.board = [[0] * 15 for _ in range(20)]

    def check_collision(self, piece, dx=0, dy=0):
        px, py = piece.position
        px += dx
        py += dy
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_x < 0 or board_x > 14 or board_y >= 20:
                return True
            if board_y < 0:
                continue
            if self.board[board_y][board_x] != 0:
                return True
        return False

    def lock_piece(self, piece):
        px, py = piece.position


        # Перевірити, чи шматок у валідній позиції
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_y >= 20 or board_x < 0 or board_x > 14:
                # Якщо шматок виходить за межі, підняти його вгору
                piece.position[1] -= 1
                return self.lock_piece(piece)
            if board_y >= 0 and self.board[board_y][board_x] != 0:
                # Якщо є перекриття з іншими клітинками, підняти шматок
                piece.position[1] -= 1
                return self.lock_piece(piece)


        # Фіксація шматка
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_y >= 0 and board_y < 20 and board_x >= 0 and board_x < 15:
                self.board[board_y][board_x] = 1

    def clear_lines(self):
        new_board = [row for row in self.board if not all(cell != 0 for cell in row)]
        lines_cleared = 20 - len(new_board)
        while len(new_board) < 20:
            new_board.insert(0, [0] * 15)
        self.board = new_board
        return lines_cleared

    def is_game_over(self, piece):
        return self.check_collision(piece)