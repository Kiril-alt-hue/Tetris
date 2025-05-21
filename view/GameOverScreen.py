import pygame
from gameMain.ThemeSelection import ThemeSelection

class GameOverScreen:
    def __init__(self, screen, score, sound_manager, secounds):
        self.screen = screen
        self.score = score
        self.sound_manager = sound_manager
        self.total_seconds = secounds
        self.font = pygame.font.SysFont('impact', 40)

        minutes = int(self.total_seconds // 60)
        seconds_remaining = self.total_seconds % 60
        # Форматуємо час у вигляді "хвилини:секунди.десята"
        formatted_time = f"{minutes}:{seconds_remaining:02.0f}"

        self.game_over_text = self.font.render("Game Over", True, (201, 0, 97))
        self.score_text = self.font.render(f"Final Score: {self.score}", True, (255, 237, 249))
        self.time_text = self.font.render(f"Game time: {formatted_time}", True, (255, 237, 249))  # Використовуємо відформатований час
        self.menu_text = self.font.render("Press M to Main Menu", True, (255, 237, 249))
        self.restart_text = self.font.render("Press R to Restart", True, (255, 237, 249))

        self.sound_manager.stop_music()
        self.sound_manager.play_game_over_music()
        self.draw_screen()

    def draw_screen(self):
        self.screen.fill((33, 33, 33))
        self.screen.blit(self.game_over_text, (150, 300))
        self.screen.blit(self.score_text, (150, 350))
        self.screen.blit(self.time_text, (150, 400))  # Відображаємо час
        self.screen.blit(self.restart_text, (150, 450))
        self.screen.blit(self.menu_text, (150, 500))
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                elif event.key == pygame.K_m:
                    return 'menu'
        return None