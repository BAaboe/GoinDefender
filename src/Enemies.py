import pygame
import Window
import Game
import Character
import random


class Enemies:
    def __init__(self, game):
        self.enemies = []
        self.game = game
        self.numOfEnemies = 0
        self.maxEnemies = 5

    def update(self):
        for i in self.enemies:
            i.update()
        if self.numOfEnemies < self.maxEnemies:
            if self.enemies:
                self.addEnemy(random.randint(0, self.game.wd.width/(self.enemies[-1].width+20))*(self.enemies[-1].width+20), 50., 1)
            else:
                self.addEnemy(20, 50, 1)

    def draw(self):
        for i in self.enemies:
            i.draw()

    def addEnemy(self, x, y, level):
        self.enemies.append(Enemy(self.game, x, y, level))
        self.numOfEnemies += 1

    def removeEnemy(self, enemy):
        self.enemies.remove(enemy)
        self.numOfEnemies -= 1


class Enemy(Character.Character):
    def __init__(self, game, x, y, level=1):

        self.level = level

        self.shootSpeed = 9
        self.lastShot = 0

        self.explosionSound = pygame.mixer.Sound("../assets/enemyExplosion.wav")
        self.hurtSound = pygame.mixer.Sound("../assets/hitHurt2.wav")
        self.shootSound = pygame.mixer.Sound("../assets/laserShoot2.wav")

        super().__init__(game, pygame.image.load(f"../assets/goin{self.level}.png"), x, y, 30, 30, 5)

    def update(self):
        if self.wd.timeS-self.lastShot > self.shootSpeed:
            self.shoot()

        self.draw()
        self.check_if_hit()

    def shoot(self):
        self.game.lasers.addLaser(self.x + self.width / 2, self.y, -1, "Blue")
        pygame.mixer.Sound.play(self.shootSound)
        self.lastShot = self.wd.timeS

    def check_if_hit(self):
        selfHitBox = pygame.Rect((self.x, self.y), (self.width, self.height))
        for laser in self.game.lasers.lasers:
            laserHitBox = pygame.Rect((laser.x, laser.y), (laser.width, laser.height))
            if selfHitBox.colliderect(laserHitBox):
                if laser.yDir == 1:
                    self.hp -= 1
                    self.game.lasers.removeLaser(laser)
                    if self.hp == 0:
                        self.die()
                    else:
                        pygame.mixer.Sound.play(self.hurtSound)

    def die(self):
        self.game.enemies.removeEnemy(self)
        pygame.mixer.Sound.play(self.explosionSound)
        self.game.player.score += self.level*5
