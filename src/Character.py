import pygame
import Window
import Game


class Character:
    def __init__(self, game, img, x=0, y=0, height=10, width=10):
        self.game = game
        self.wd = game.wd

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.img = img
        self.xSpeed = 0
        self.ySpeed = 0

        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.wd.window.blit(self.img, (self.x, self.y))

    def draw(self):
        self.wd.window.blit(self.img, (self.x, self.y))

    def update(self):
        self.x += self.xSpeed
        self.y -= self.ySpeed
        self.draw()
