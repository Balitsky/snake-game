from pygame.rect import Rect
from pygame.surface import Surface

"""
x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h
"""


class Box(Rect):

    # percentage from the base
    offsetX: float
    offsetY: float
    sizeX: float
    sizeY: float

    def __init__(self, offsetX: float, offsetY: float, sizeX: float, sizeY: float, base: Surface):
        self.initVariables(offsetX, offsetY, sizeX, sizeY)
        self.__recalculate(0, 0, base.get_size()[0], base.get_size()[1])

    def __init__(self, offsetX: float, offsetY: float, sizeX: float, sizeY: float, base: "Box"):
        self.initVariables(offsetX, offsetY, sizeX, sizeY)
        self.recalculate(base)

    def initVariables(self, offsetX: float, offsetY: float, sizeX: float, sizeY: float):
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.sizeX = sizeX
        self.sizeY = sizeY

    def recalculate(self, base: "Box"):
        self.__recalculate(base.x, base.y, base.w, base.h)

    def __recalculate(self, x, y, w, h):
        x = round(x + w * self.offsetX)
        y = round(y + h * self.offsetY)
        w = round(w * self.sizeX)
        h = round(h * self.sizeY)

        super().__init__(x, y, w, h)