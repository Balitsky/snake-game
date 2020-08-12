import pygame
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.color import Color
from lib.Box import Box


class Widget(Sprite):
    box: Box
    childs: []
    parent: "Widget"

    def __init__(self):
        Sprite.__init__(self)
        self.box = Box()
        self.rect = self.box
        self.image = Surface((1, 1))
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)
        child.box.setBase(self.box)

    def paint(self, display):
        self.box.recalculate()

        pygame.draw.rect(display, self.background, self.box)
        for child in self.childs:
            child.paint(display)

    def setLayout(self, *args, **kwargs):
        self.box.setLayout(*args, **kwargs)

    def setBackground(self, color: str = None, image: str = None, optimize = False):
        if image:
            self.image = pygame.image.load(image)
            if optimize:
                self.image = self.image.convert()
        elif color:
            self.image.fill(Color(color))
        
    def update(self):
        self.box.recalculate()
        self.image = pygame.transform.scale(self.image, (self.box.w, self.box.h))