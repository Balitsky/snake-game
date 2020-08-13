import pygame
from pygame.surface import Surface
from pygame.sprite import OrderedUpdates
from lib.Widget import Widget


class Scene(OrderedUpdates):
    display: Surface
    baseWidget: Widget

    """Basic abstract scene class"""

    def __init__(self, display: Surface):
        super().__init__()
        self.display = display
        self.baseWidget = Widget()
        self.baseWidget.setBackground("#000000")
        self.baseWidget.box.setBase(self.display.get_rect())
        self.add(self.baseWidget)
        self.setup()

    def addToScene(self, widget: Widget):
        self.baseWidget.addChild(widget)
        self._addToScene(widget)

    def _addToScene(self, widget: Widget):
        self.add(widget)
        for child in widget.childs:
            self._addToScene(child)

    def render(self):
        self.update()
        pygame.display.update(self.draw(self.display))

    def setup(self):
        pass
