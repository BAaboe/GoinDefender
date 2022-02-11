import pygame
from pygame.locals import *
import Window, Enemy, Player

pygame.init()

class Game:
    def __init__(self):
        self.wd = Window.Window()

        self.FPS = 30
        self.FramesPerSecond = pygame.time.Clock()

        self.wd.window.fill(self.wd.BLACK)

        

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            self.wd.window.fill(self.wd.BLACK)



            pygame.display.update()
            self.FramesPerSecond.tick(self.FPS)


    def start(self):
        #Do some shit idk
        self.game_loop()
