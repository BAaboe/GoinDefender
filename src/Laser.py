import pygame
import Window
from src import Game


class Laser:
    def __init__(self, game: Game.Game, x, y):
        self.game = game
        self.wd = self.game.wd

        self.x = x
        self.y = y
        self.width = 9
        self.height = 12

        self.ySpeed = 7

        self.img = pygame.image.load("../assets/RedLaser.png")

    def draw(self):
        self.wd.window.blit(self.img, (self.x, self.y))

    def update(self):
        self.y -= self.ySpeed
        self.draw()
