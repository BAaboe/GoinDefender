import pygame
from pygame.locals import *
import Window
import Character
import Lasesrs
import Game


class Player(Character.Character):
    def __init__(self, game: Game.Game, x, y):
        self.hp = 5
        self.score = 0
        self.insane = 1
        self.movSpeed = 5
        self.direction = "right"

        self.shootSpeed = 2

        self.lastShot = 0

        super().__init__(game, pygame.image.load(f"../assets/bard{self.insane}.png"), x, y, 30, 30)

    def update(self):
        if self.wd.key_pressed[K_a]:
            self.xSpeed = -self.movSpeed
            if self.direction != "left":
                self.img = pygame.transform.flip(self.img, True, False)
                self.direction = "left"
        elif self.wd.key_pressed[K_d]:
            self.xSpeed = self.movSpeed
            if self.direction != "right":
                self.img = pygame.transform.flip(self.img, True, False)
                self.direction = "right"
        else:
            self.xSpeed = 0

        if self.wd.key_pressed[K_w]:
            self.ySpeed = self.movSpeed
        elif self.wd.key_pressed[K_s]:
            self.ySpeed = -self.movSpeed
        else:
            self.ySpeed = 0

        if self.wd.key_pressed[K_SPACE]:
            if self.wd.timeS-self.lastShot > self.shootSpeed:
                self.lasers.addLaser(self.x, self.y)
                self.lastShot = self.wd.timeS

        self.lasers.update()
        super().update()
