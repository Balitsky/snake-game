import pygame
from pygame.surface import Surface
from Box import Box


class Widget:
    box: Box
    childs: []
    background: Surface

    def __init__(self):
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)

    def paint(self, display):
        pygame.draw.rect(display, self.background, self.box)
        for child in self.childs:
            child.paint(display)


    def setLayout(self, *args):
        self.box = Box(*args)


pygame.init()
display = pygame.display.set_mode((500, 500))

widget = Widget()
widget.setLayout(0.25, 0.25, 0.5, 0.5, (500, 500))

widget1 = Widget()
widget1.setLayout(0.8, 0.8, 0.2, 0.2, (widget.box.w, widget.box.h))

widget2 = Widget()
widget2.setLayout(0, 0, 0.2, 0.2, (widget.box.w, widget.box.h))

widget.addChild(widget1)
widget.addChild(widget2)

widget.paint(display)

pygame.display.update()
pygame.time.wait(2000)
