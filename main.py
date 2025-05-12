import sys
import os
sys.path.append(os.path.dirname(__file__))
import pygame
import random
from view.Button import Button
from view.DrawBoard import DrawBoard
from view.DrawMenu import DrawMenu
from view.DrawPauseOnOff import DrawPauseOnOff
from view.DrawPiece import DrawPiece
from view.DrawScore import DrawScore
from view.GameOverScreen import GameOverScreen
from view.Grid import Grid
from view.Platform import Platform
from Piece import SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape
from Board import Board
from mechanika.KeyHoldHandler import KeyHoldHandler
from mechanika.KeyPressHandler import KeyPressHandler

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('view/icon.png'))
        pygame.display.set_caption("Тетріс")
        self.BLOCK_SIZE = 40
        self.GRID_HEIGHT = 650
        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, 1500)

        self.board = Board(self.screen, self.BLOCK_SIZE)
        self.score = 0
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")
        self.pink_theme_button = Button([200, 470, 200, 50], (255, 105, 180), "Start Pink")
        self.move_delay = 120
        self.last_move_time = 0
        self.just_moved = False
        self.paused = False
        self.lock_time = 0
        self.theme_colors = self.wait_for_theme_selection()
        self.current_piece = self.spawn_piece()

        # Ініціалізація компонентів інтерфейсу
        self.platform = Platform(self.screen)
        self.grid = Grid(self.screen)
        self.draw_board = DrawBoard(self.screen, self.BLOCK_SIZE)
        self.draw_piece = DrawPiece(self.screen)
        self.draw_score = DrawScore(self.screen)
        self.draw_menu = DrawMenu(self.screen)
        self.draw_pause = DrawPauseOnOff(self.screen, self.grid, self.draw_piece, self.draw_board, self.platform, self.draw_score)
        self.game_over_screen = GameOverScreen(self)

        # Ініціалізація обробників клавіш
        self.key_hold_handler = KeyHoldHandler(self.board)
        self.key_press_handler = KeyPressHandler(self.board)

    def wait_for_theme_selection(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pink_theme_button.is_clicked(event.pos):
                        return [
                            (255, 182, 193), (255, 192, 203), (255, 105, 180),
                            (255, 20, 147), (219, 112, 147), (199, 21, 133), (255, 0, 127)
                        ]
                    elif self.start_button.is_clicked(event.pos):
                        return [
                            (255, 0, 0), (255, 105, 180), (0, 255, 255),
                            (128, 0, 128), (255, 165, 0), (255, 255, 0), (0, 255, 0)
                        ]
            self.screen.fill((33, 33, 33))
            self.start_button.draw_button(self.screen)
            self.pink_theme_button.draw_button(self.screen)
            pygame.display.flip()

    def spawn_piece(self):
        shapes = [SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape]
        shape_class = random.choice(shapes)
        shape_color = random.choice(self.theme_colors)
        return shape_class([5, 0], shape_color)

    # def drop_piece_to_bottom(self):
    #     while not self.board.check_collision(self.current_piece, dy=1):
    #         self.current_piece.move(dy=1)
    #     self.board.lock_piece(self.current_piece)
    #     self.score += self.board.clear_lines() * 100
    #     self.current_piece = self.spawn_piece()
    #     if self.board.is_game_over(self.current_piece):
    #         self.game_over = True

    def run(self):
        if not self.draw_menu.draw_menu():
            return

        while not self.game_over:
            current_time = pygame.time.get_ticks()
            self.clock.tick(60)
            self.just_moved = False

            # Обробка утримання клавіш
            keys = pygame.key.get_pressed()
            if not self.paused:
                self.last_move_time, self.just_moved = self.key_hold_handler.handle_key_holds(
                    keys, self.current_piece, current_time, self.last_move_time, self.move_delay, self.just_moved
                )

            # Обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == self.FALL_EVENT and not self.paused:
                    if not self.board.check_collision(self.current_piece, dy=1):
                        self.current_piece.move(dy=1)
                        self.lock_time = 0
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
                    self.paused, self.lock_time, drop_triggered = self.key_press_handler.handle_key_presses(
                        event, self.current_piece, self.paused, self.lock_time
                    )
                    if drop_triggered:
                        self.last_move_time = current_time

            if not self.game_over:
                self.draw_pause.draw_pause_on_off(self.paused, self.current_piece, self.board.board, self.score)

        self.game_over_screen.show_game_over_screen()

def test_view():
    pygame.init()
    view = View()
    assert view.BLOCK_SIZE == 40, "BLOCK_SIZE має бути 40"
    assert view.GRID_HEIGHT == 650, "GRID_HEIGHT має бути 650"
    assert isinstance(view.board, Board), "board має бути екземпляром Board"
    assert isinstance(view.current_piece, (SquareShape, TShape, StairShape1, StairShape2, LShape1, LShape2, LineShape)), "current_piece має бути фігурою"
    pygame.quit()
    print("Тест View пройдено!")

if __name__ == "__main__":
    game = View()
    game.run()