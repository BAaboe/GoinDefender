import pygame
import Window
import Game
import Character


class Enemies:
    def __init__(self, game):
        self.enemies = []
        self.game = game
        self.numOfEnemies = 0

    def update(self):
        for i in self.enemies:
            i.update()

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
        if self.hp == 0:
            self.game.enemys.removeEnemy(self)

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
                    self.game.player.score += 1
                    if self.hp == 0:
                        self.die()
                    else:
                        pygame.mixer.Sound.play(self.hurtSound)
                        self.game.joystick.rumble(0.5, 0.5, 100)

    def die(self):
        pygame.mixer.Sound.play(self.explosionSound)
