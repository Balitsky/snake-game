import pygame
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import OrderedUpdates
from Box import Box


class Widget(Sprite):
    box: Box
    childs: []
    parent: "Widget"

    def __init__(self):
        Sprite.__init__(self)
        self.box = Box()
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

    def setBackground(self, color: () = None, image: str = None):
        if color:
            self.image = Surface((1, 1))
            self.image.fill(color)
        elif image:
            self.image = pygame.image.load(image).convert()

    def update(self):
        self.box.recalculate()
        self.rect = self.box
        self.image = pygame.transform.scale(self.image, (self.box.w, self.box.h))


# widget debug
pygame.init()
display = pygame.display.set_mode((500, 500))

widget = Widget()
widget.setBackground((0, 255, 0))
widget.box.setBase(display.get_rect())
widget.setLayout(0.25, 0.25, 0.5, 0.5)

widget1 = Widget()
widget1.setBackground(image = "kir.png")
widget1.setLayout(0.8, 0.8, 0.2, 0.2)

widget2 = Widget()
widget2.setBackground(image = "baz.jpg")
widget2.setLayout(0.2, 0.2, 0.2, 0.2)

widget3 = Widget()
widget3.setBackground(image = "baz.jpg")
widget3.setLayout(0.6, 0.2, 0.2, 0.2)

widget4 = Widget()
widget4.setBackground((0, 255, 255))
widget4.setLayout(0.3, 0.6, 0.4, 0.2)



widget.addChild(widget1)
widget.addChild(widget2)
widget.addChild(widget3)
widget.addChild(widget4)


group = OrderedUpdates(widget, widget1, widget2, widget3, widget4)

group.update()
pygame.display.update(group.draw(display))

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


    group.update()
    pygame.display.update(group.draw(display))
pygame.quit()
quit()

