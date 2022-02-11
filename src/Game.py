import pygame
from pygame.locals import *
import math
import Window, Enemy, Player, Enemys, Lasesrs

pygame.init()


class Game:
    def __init__(self):
        self.wd = Window.Window()

        self.wd.window.fill(self.wd.BLACK)
        self.enemys = Enemys.Enemys(self)
        self.enemys.addEnemy(50, 50, 1)
        self.player = Player.Player(self, self.wd.width/2, self.wd.height-100)

        self.lasers = Lasesrs.Lasers(self)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            self.wd.key_pressed = pygame.key.get_pressed()
            self.wd.window.fill(self.wd.BLACK)

            self.update()
            self.updateTime()

            pygame.display.update()
            self.wd.FramesPerSecond.tick(self.wd.FPS)

    def update(self):
        self.player.update()
        self.enemys.update()

    def updateTime(self):
        self.wd.timeMs = pygame.time.get_ticks()
        self.wd.timeS = math.floor(self.wd.timeMs/100)

    def start(self):
        # Do some shit idk
        self.game_loop()
