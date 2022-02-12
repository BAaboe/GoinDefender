import pygame
import Window
import Game
import Character


class Enemys:
    def __init__(self, game):
        self.enemys = []
        self.game = game

    def update(self):
        for i in self.enemys:
            i.update()

    def draw(self):
        for i in self.enemys:
            i.draw()

    def addEnemy(self, x, y, level):
        self.enemys.append(Enemy(self.game, x, y, level))

    def removeEnemy(self, enemy):
        self.enemys.remove(enemy)


class Enemy(Character.Character):
    def __init__(self, game, x, y, level=1):

        self.level = level

        self.shootSpeed = 9
        self.lastShot = 0

        super().__init__(game, pygame.image.load(f"../assets/goin{self.level}.png"), x, y, 30, 30, self.level)

    def update(self):
        if self.hp == 0:
            self.game.enemys.removeEnemy(self)

        if self.wd.timeS-self.lastShot > self.shootSpeed:
            self.shoot()

        self.draw()



    def shoot(self):
        self.game.lasers.addLaser(self.x + self.width / 2, self.y, -1, "Blue")
        # pygame.mixer.Sound.play(self.shootSound)
        # TODO: fix sound
        self.lastShot = self.wd.timeS
