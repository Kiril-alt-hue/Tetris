from view.Button import Button
import pygame, sys

class ThemeSelection:
    def __init__(self, screen):
        self.screen = screen
        self.start_button = Button([150, 300, 300, 150], (100, 200, 100), "Start Classic Game")
        self.pink_theme_button = Button([150, 470, 300, 100], (255, 105, 180), "Start Pink")
        self.font = pygame.font.SysFont( 'jokerman', 50)
        self.menu_text = self.font.render( "Main Menu", True, (240, 240, 240))  # меню

    def draw(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pink_theme_button.is_clicked(event.pos):
                        return [
                            (255, 182, 193), (255, 192, 203), (255, 105, 180),
                            (255, 20, 147), (219, 112, 147), (199, 21, 133), (255, 0, 127)
                        ]
                    elif self.start_button.is_clicked(event.pos):
                        return [
                            (255, 0, 0), (255, 105, 180), (0, 255, 255),
                            (128, 0, 128), (255, 165, 0), (255, 255, 0), (0, 255, 0)
                        ]
            self.screen.fill((33, 33, 33))
            self.start_button.draw_button(self.screen)
            self.pink_theme_button.draw_button(self.screen)
            self.screen.blit(self.menu_text,(165, 80))
            pygame.display.flip()


if __name__ == "__main__":
    # TEST
    pygame.init()
    screen = pygame.display.set_mode((600, 800))

    running = True
    while running:
        menu = ThemeSelection(screen)
        should_continue = menu.draw()

        if not should_continue:
            running = False

    pygame.quit()