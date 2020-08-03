import pygame
from lib.Box import Box


class Widget:
    box: Box
    childs: [] = []
    background: ()

    def addChild(self, child):
        self.childs.append(child)

    def paint(self, display):
        print(self.childs)
        pygame.draw.rect(display, self.background, self.box)
        for child in self.childs:
            child.paint(display)


    def setLayout(self, *args):
        self.box = Box(*args)
        print(self.box)


widget = Widget()
widget.setLayout(0.25, 0.25, 0.5, 0.5, (500, 500))
widget1 = Widget()
widget1.setLayout(0.8, 0.8, 0.2, 0.2, (widget.box.w, widget.box.h))
widget1.background = (255, 0, 0)
widget.addChild(widget1)
pygame.init()
display = pygame.display.set_mode((500, 500))
widget.background = (0, 255, 0)
widget.paint(display)
pygame.display.update()
pygame.time.wait(5000)
