import pygame


class Window:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.width = 800
        self.height = 600

        self.key_pressed = []

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Goin Invader")

        self.FPS = 30
        self.time = pygame.time.Clock()
        self.timeMs = 0
        self.timeS = 0

    def display_text(self, size, text, color, x, y):
        font = pygame.font.Font("../assets/NotoSans-Regular.ttf", size)
        textObj = font.render(text, True, color)
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        self.window.blit(textObj, textRect)
