from Piece import *

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_icon(pygame.image.load('icon.png'))
        pygame.display.set_caption("Тетріс")
        self.BLOCK_SIZE = 40
        self.GRID_HEIGHT = 650
        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, 1000)

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
        for y in range(20):
            for x in range(15):  # Змінено з 10 на 15 для відображення повного поля
                if board[y][x]:
                    pygame.draw.rect(
                        self.screen,
                        (200, 200, 50),
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