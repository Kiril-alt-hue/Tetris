import pygame

class Button:
    def __init__(self, size : list, color, text):
        self.x = size[0]
        self.y = size[1]
        self.w = size[2]
        self.h = size[3]
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)