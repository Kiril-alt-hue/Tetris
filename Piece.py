import pygame

class Piece:
    def __init__(self, coordinates: list, position: list, color):
        self.coordinates = coordinates
        self.position = position
        self.color = color

    def draw(self, surface, block_size):
        px, py = self.position
        for dx, dy in self.coordinates:
            x = (px + dx) * block_size
            y = (py + dy) * block_size
            pygame.draw.rect(surface, self.color, (x, y, block_size, block_size))
            pygame.draw.rect(surface, (0, 0, 0), (x, y, block_size, block_size), 2)

    def rotate(self, n=1):
        """Повертає координати фігури після повороту на 90*n градусів (за годинниковою стрілкою)."""
        n = n % 4  # Оскільки поворот на 360° дає те саме, що й 0°
        for _ in range(n):
            self.coordinates = [(-y, x) for x, y in self.coordinates]
        return self.coordinates

    def move(self, dx=0, dy=1):
        self.position[0] += dx
        self.position[1] += dy

    def diagonal_right(self):
        self.move(dx=1, dy=1)

    def diagonal_left(self):
        self.move(dx=-1, dy=1)


class SquareShape(Piece):
    def __init__(self, position: list, color):
        coordinates = [(0, 0), (1, 0), (0, 1), (1, 1)]
        super().__init__(coordinates, position, color)

    def rotate(self, n=1):
        return self.coordinates


class TShape(Piece):
    def __init__(self, position: list, color):
        coordinates = [(0, -1), (-1, 0), (0, 0), (1, 0)]
        super().__init__(coordinates, position, color)


class StairShape1(Piece):
    def __init__(self, position: list, color):
        coordinates = [(-1, -1), (0, -1), (0, 0), (1, 0)]
        super().__init__(coordinates, position, color)


class StairShape2(Piece):
    def __init__(self, position: list, color):
        coordinates = [(1, -1), (0, -1), (0, 0), (-1, 0)]
        super().__init__(coordinates, position, color)


class LShape1(Piece):
    def __init__(self, position: list, color):
        coordinates = [(-1, 0), (0, 0), (1, 0), (1, -1)]
        super().__init__(coordinates, position, color)


class LShape2(Piece):
    def __init__(self, position: list, color):
        coordinates = [(-1, -1), (-1, 0), (0, 0), (1, 0)]
        super().__init__(coordinates, position, color)


class LineShape(Piece):
    def __init__(self, position: list, color):
        coordinates = [(-2, 0), (-1, 0), (0, 0), (1, 0)]
        super().__init__(coordinates, position, color)