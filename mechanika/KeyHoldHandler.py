import pygame
import asyncio
import platform
from Board import Board
from Piece import SquareShape

class KeyHoldHandler:
    def __init__(self, board):
        self.board = board

    def handle_key_holds(self, keys, current_piece, current_time, last_move_time, move_delay, just_moved):
        """
        Обробляє утримання клавіш для руху фігури.
        Повертає оновлені last_move_time і just_moved.
        """
        if current_time - last_move_time > move_delay:
            if keys[pygame.K_LEFT]:
                if not self.board.check_collision(current_piece, dx=-1):
                    current_piece.move(dx=-1)
                    last_move_time = current_time
                    just_moved = True
            if keys[pygame.K_RIGHT]:
                if not self.board.check_collision(current_piece, dx=1):
                    current_piece.move(dx=1)
                    last_move_time = current_time
                    just_moved = True
            if keys[pygame.K_DOWN]:
                if not self.board.check_collision(current_piece, dy=1):
                    current_piece.move(dy=1)
                    last_move_time = current_time
                    just_moved = True
        return last_move_time, just_moved

# Тестові дані
def test_key_hold_handler():
    pygame.init()
    screen = pygame.display.set_mode((600, 650))
    board = Board(screen, BLOCK_SIZE=40)
    handler = KeyHoldHandler(board)
    piece = SquareShape([5, 0], (255, 0, 0))
    keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_DOWN: False}
    current_time = 1000
    last_move_time = 800
    move_delay = 120
    just_moved = False
    last_move_time, just_moved = handler.handle_key_holds(keys, piece, current_time, last_move_time, move_delay, just_moved)
    assert piece.position[0] == 4, "Фігура мала зрушити вліво"
    assert just_moved is True, "just_moved має бути True після руху"
    assert last_move_time == 1000, "last_move_time має оновитися"
    pygame.quit()
    print("Тест KeyHoldHandler пройдено!")

async def main():
    test_key_hold_handler()
    await asyncio.sleep(0.1)  # Minimal delay to ensure tests run

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())