import pygame
from pygame.surface import Surface
from Box import Box


class Widget:
    box: Box
    childs: []
    parent: "Widget"
    background: ()

    def __init__(self):
        self.childs = []
        self.parent = None

    def addChild(self, child):
        self.childs.append(child)
        child.parent = self

    def paint(self, display):
        if self.parent:
            self.box.recalculate(self.parent.box)
        pygame.draw.rect(display, self.background, self.box)
        for child in self.childs:
            child.paint(display)


    def setLayout(self, *args, **kwargs):
        self.box = Box(*args, **kwargs)




# widget debug
pygame.init()
display = pygame.display.set_mode((500, 500))

widget = Widget()
widget.background = (0, 255, 0)
widget.setLayout(0.25, 0.25, 0.5, 0.5, display.get_rect())

widget1 = Widget()
widget1.background = (255, 0, 0)
widget1.setLayout(0.8, 0.8, 0.2, 0.2, widget.box)

widget2 = Widget()
widget2.background = (0, 0, 255)
widget2.setLayout(0, 0, 0.2, 0.2, widget1.box)

widget.addChild(widget1)
widget1.addChild(widget2)

widget.paint(display)

pygame.display.update()
pygame.time.wait(2000)

clock = pygame.time.Clock()

def gameEnd():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return True

while not gameEnd():
    clock.tick(60)
    widget1.box.offsetX += -0.005
    widget1.box.recalculate(widget.box)
    widget.paint(display) 
    pygame.display.update()
pygame.quit()
quit()

