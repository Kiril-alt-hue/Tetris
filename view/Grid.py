import pygame

class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.GRID_HEIGHT = 650
        self.BLOCK_SIZE = 40

    def draw_grid(self):
        for x in range(0, 600, self.BLOCK_SIZE):
            pygame.draw.line(self.screen, (28, 28, 28), (x, 0), (x, self.GRID_HEIGHT), 3)
        for y in range(0, self.GRID_HEIGHT, self.BLOCK_SIZE):
            pygame.draw.line(self.screen, (28, 28, 28), (0, y), (600, y), 3)

def test_grid():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    grid = Grid(screen)
    grid.draw_grid()
    pygame.display.flip()
    pygame.quit()
    assert grid.GRID_HEIGHT == 650, "GRID_HEIGHT має бути 650"
    assert grid.BLOCK_SIZE == 40, "BLOCK_SIZE має бути 40"
    print("Тест Grid пройдено!")

if __name__ == "__main__":
    test_grid()