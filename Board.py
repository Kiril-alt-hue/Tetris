import pygame
from Piece import Piece

class Board:
    def __init__(self, view):
        self.board = [[0] * 15 for _ in range(20)]
        self.view = view

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
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_y >= 20 or board_x < 0 or board_x > 14:
                piece.position[1] -= 1
                return self.lock_piece(piece)
            if board_y >= 0 and self.board[board_y][board_x] != 0:
                piece.position[1] -= 1
                return self.lock_piece(piece)
        for x, y in piece.coordinates:
            board_x = px + x
            board_y = py + y
            if board_y >= 0 and board_y < 20 and board_x >= 0 and board_x < 15:
                self.board[board_y][board_x] = 1

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(cell != 0 for cell in row)]
        if lines_to_clear:
            for _ in range(5):  # 5 кроків анімації
                for y in lines_to_clear:
                    for x in range(15):
                        if self.board[y][x]:
                            pygame.draw.rect(self.view.screen, (255, 255, 255),
                                           (x * self.view.BLOCK_SIZE, y * self.view.BLOCK_SIZE, self.view.BLOCK_SIZE, self.view.BLOCK_SIZE))
                pygame.display.flip()
                pygame.time.delay(100)
            new_board = [row for i, row in enumerate(self.board) if i not in lines_to_clear]
            lines_cleared = 20 - len(new_board)
            while len(new_board) < 20:
                new_board.insert(0, [0] * 15)
            self.board = new_board
            return lines_cleared
        return 0

    def is_game_over(self, piece):
        return self.check_collision(piece)