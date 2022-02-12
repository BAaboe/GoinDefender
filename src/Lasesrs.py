import pygame
import Window
import Game


class Lasers:
    def __init__(self, game):
        self.game = game
        self.wd = game.wd
        self.lasers = []

    def update(self):
        for i in self.lasers:
            if i.y+i.height < 0:
                self.removeLaser(i)
            elif i.y > self.game.wd.height:
                self.removeLaser(i)
            else:
                i.update()

    def addLaser(self, x, y, yDir=1, color="Red"):
        self.lasers.append(Laser(self.game, x, y, yDir, color))

    def removeLaser(self, laser):
        self.lasers.remove(laser)


class Laser:
    def __init__(self, game, x, y, yDir, color):
        self.game = game
        self.wd = self.game.wd

        self.x = x
        self.y = y
        self.width = 9
        self.height = 12

        self.yDir = yDir

        self.ySpeed = 10

        self.img = pygame.image.load(f"../assets/{color}Laser.png")
        if yDir == -1:
            self.img = pygame.transform.flip(self.img, False, True)

    def draw(self):
        self.wd.window.blit(self.img, (self.x, self.y))

    def update(self):
        self.y -= self.ySpeed*self.yDir
        self.draw()
