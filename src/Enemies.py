import pygame
import Window
import Game
import Character


class Enemies:
    def __init__(self, game):
        self.enemies = []
        self.game = game

    def update(self):
        for i in self.enemies:
            i.update()

    def draw(self):
        for i in self.enemies:
            i.draw()

    def addEnemy(self, x, y, level):
        self.enemies.append(Enemy(self.game, x, y, level))

    def removeEnemy(self, enemy):
        self.enemies.remove(enemy)


class Enemy(Character.Character):
    def __init__(self, game, x, y, level=1):

        self.level = level

        self.shootSpeed = 9
        self.lastShot = 0

        super().__init__(game, pygame.image.load(f"../assets/goin{self.level}.png"), x, y, 30, 30, self.level)

    def update(self):
        if self.hp == 0:
            self.game.enemies.removeEnemy(self)

        if self.wd.timeS-self.lastShot > self.shootSpeed:
            self.shoot()

        self.draw()



    def shoot(self):
        self.game.lasers.addLaser(self.x + self.width / 2, self.y, -1, "Blue")
        # pygame.mixer.Sound.play(self.shootSound)
        # TODO: fix sound
        self.lastShot = self.wd.timeS
