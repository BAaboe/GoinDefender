import pygame
import Enemy

class Enemys:
    def __init__(self):
        self.enemys = []
    

    def update(self):
        for i in self.enemys:
            i.draw()

    def addEnemy(self, x, y, level):
        self.enemys.append(Enemy.Enemy())