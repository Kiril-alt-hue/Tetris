class Board:
    def __init__(self):
        self.board = [[0] * 15 for _ in range(20)]  # Змінено з 10 на 15 стовпців

    def check_collision(self, piece, dx=0, dy=0):
        px, py = piece.position
        px += dx
        py += dy
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_x < 0 or board_x > 14 or board_y >= 20:  # Змінено з > 9 на > 14
                return True
            if board_y < 0:
                continue
            if self.board[board_y][board_x] != 0:
                return True
        return False

    def lock_piece(self, piece):
        px, py = piece.position
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_y >= 0:
                self.board[board_y][board_x] = 1

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = 20 - len(new_board)
        while len(new_board) < 20:
            new_board.insert(0, [0] * 15)  # Змінено з [0] * 10 на [0] * 15
        self.board = new_board
        return lines_cleared

    def is_game_over(self, piece):
        return self.check_collision(piece)