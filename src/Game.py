import math

import pygame
from pygame.locals import *

import Enemys
import Lasesrs
import Player
import Window
import Overlay

pygame.init()
pygame.mixer.init()


class Game:
    def __init__(self):
        self.wd = Window.Window()

        self.wd.window.fill(self.wd.BLACK)
        self.enemys = Enemys.Enemys(self)
        self.enemys.addEnemy(50, 50, 1)
        self.player = Player.Player(self, self.wd.width/2, self.wd.height-100)

        self.lasers = Lasesrs.Lasers(self)

        self.overlay = Overlay.Overlay(self)

        self.joystickConnected = False

        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystickConnected = True
        except pygame.error as e:
            self.joystickConnected = False

    def game_loop(self):
        while True:
            self.wd.key_pressed = pygame.key.get_pressed()
            print(self.joystick.get_axis(0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            self.wd.window.fill(self.wd.BLACK)

            self.update()
            self.updateTime()

            pygame.display.update()
            self.wd.time.tick(self.wd.FPS)

    def update(self):
        if not self.player.dead:
            self.lasers.update()
            self.player.update()
            self.enemys.update()
        else:
            self.draw()
        self.overlay.update()

    def draw(self):
        self.player.draw()
        self.enemys.draw()

    def updateTime(self):
        self.wd.timeMs = pygame.time.get_ticks()
        self.wd.timeS = math.floor(self.wd.timeMs/100)

    def start(self):
        # TODO: Do some shit idk
        self.game_loop()
