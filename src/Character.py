import pygame
import Window

class Charecter:
    def __init__(self, wd: Window.Window, x = 0, y = 0, height = 10, width=10, img):
        self.wd = Window

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.img = img

        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def draw(self):
        self.wd.window.blit(self.image, (self.x, self.y))

    def update(self):
        self.draw()