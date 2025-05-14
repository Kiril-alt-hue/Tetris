import sys
import os
import pygame
import random

# Імпорти з вашого оновленого коду
from view.DrawBoard import DrawBoard
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
from gameMain.SpawnPiece import SpawnPiece
from gameMain.ThemeSelection import ThemeSelection
from view.GameOverScreen import GameOverScreen

# Функція для ініціалізації гри
def initialize_game(screen):
    BLOCK_SIZE = 40
    grid = Grid(screen)
    platform = Platform(screen)
    board = Board(screen, BLOCK_SIZE)
    key_hold_handler = KeyHoldHandler(board)
    draw_piece = DrawPiece(screen)
    draw_board = DrawBoard(screen, BLOCK_SIZE)
    draw_score = DrawScore(screen)
    draw_pause = DrawPauseOnOff(screen, grid, draw_piece, draw_board, platform, draw_score)
    return grid, platform, board, key_hold_handler, draw_pause

# Функція для запуску одного сеансу гри
def run_game(screen, theme_colors, theme_selection, clock):
    grid, platform, board, key_hold_handler, draw_pause = initialize_game(screen)
    spawner = SpawnPiece(theme_colors)
    current_piece = spawner.spawn_piece()

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
                        score += board.clear_lines() * 100
                        current_piece = spawner.spawn_piece()
                        lock_time = 0
                        if board.is_game_over(current_piece):
                            game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                paused, lock_time, drop_triggered = key_press_handler.handle_key_presses(
                    event, current_piece, paused, lock_time
                )
                if drop_triggered:
                    last_move_time = current_time

        if not game_over:
            draw_pause.draw_pause_on_off(paused, current_piece, board.board, score)

    game_over_screen = GameOverScreen(screen, score)
    while True:
        action = game_over_screen.handle_input()
        if action == 'restart':
            return True
        elif action == 'menu':
            return False
        pygame.time.delay(100)

# Головна програма
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_icon(pygame.image.load('view/icon.png'))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    theme_selection = ThemeSelection(screen)

    while True:  # Outer loop for theme selection
        theme_colors = theme_selection.draw()
        if theme_colors is None:
            break

        while True:  # Inner loop for game sessions
            restart = run_game(screen, theme_colors, theme_selection, clock)
            if not restart:
                break  # Exit to theme selection

    pygame.quit()