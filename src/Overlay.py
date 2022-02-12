import pygame
import Game


class Overlay:
    """
    The Overlay class keeps track of all the overlay elements
    """
    def __init__(self, game):
        self.game = game
        self.hearts = Hearts(self.game)
        self.textObjs = TextObjects(self.game)

    def update(self):
        self.hearts.update()
        self.textObjs.update()

    def draw(self):
        self.hearts.draw()
        self.textObjs.draw()

    def addText(self, text, x, y, size, color=(255, 255, 255), name="undefined"):
        self.textObjs.addText(text, x, y, size, color, name)

    def removeText(self, name):
        for i in self.textObjs.textObjects:
            if i.name == name:
                self.textObjs.removeText(i)


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

        self.type = ""
        if self.img:
            self.type = "img"
            self.img = pygame.transform.scale(self.img, (self.width, self.height))
        elif self.text:
            self.type = "text"

    def draw(self):
        if self.type == "img":
            self.game.wd.window.blit(self.img, (self.x, self.y))
        elif self.type == "text":
            self.game.wd.display_text(self.size, self.text, self.color, self.x, self.y)


class Hearts:
    def __init__(self, game):
        self.game = game
        self.hearts = []

    def draw(self):
        for heart in self.hearts:
            heart.draw()

    def addHeart(self):
        img = pygame.image.load("../assets/heart.png")
        x = 0
        y = 0
        width = 20
        height = 20
        if self.hearts:
            x = self.hearts[-1].x - width - 10
            y = self.game.wd.height - height - 10
        else:
            x = self.game.wd.width - width - 10
            y = self.game.wd.height - height - 10

        self.hearts.append(OverlayElement(self.game, x, y, "heart", width, height, img, None, None, None))

    def removeHeart(self):
        self.hearts.pop(-1)

    def checkHP(self):
        hp = self.game.player.hp
        if not len(self.hearts) == hp:
            self.hearts.clear()
            for i in range(hp):
                self.addHeart()

    def update(self):
        self.checkHP()
        self.draw()

    def draw(self):
        for heart in self.hearts:
            heart.draw()


class TextObjects:
    def __init__(self, game):
        self.game = game
        self.textObjects = []

    def addText(self, text, x, y, size, color=(255, 255, 255), name="undefined"):
        self.textObjects.append(OverlayElement(self.game, x, y, name, None, None, None, text, color, size))

    def removeText(self, textObj):
        self.textObjects.remove(textObj)

    def updateScore(self):
        if not self.game.player.dead:
            x = self.game.wd.width - 50
            y = self.game.wd.height - 70
            size = 30
        else:
            x = self.game.wd.width / 2
            y = self.game.wd.height / 2 + 50
            size = 50
        color = self.game.wd.WHITE
        name = "score"

        score = self.game.player.score

        for text in self.textObjects:
            if text.name == "score":
                self.removeText(text)

        self.addText(str(score), x, y, size, color, name)

    def update(self):
        self.updateScore()
        self.draw()

    def draw(self):
        for text in self.textObjects:
            text.draw()

