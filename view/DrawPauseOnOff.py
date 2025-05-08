
class DrawPauseOnOff:
    def __init__(self, screen):
        self.screen = screen
        self.GRID_HEIGHT = 650

    def draw_pause_on_off(self, paused, piece, board, score):
        if not paused:  # Малювання гри
            self.screen.fill((33, 33, 33))
            self.screen.set_clip(0, 0, 600, self.GRID_HEIGHT)
            self.draw_grid()
            self.draw_piece(piece)
            self.draw_board(board)
            self.screen.set_clip(None)
            self.draw_platform()
            self.draw_score(score)
        else:  # Малювання паузи
            font = pygame.font.Font(None, 48)
            pause_text = font.render("Paused", True, (255, 255, 255))
            self.screen.blit(pause_text, (250, 400))
        pygame.display.flip()