import pygame
from pygame.locals import *
import Window
import Character
import Lasesrs
import Game


class Player(Character.Character):
    def __init__(self, game, x, y):
        self.score = 0
        self.insane = 1
        self.movSpeed = 10
        self.direction = "right"

        self.shootSpeed = 4

        self.lastShot = 0

        self.shootSound = pygame.mixer.Sound("../assets/laserShoot.wav")
        self.hurtSound = pygame.mixer.Sound("../assets/hitHurt.wav")
        self.explosionSound = pygame.mixer.Sound("../assets/explosion.wav")

        self.dead = 0

        super().__init__(game, pygame.image.load(f"../assets/bard{self.insane}.png"), x, y, 30, 30, 5)

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

        """if self.wd.key_pressed[K_w]:
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
            self.ySpeed = 0"""

        if self.wd.key_pressed[K_SPACE]:
            if self.wd.timeS-self.lastShot > self.shootSpeed:
                self.shoot()

        if self.game.joystickConnected:
            leftStickAxis = self.game.joystick.get_axis(0)
            if -0.5 > leftStickAxis >= -1:
                if self.x <= 0:
                    self.xSpeed = 0
                else:
                    self.xSpeed = -self.movSpeed
                    if self.direction != "left":
                        self.img = pygame.transform.flip(self.img, True, False)
                        self.direction = "left"
            elif 1 > leftStickAxis > 0.5:
                if self.x + self.width >= self.wd.width:
                    self.xSpeed = 0
                else:
                    self.xSpeed = self.movSpeed
                    if self.direction != "right":
                        self.img = pygame.transform.flip(self.img, True, False)
                        self.direction = "right"

            """if 0.5 > leftStickAxis > -0.5:
                if self.y <= 0:
                    self.ySpeed = 0
                else:
                    self.ySpeed = self.movSpeed"""

            if self.game.joystick.get_button(0) or self.game.joystick.get_button(7):
                if self.wd.timeS - self.lastShot > self.shootSpeed:
                    self.shoot()

        self.check_if_hit()
        super().update()

    def shoot(self):
        self.game.lasers.addLaser(self.x + self.width / 2, self.y, 1)
        pygame.mixer.Sound.play(self.shootSound)
        self.lastShot = self.wd.timeS

    def check_if_hit(self):
        playerHitBox = pygame.Rect((self.x, self.y), (self.width, self.height))
        for laser in self.game.lasers.lasers:
            laserHitBox = pygame.Rect((laser.x, laser.y), (laser.width, laser.height))
            if playerHitBox.colliderect(laserHitBox):
                if laser.yDir == -1:
                    self.hp -= 1
                    self.game.lasers.removeLaser(laser)
                    if self.hp == 0:
                        self.game.joystick.rumble(1, 1, 100)
                        self.die()
                    else:
                        pygame.mixer.Sound.play(self.hurtSound)
                        self.game.joystick.rumble(0.5, 0.5, 100)

    def die(self):
        pygame.mixer.Sound.play(self.explosionSound)
        self.game.overlay.removeText("score")
        self.game.overlay.addText("Game Over", self.wd.width/2, self.wd.height/2-50, 100, self.game.wd.WHITE, "game_over")
        self.dead = 1
