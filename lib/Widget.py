import pygame
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.color import Color
from lib.Box import Box
from lib.animations.Animator import Animator


class Widget(Sprite):
    box: Box
    childs: []
    parent: "Widget"
    animator: Animator

    def __init__(self):
        Sprite.__init__(self)
        self.box = Box()
        self.rect = self.box
        self.image = Surface((1, 1))
        self.childs = []
        self.animator = Animator(self)

    def addChild(self, child):
        self.childs.append(child)
        child.box.setBase(self.box)

    def setLayout(self, *args, **kwargs):
        self.box.setLayout(*args, **kwargs)

    def setBackground(self, color: str = None, image: str = None, optimize=False):
        if image:
            self.image = pygame.image.load(image)
            if optimize:
                self.image = self.image.convert()
        elif color:
            self.image = Surface((1, 1))
            self.image.fill(Color(color))

    def update(self):
        self.animator.update()
        self.box.recalculate()
        self.image = pygame.transform.scale(self.image, (self.box.w, self.box.h))

    def clone(self) -> "Widget":
        cloned = Widget()
        cloned.image = self.image
        cloned.box = self.box.clone()
        cloned.rect = cloned.box

        for child in self.childs:
            cloned.addChild(child.clone())

        return cloned

