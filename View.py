import pygame

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('icon.png'))
        pygame.display.set_caption("Тетріс")
        self.BLOCK_SIZE = 40
        self.GRID_HEIGHT = 650
        self.FALL_EVENT = pygame.USEREVENT + 1
        self.score = 0
        # self.paused = False
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")
        pygame.time.set_timer(self.FALL_EVENT, 1500)

    def draw_menu(self):
        in_menu = True
        while in_menu:  # Цикл меню
            self.screen.fill((33, 33, 33))  # Заповнення екрану чорним
            self.start_button.draw_button(self.screen)  # Малювання кнопки
            pygame.display.flip()  # Оновлення екрану

            for event in pygame.event.get():  # Обробка подій
                if event.type == pygame.QUIT:  # Вихід із гри
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Натискання миші
                    if self.start_button.is_clicked(event.pos):  # Початок гри
                        in_menu = False

    def draw_grid(self):
        #сітка
        for x in range(0, 600, self.BLOCK_SIZE):
            pygame.draw.line(self.screen, (28, 28, 28), (x, 0), (x, self.GRID_HEIGHT), 3) #змінила товщину на 3
        for y in range(0, self.GRID_HEIGHT, self.BLOCK_SIZE):
            pygame.draw.line(self.screen, (28, 28, 28), (0, y), (600, y), 3) #змінила товщину на 3

    def draw_platform(self):
        #платформа
        pygame.draw.rect(self.screen, (50, 50, 50), (0, self.GRID_HEIGHT, 600, 150))
        pygame.draw.rect(self.screen, (255, 194, 236), (0, self.GRID_HEIGHT, 600, 150), 3)

    def draw_piece(self, piece):
        px, py = piece.position
        for dx, dy in piece.coordinates:
            x = (px + dx) * self.BLOCK_SIZE
            y = (py + dy) * self.BLOCK_SIZE
            # Малюємо лише в межах GRID_HEIGHT
            if 0 <= y < self.GRID_HEIGHT and 0 <= x < 600:
                pygame.draw.rect(self.screen, piece.color, (x, y, self.BLOCK_SIZE, self.BLOCK_SIZE))
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.BLOCK_SIZE, self.BLOCK_SIZE), 2)

    def draw_board(self, board):
        for y in range(16): # Можливе вирішення багу (воно працює!!!)
            for x in range(15):  # Змінено з 10 на 15 для відображення повного поля
                if board[y][x] != 0:
                    pygame.draw.rect(
                        self.screen,
                        board[y][x],
                        (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
                    )
                    pygame.draw.rect(
                        self.screen,
                        (0, 0, 0),
                        (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE),
                        2
                    )

    def draw_score(self, score):
        font = pygame.font.Font(None, 90)
        score_text = font.render(f"{score}", True, (255, 194, 236))
        self.screen.blit(score_text, (400, 655)) #змінено для виводу

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

    def draw_game_over_screen(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        self.screen.fill((33, 33, 33))  # Заповнення екрану
        self.screen.blit(game_over_text, (150, 300))
        self.screen.blit(score_text, (150, 350))
        self.screen.blit(restart_text, (150, 400))
        pygame.display.flip()


class Button:
    def __init__(self, size : list, color, text):
        self.x = size[0]
        self.y = size[1]
        self.w = size[2]
        self.h = size[3]
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)