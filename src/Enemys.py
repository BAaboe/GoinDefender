import pygame
import Enemy
import Window
from src import Game


class Enemys:
    def __init__(self, game: Game.Game):
        self.enemys = []
        self.game = game

    def update(self):
        for i in self.enemys:
            i.draw()

    def addEnemy(self, x, y, level):
        self.enemys.append(Enemy.Enemy(self.game, x, y, level))
