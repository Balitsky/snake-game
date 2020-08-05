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
    background: ()

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

    def update(self):
        self.box.recalculate()
        self.image = Surface((self.box.w, self.box.h))
        self.image.fill(self.background)

        self.rect = self.box
        # print(self.rect)

    def copy(self) -> "Widget":
        widget = Widget()
        widget.box = self.box.copy()
        
        widget.background = self.background
        return widget



# widget debug
pygame.init()
display = pygame.display.set_mode((500, 500))

widget = Widget()
widget.background = (0, 255, 0)
widget.box.setBase(display.get_rect())
widget.setLayout(0.25, 0.25, 0.5, 0.5)

widget1 = Widget()
widget1.background = (255, 0, 0)
widget1.setLayout(0.8, 0.8, 0.2, 0.2)

widget2 = Widget()
widget2.background = (0, 0, 255)
widget2.setLayout(0.2, 0.2, 0.2, 0.2)

widget3 = Widget()
widget3.background = (0, 0, 255)
widget3.setLayout(0.6, 0.2, 0.2, 0.2)

widget4 = Widget()
widget4.background = (0, 255, 255)
widget4.setLayout(0.3, 0.6, 0.4, 0.2)


widget.addChild(widget1)
widget.addChild(widget2)
widget.addChild(widget3)
widget.addChild(widget4)
widget1.addChild(widget2.copy())

# widget.paint(display)

group = OrderedUpdates(widget, widget1, widget2, widget3, widget4)

group.update()
group.draw(display)
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


    group.update()
    pygame.display.update(group.draw(display))
pygame.quit()
quit()

