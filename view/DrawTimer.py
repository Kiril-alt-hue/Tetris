import pygame
from gameMain.Timer import Timer

class DrawTimer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('fonts/jokerman.ttf', 25)
        self.color = (255, 194, 236)
        self.position = (490, 740)

    def draw(self, seconds):
        time_str = Timer.format_time(seconds)
        text_surface = self.font.render(time_str, True, self.color)
        self.screen.blit(text_surface, self.position)


if __name__ == "__main__":
    # Ініціалізація PyGame
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    clock = pygame.time.Clock()

    # Створюємо об'єкти таймера
    game_timer = Timer()
    draw_timer = DrawTimer(screen)

    # Запускаємо таймер
    game_timer.start()

    running = True
    while running:
        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Оновлення екрану
        screen.fill((0, 0, 0))  # Очищаємо екран

        # Отримуємо та відображаємо час
        current_time = game_timer.get_current_time()
        draw_timer.draw(current_time)

        # Оновлюємо відображення
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()