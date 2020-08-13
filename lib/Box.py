from pygame.rect import Rect

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

    base: Rect

    # percentage from the base
    offsetX: float
    offsetY: float
    sizeX: float
    sizeY: float

    def __init__(self):
        # default layout
        self.setLayout(0, 0, 1, 1)

    def setBase(self, base: Rect):
        self.base = base

    def setLayout(self, offsetX: float, offsetY: float, sizeX: float, sizeY: float):
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.sizeX = sizeX
        self.sizeY = sizeY

    def recalculate(self, base: Rect = None):
        if not base:
            base = self.base

        x = round(base.x + base.w * self.offsetX)
        y = round(base.y + base.h * self.offsetY)
        w = round(base.w * self.sizeX)
        h = round(base.h * self.sizeY)

        super().__init__(x, y, w, h)

    def clone(self) -> "Box":
        newBox = Box()
        newBox.setLayout(self.offsetX, self.offsetY, self.sizeX, self.sizeY)
        return newBox


