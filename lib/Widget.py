import pygame
from pygame.surface import Surface
from Box import Box


class Widget:
    box: Box
    childs: []
    background: ()

    def __init__(self):
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)

    def paint(self, display):
        pygame.draw.rect(display, self.background, self.box)
        for child in self.childs:
            child.paint(display)


    def setLayout(self, *args, **kwargs):
        self.box = Box(*args, **kwargs)


pygame.init()
display = pygame.display.set_mode((500, 500))

widget = Widget()
widget.background = (0, 255, 0)
widget.setLayout(0.25, 0.25, 0.5, 0.5, base = None, display = display)

widget1 = Widget()
widget1.background = (255, 0, 0)
widget1.setLayout(0.8, 0.8, 0.2, 0.2, widget.box)

widget2 = Widget()
widget2.background = (0, 0, 255)
widget2.setLayout(0, 0, 0.2, 0.2, widget1.box)

widget.addChild(widget1)
widget.addChild(widget2)

widget.paint(display)

pygame.display.update()
pygame.time.wait(2000)
