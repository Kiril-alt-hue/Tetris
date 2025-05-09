# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pygame

class GameOverScreen:
    def __init__(self, view):
        self.view = view

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.view.score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        self.view.screen.fill((33, 33, 33))
        self.view.screen.blit(game_over_text, (150, 300))
        self.view.screen.blit(score_text, (150, 350))
        self.view.screen.blit(restart_text, (150, 400))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.view.__init__()
                        self.view.run()
                        return
        pygame.quit()

def test_game_over_screen():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))

    class MockView:
        def __init__(self):
            self.screen = screen
            self.score = 100

        def run(self):
            pass

    view = MockView()
    game_over_screen = GameOverScreen(view)
    game_over_screen.show_game_over_screen()
    pygame.quit()
    assert game_over_screen.view == view, "View має бути правильно ініціалізованим"
    print("Тест GameOverScreen пройдено!")

if __name__ == "__main__":
    test_game_over_screen()