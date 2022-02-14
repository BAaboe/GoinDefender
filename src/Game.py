import math

import pygame
from pygame.locals import *

import Enemies
import Lasers
import Player
import Window
import Overlay
import json

pygame.init()
pygame.mixer.init()


class Game:
    def __init__(self):
        self.wd = Window.Window()

        self.wd.window.fill(self.wd.BLACK)
        self.enemies = Enemies.Enemies(self)

        self.player = Player.Player(self, self.wd.width/2, self.wd.height-100)

        self.lasers = Lasers.Lasers(self)

        self.overlay = Overlay.Overlay(self)

        self.joystickConnected = False

        self.started = False

        self.themeSong = pygame.mixer.Sound("../assets/GoinInvaderTheme.wav")

        self.levelData = None
        with open("../assets/level.json", "r") as f:
            self.levelData = json.load(f)

        self.level = 1

        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystickConnected = True
        except pygame.error as e:
            self.joystickConnected = False

    def game_loop(self):
        while True:
            self.wd.key_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            if self.wd.key_pressed[K_ESCAPE]:
                pygame.quit()
                quit()
            if self.joystickConnected:
                if self.joystick.get_button(1):
                    pygame.quit()
                    quit()

            if self.player.dead:
                if self.wd.key_pressed[K_SPACE]:
                    break
                if self.joystickConnected:
                    if self.joystick.get_button(0):
                        break

            self.wd.window.fill(self.wd.BLACK)

            self.update()
            self.updateTime()

            pygame.display.update()
            self.wd.time.tick(self.wd.FPS)

    def update(self):
        if self.player.score >= 30:
            self.level = 2
        elif self.player.score >= 90:
            self.level = 3

        if not self.player.dead:
            self.lasers.update()
            self.player.update()
            self.enemies.update()
        else:
            self.draw()
        self.overlay.update()

    def draw(self):
        self.player.draw()
        self.enemies.draw()

    def updateTime(self):
        self.wd.timeMs = pygame.time.get_ticks()
        self.wd.timeS = math.floor(self.wd.timeMs/100)

    def start(self):
        self.startScreen()
        self.game_loop()

    def startScreen(self):
        # TODO: Finish this
        self.overlay.addText("Goin Invader", self.wd.width / 2, self.wd.height / 2 - 50, 100, self.wd.WHITE, "title")
        self.overlay.addText("Press space or X to start", self.wd.width / 2, self.wd.height / 2 + 50, 50, self.wd.WHITE,
                             "instruction")
        pygame.mixer.Sound.play(self.themeSong)
        while not self.started:
            self.wd.key_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            if self.wd.key_pressed[K_ESCAPE]:
                pygame.quit()
                quit()
            if self.joystickConnected:
                if self.joystick.get_button(1):
                    pygame.quit()
                    quit()

            if self.wd.key_pressed[K_SPACE]:
                self.started = True
                self.overlay.removeText("title")
                self.overlay.removeText("instruction")
                pygame.mixer.Sound.stop(self.themeSong)
            if self.joystickConnected:
                if self.joystick.get_button(0):
                    self.started = True
                    self.overlay.removeText("title")
                    self.overlay.removeText("instruction")
                    pygame.mixer.Sound.stop(self.themeSong)

            self.wd.window.fill(self.wd.BLACK)
            self.player.draw()
            self.overlay.draw()

            pygame.display.update()
            self.wd.time.tick(self.wd.FPS)
