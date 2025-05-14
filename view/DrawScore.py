import pygame

class DrawScore:
    def __init__(self, screen):
        self.screen = screen

    def draw_score(self, score):
        font = pygame.font.SysFont( 'jokerman', 50)
        score_text = font.render(f"{score}", True, (255, 194, 236))
        self.screen.blit(score_text, (400, 655))


if __name__ == "__main__":
    #TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    clock = pygame.time.Clock()

    score_drawer = DrawScore(screen)

    test_scores = [0, 52, 100, 1488, 9000, 90000]
    current_score_index = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_score_index = (current_score_index + 1) % len(test_scores)
                    print(f"Змінено рахунок на: {test_scores[current_score_index]}")
                elif event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))

        score_drawer.draw_score(test_scores[current_score_index])


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print("Тестування успішно завершено!")