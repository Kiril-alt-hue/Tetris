
class GameOverScreen:
    def __init__(self, view, score):
        self.view = view
        self.score = score


    def show_game_over_screen(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        self.view.screen.fill((33, 33, 33))  # Заповнення екрану
        self.view.screen.blit(game_over_text, (150, 300))
        self.view.screen.blit(score_text, (150, 350))
        self.view.screen.blit(restart_text, (150, 400))
        pygame.display.flip()
        waiting = True
        while waiting:  # Цикл очікування перезапуску
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Вихід
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Перезапуск
                        self.__init__()
                        self.run()
                        return