import pygame

class DrawScore:
    def __init__(self, screen):
        self.screen = screen

    def draw_score(self, score):
        font = pygame.font.Font(None, 90)
        score_text = font.render(f"{score}", True, (255, 194, 236))
        self.screen.blit(score_text, (400, 655)) #змінено для виводу