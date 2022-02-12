import pygame
import Window
import Game


class Laser:
    def __init__(self, game, x, y):
        self.game = game
        self.wd = self.game.wd

        self.x = x
        self.y = y
        self.width = 9
        self.height = 12

        self.ySpeed = 12

        self.img = pygame.image.load("../assets/BlueLaser.png")

    def draw(self):
        self.wd.window.blit(self.img, (self.x, self.y))

    def update(self):
        self.y -= self.ySpeed
        self.draw()
