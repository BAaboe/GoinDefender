import pygame
from pygame.locals import *
import Window
import Character
import Lasesrs
import Game


class Player(Character.Character):
    def __init__(self, game, x, y):
        self.hp = 5
        self.score = 0
        self.insane = 1
        self.movSpeed = 10
        self.direction = "right"

        self.shootSpeed = 2

        self.lastShot = 0
        self.shootSound = pygame.mixer.Sound("../assets/laserShoot.wav")

        super().__init__(game, pygame.image.load(f"../assets/bard{self.insane}.png"), x, y, 30, 30)

    def update(self):
        if self.wd.key_pressed[K_a]:
            if self.x <= 0:
                self.xSpeed = 0
            else:
                self.xSpeed = -self.movSpeed
                if self.direction != "left":
                    self.img = pygame.transform.flip(self.img, True, False)
                    self.direction = "left"
        elif self.wd.key_pressed[K_d]:
            if self.x+self.width >= self.wd.width:
                self.xSpeed = 0
            else:
                self.xSpeed = self.movSpeed
                if self.direction != "right":
                    self.img = pygame.transform.flip(self.img, True, False)
                    self.direction = "right"
        else:
            self.xSpeed = 0

        if self.wd.key_pressed[K_w]:
            if self.y <= 0:
                self.ySpeed = 0
            else:
                self.ySpeed = self.movSpeed
        elif self.wd.key_pressed[K_s]:
            if self.y+self.height >= self.wd.height:
                self.ySpeed = 0
            else:
                self.ySpeed = -self.movSpeed
        else:
            self.ySpeed = 0

        if self.wd.key_pressed[K_SPACE]:
            if self.wd.timeS-self.lastShot > self.shootSpeed:
                self.game.lasers.addLaser(self.x+self.width/2, self.y)
                pygame.mixer.Sound.play(self.shootSound)
                self.lastShot = self.wd.timeS

        if self.wd.key_pressed[K_f]:
            self.game.overlay.addHeart()

        self.game .lasers.update()
        super().update()
