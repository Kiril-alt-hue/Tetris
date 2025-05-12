# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pygame
from view.Button import Button

class DrawMenu:
    def __init__(self, screen):
        self.screen = screen
        self.start_button = Button([200, 300, 200, 150], (100, 200, 100), "Start Game")
        self.pink_theme_button = Button([200, 470, 200, 50], (255, 105, 180), "Start Pink")

    def draw_menu(self):
        self.screen.fill((33, 33, 33))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.start_button.is_clicked(event.pos):
                        return True
                    elif self.pink_theme_button.is_clicked(event.pos):
                        return True
            self.start_button.draw_button(self.screen)
            self.pink_theme_button.draw_button(self.screen)
            pygame.display.flip()
        return False

def test_draw_menu():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    menu = DrawMenu(screen)
    menu.start_button.draw_button(screen)
    pygame.display.flip()
    assert menu.start_button.text == "Start Game", "Кнопка має мати текст 'Start Game'"
    assert menu.start_button.is_clicked((250, 350)) is True, "Кнопка має реагувати на клік у межах"
    pygame.quit()
    print("Тест DrawMenu пройдено!")

if __name__ == "__main__":
    test_draw_menu()