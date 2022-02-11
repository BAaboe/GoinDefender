import pygame
import Window
import Laser
from src import Game


class Lasers:
    def __init__(self, game: Game.Game):
        self.game = game
        self.wd = game.wd
        self.lasers = []

    def update(self):
        for i in self.lasers:
            if i.y+i.height < 0:
                self.removeLaser(i)
            else:
                i.update()

    def addLaser(self, x, y):
        self.lasers.append(Laser.Laser(self.wd, x, y))

    def removeLaser(self, laser: Laser.Laser):
        self.lasers.remove(laser)
