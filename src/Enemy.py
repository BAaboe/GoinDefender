import pygame
import Window
import Character


class Enemy(Character):
    def __init__(self,x, y ,wd: Window.Window(), level=1):
        super().__init__(wd)
        self.x = x
        self.y = y
        
        self.width, self.height = 50

        self.level = level
        
        self.img = pygame.image.load(f"assets/goin{self.level}.png")