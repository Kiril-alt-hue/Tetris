import pygame


class Button:
    def __init__(self, size: list, color, text):
        self.x = size[0]
        self.y = size[1]
        self.w = size[2]
        self.h = size[3]
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('impact', 30)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

if __name__ == "__main__":
    #TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    test_button = Button([250, 200, 200, 100], (100, 200, 100), "Test Button")

    running = True
    clicked = False

    while running:
        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if test_button.is_clicked(event.pos):
                    print("Кнопка була натиснута!")
                    clicked = True

        # Отримання позиції миші
        mouse_pos = pygame.mouse.get_pos()

        # Зміна кольору при наведенні
        hover_color = (150, 250, 150) if test_button.rect.collidepoint(mouse_pos) else test_button.color

        # Малювання
        screen.fill((0, 0, 0))
        test_button.color = hover_color  # Тимчасово змінюємо колір для ефекту наведення
        test_button.draw_button(screen)
        test_button.color = (100, 200, 100)  # Повертаємо оригінальний колір

        pygame.display.flip()

    pygame.quit()
    print("Тестування завершено успішно!")