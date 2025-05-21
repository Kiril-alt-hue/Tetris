import sys
import pygame
from sound.SoundManager import SoundManager
from view.DrawBoard import DrawBoard
from view.DrawPauseOnOff import DrawPauseOnOff
from view.DrawPiece import DrawPiece
from view.DrawScore import DrawScore
from view.GameOverScreen import GameOverScreen
from view.Grid import Grid
from view.Platform import Platform
from view.DrawTimer import DrawTimer
from Board import Board
from mechanika.KeyHoldHandler import KeyHoldHandler
from mechanika.KeyPressHandler import KeyPressHandler
from gameMain.SpawnPiece import SpawnPiece, SpawnNextPiece
from gameMain.ThemeSelection import ThemeSelection
from gameMain.Timer import Timer

def initialize_game(screen):
    BLOCK_SIZE = 40
    grid = Grid(screen)
    platform = Platform(screen)
    board = Board(screen, BLOCK_SIZE)
    key_hold_handler = KeyHoldHandler(board)
    draw_piece = DrawPiece(screen)
    draw_next_piece = DrawPiece(screen)
    draw_board = DrawBoard(screen, BLOCK_SIZE)
    draw_score = DrawScore(screen)
    draw_timer = DrawTimer(screen)
    draw_pause = DrawPauseOnOff(screen, grid, draw_piece, draw_next_piece, draw_board, platform, draw_score, draw_timer)
    return grid, platform, board, key_hold_handler, draw_pause

def run_game(screen, theme_colors, theme_selection, clock, sound_manager):
    grid, platform, board, key_hold_handler, draw_pause = initialize_game(screen)
    spawner = SpawnPiece(theme_colors)
    spawner_new = SpawnNextPiece(theme_colors)
    current_piece = spawner.spawn_piece()
    new_piece = spawner_new.spawn_piece()
    game_timer = Timer()  # Створення таймера
    game_timer.start()  # Запуск таймера

    game_over = False
    just_moved = False
    paused = False
    last_move_time = 0
    move_delay = 120
    lock_time = 0
    score = 0
    FALL_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(FALL_EVENT, 1000)

    key_press_handler = KeyPressHandler(board)

    while not game_over:
        current_time = pygame.time.get_ticks()
        seconds = game_timer.get_current_time()
        clock.tick(60)

        keys = pygame.key.get_pressed()
        if not paused:
            last_move_time, just_moved = key_hold_handler.handle_key_holds(
                keys, current_piece, current_time, last_move_time, move_delay, just_moved
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == FALL_EVENT and not paused:
                if not board.check_collision(current_piece, dy=1):
                    current_piece.move(dy=1)
                    lock_time = 0
                else:
                    if lock_time == 0:
                        lock_time = pygame.time.get_ticks()
                    elif pygame.time.get_ticks() - lock_time > 500:
                        board.lock_piece(current_piece)
                        sound_manager.play_drop_sound()
                        pygame.event.pump()
                        lines_cleared = board.clear_lines()
                        if lines_cleared > 0:
                            sound_manager.play_clear_sound()
                        score += lines_cleared * 100
                        current_piece = spawner_new.return_piece()
                        new_piece = spawner_new.spawn_piece()
                        lock_time = 0
                        if board.is_game_over(current_piece):
                            game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True  # Перехід до Game Over
                    break  # Вихід із циклу подій
                prev_paused = paused  # Зберігаємо попередній стан паузи
                paused, lock_time, drop_triggered = key_press_handler.handle_key_presses(
                    event, current_piece, paused, lock_time
                )
                # Керуємо музикою, якщо стан паузи змінився
                if paused != prev_paused:
                    if paused:
                        sound_manager.pause_music()
                    else:
                        sound_manager.unpause_music()
                if drop_triggered:
                    last_move_time = current_time
            sound_manager.play_next_track(event)

        if not game_over:
            draw_pause.draw_pause_on_off(paused, current_piece, new_piece, board.board, score, seconds)

    game_over_screen = GameOverScreen(screen, score, sound_manager, seconds)
    while True:
        action = game_over_screen.handle_input()
        if action == 'restart':
            sound_manager.stop_music()
            sound_manager.play_game_music()
            return True
        elif action == 'menu':
            sound_manager.stop_music()
            sound_manager.play_menu_music()
            return False
        pygame.time.delay(100)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_icon( pygame.image.load('view/icon.png'))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    sound_manager = SoundManager()
    sound_manager.play_menu_music()

    theme_selection = ThemeSelection(screen, sound_manager)

    while True:
        theme_colors = theme_selection.draw()
        if theme_colors is None:
            break

        while True:
            restart = run_game(screen, theme_colors, theme_selection, clock, sound_manager)
            if not restart:
                break

    pygame.quit()