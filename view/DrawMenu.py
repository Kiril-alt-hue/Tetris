import pygame
from Button import Button


class DrawMenu:
    def __init__(self, screen):
        self.screen = screen
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")

    def draw_menu(self):
        in_menu = True
        while in_menu: # Цикл меню
            self.screen.fill((33, 33, 33)) # Заповнення екрану чорним
            self.start_button.draw_button(self.screen)  # Малювання кнопки
            pygame.display.flip() # Оновлення екрану

            for event in pygame.event.get(): # Обробка подій
                if event.type == pygame.QUIT: # Вихід із гри
                    pygame.quit()
                    return False  #повертаємо False для повного виходу
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_clicked(event.pos):
                        in_menu = False
        return True  #повертаємо True для продовження роботи


if __name__ == "__main__":
    #TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Game Menu")

    running = True
    while running:
        menu = DrawMenu(screen)
        should_continue = menu.draw_menu()

        if not should_continue:
            running = False

    pygame.quit()