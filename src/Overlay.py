import pygame
import Game


class Overlay:
    def __init__(self, game):
        self.game = game
        self.elements = []

    def draw(self):
        for i in self.elements:
            if i.img:
                i.draw()
            elif i.text:
                self.game.wd.display_text(i.size, i.text, i.color, i.x, i.y)

    def addElement(self, x, y, name="undefined", width=None, height=None, img=None, text=None, color=(255, 255, 255), size=None):
        self.elements.append(OverlayElement(self.game, x, y, name, width, height, img, text, color, size))

    def removeElement(self, element):
        self.elements.remove()

    def addHeart(self):
        img = pygame.image.load("../assets/heart.png")
        x = 0
        y = 0
        width = 20
        height = 20
        lastHeart = None
        for element in self.elements:
            if element.name == "heart":
                lastHeart = self.elements.index(element)
        if lastHeart:
            x = self.elements[lastHeart].x - width - 10
            y = self.elements[lastHeart].y - height - 10
        else:
            x = self.game.wd.width - 10
            y = self.game.wd.height - 10

        self.addElement(x, y, "heart", width, height, img)


class OverlayElement:
    def __init__(self, game, x, y, name, width, height, img, text, color, size):
        self.game = game

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.name = name

        self.color = color
        self.size = size

        self.text = text
        self.img = img
        if self.img:
            self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def draw(self):
        self.game.wd.window.blit(self.img, (self.x, self.y))
