import pygame

import Character
import Game


class Enemy(Character.Character):
    def __init__(self, game: Game.Game, x, y, level=1):

        self.level = level

        super().__init__(game, pygame.image.load(f"../assets/goin{self.level}.png"), x, y, 50, 50)


