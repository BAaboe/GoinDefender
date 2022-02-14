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
            x = random.randint(0, self.game.wd.width/(30+20))*(30+20)
            y = 50
            level = random.randint(1, self.game.level)
            if self.enemies:
                self.addEnemy(x, y, level)
                for i in self.enemies:
                    if i != self.enemies[-1]:
                        if i.x == self.enemies[-1].x:
                            self.removeEnemy(self.enemies[-1])
            else:
                self.addEnemy(x, y, level)

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

        super().__init__(game, pygame.image.load(f'../assets/goin{game.levelData[str(level)]["imgNum"]}.png'), x, y, 30, 30)

        self.maxHP = self.game.levelData[str(level)]["maxHP"]
        self.hp = self.maxHP

        self.shootSpeed = self.game.levelData[str(level)]["shootSpeed"]
        self.lastShot = 0

        self.chanceOfDDrop = self.game.levelData[str(level)]["chanceOfPowerUp"]

        self.explosionSound = pygame.mixer.Sound("../assets/enemyExplosion.wav")
        self.hurtSound = pygame.mixer.Sound("../assets/hitHurt2.wav")
        self.shootSound = pygame.mixer.Sound("../assets/laserShoot2.wav")

    def update(self):
        if self.wd.timeS-self.lastShot > self.shootSpeed:
            self.shoot()

        self.draw()
        self.check_if_hit()

    def shoot(self):
        self.game.lasers.addLaser(self.x + self.width / 2, self.y, -1, self.game.levelData[str(self.level)]["laserColor"],
                                  self.game.levelData[str(self.level)]["damage"])
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
        self.game.player.score += self.maxHP
        if random.randint(1, 100) <= self.chanceOfDDrop:
            self.drop()

    def drop(self):
        # TODO: Complete this
        pass

    def draw(self):
        super().draw()

        if self.hp != self.maxHP:
            height = self.height/self.maxHP*self.hp
            s = pygame.Surface((self.width, height))
            s.set_alpha(128)
            s.fill((128, 128, 128))
            self.game.wd.window.blit(s, (self.x, self.y+self.height-height))
