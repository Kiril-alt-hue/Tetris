import pygame

class Platform:
    def __init__(self, screen):
        self.screen = screen
        self.GRID_HEIGHT = 650

    def draw_platform(self):
        pygame.draw.rect(self.screen, (50, 50, 50), (0, self.GRID_HEIGHT, 600, 150))
        pygame.draw.rect(self.screen, (255, 194, 236), (0, self.GRID_HEIGHT, 600, 150), 3)


if __name__ == "__main__":
    #TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Тест сітки")
    clock = pygame.time.Clock()

    platform = Platform(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))

        platform.draw_platform()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print("Тестування успішно завершено!")