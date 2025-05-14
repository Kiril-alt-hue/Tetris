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
                            (255, 0, 123), (171, 0, 82), (176, 33, 102),
                            (179, 68, 121), (217, 91, 152), (227, 54, 138), (230, 124, 175)
                        ]
                    elif self.start_button.is_clicked(event.pos):
                        return [
                            (214, 21, 21), (214, 92, 21), (235, 208, 9),
                            (25, 150, 3), (20, 140, 204), (5, 61, 181), (122, 5, 181)
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