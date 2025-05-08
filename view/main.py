import  pygame
from Button import Button
from DrawBoard import DrawBoard
from DrawMenu import DrawMenu
from DrawPauseOnOff import DrawPauseOnOff
from DrawPiece import DrawPiece
from DrawScore import DrawScore
from GameOverScreen import GameOverScreen
from Grid import Grid
from Platform import Platform
from Board import Board
from Piece import Piece
from Mechanika import Mechanika

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('icon.png'))
        pygame.display.set_caption("Тетріс")
        self.BLOCK_SIZE = 40
        self.GRID_HEIGHT = 650
        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, 1500)

        self.board = Board()
        self.score = 0
        self.game_over = False
        self.current_piece = self.spawn_piece()
        self.clock = pygame.time.Clock()
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")
        self.move_delay = 120
        self.last_move_time = 0
        self.just_moved = False
        self.paused = False
        self.lock_time = 0

        # Ініціалізація компонентів інтерфейсу
        self.platform = Platform(self.screen)
        self.grid = Grid(self.screen)
        self.draw_board = DrawBoard(self.screen, self.BLOCK_SIZE)
        self.draw_piece = DrawPiece(self.screen)
        self.draw_score = DrawScore(self.screen)
        self.draw_menu = DrawMenu(self.screen)
        self.draw_pause = DrawPauseOnOff(self.screen)
        self.game_over_screen = GameOverScreen(self.screen, self.draw_score)

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


if __name__ == "__main__":
    game = View()
    game.run()