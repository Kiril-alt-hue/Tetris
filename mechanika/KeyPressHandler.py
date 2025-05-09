import pygame
import asyncio
import platform
from Board import Board
from Piece import SquareShape

class KeyPressHandler:
    def __init__(self, board, view):
        self.board = board
        self.view = view

    def handle_key_presses(self, event, current_piece, paused, lock_time):
        """
        Обробляє натискання клавіш.
        Повертає оновлені paused, lock_time і чи було викликано швидке падіння.
        """
        drop_triggered = False
        if event.key == pygame.K_p:
            paused = not paused
            lock_time = 0
        elif not paused:
            if event.key == pygame.K_UP:
                original_coords = current_piece.coordinates
                original_pos = current_piece.position.copy()
                current_piece.coordinates = current_piece.rotate()
                if self.board.check_collision(current_piece):
                    current_piece.coordinates = original_coords
                    current_piece.position = original_pos
            elif event.key == pygame.K_SPACE:
                self.view.drop_piece_to_bottom()
                drop_triggered = True
        return paused, lock_time, drop_triggered

# Тестові дані
def test_key_press_handler():
    pygame.init()
    screen = pygame.display.set_mode((600, 650))
    board = Board(screen, BLOCK_SIZE=40)

    class MockView:
        def drop_piece_to_bottom(self):
            pass

    view = MockView()
    handler = KeyPressHandler(board, view)
    piece = SquareShape([5, 0], (255, 0, 0))

    class MockEvent:
        def __init__(self, key):
            self.key = key

    event = MockEvent(pygame.K_p)
    paused = False
    lock_time = 100
    paused, lock_time, drop_triggered = handler.handle_key_presses(event, piece, paused, lock_time)
    assert paused is True, "Гра мала перейти в паузу"
    assert lock_time == 0, "lock_time має скинутися"
    assert drop_triggered is False, "Швидке падіння не мало бути викликано"
    pygame.quit()
    print("Тест KeyPressHandler пройдено!")

async def main():
    test_key_press_handler()
    await asyncio.sleep(0.1)  # Minimal delay to ensure tests run

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())