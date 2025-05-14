import pygame
from gameMain.ThemeSelection import ThemeSelection


class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.SysFont('impact', 40)

        self.game_over_text = self.font.render("Game Over", True, (201, 0, 97))
        self.score_text = self.font.render(f"Final Score: {self.score}", True, (255, 237, 249))
        self.menu_text = self.font.render("Press M to Main Menu", True, (255, 237, 249))
        self.restart_text = self.font.render("Press R to Restart", True, (255, 237, 249))

        self.draw_screen()

    def draw_screen(self):
        self.screen.fill((33, 33, 33))
        self.screen.blit(self.game_over_text, (150, 300))
        self.screen.blit(self.score_text, (150, 350))
        self.screen.blit(self.restart_text, (150, 400))
        self.screen.blit(self.menu_text, (150, 450))
        pygame.display.flip()

    def handle_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return 'restart'
                    elif event.key == pygame.K_m:
                        return 'menu'


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    test_score = 1488
    game_over = GameOverScreen(screen, test_score)
    theme_selection = ThemeSelection(screen)

    running = True
    while running:
        action = game_over.handle_input()

        if action == 'restart':
            print("Restarting game...")
            test_score += 100
            game_over = GameOverScreen(screen, test_score)
        elif action == 'menu':
            print("Returning to menu...")
            theme_selection.draw()

        pygame.time.delay(100)

    pygame.quit()