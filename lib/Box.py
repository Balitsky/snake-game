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

    # percentage from the base
    offsetX: float
    offsetY: float
    sizeX: float
    sizeY: float

    def __init__(self, offsetX: float, offsetY: float, sizeX: float, sizeY: float, base: "Box"):
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.sizeX = sizeX
        self.sizeY = sizeY
        super().__init__(self.calculateParam(base))

    def recalculate(self, base: "Box"):
        x = round(base.x + base.w * self.offsetX)
        y = round(base.y + base.h * self.offsetY)
        w = round(base.w * self.sizeX)
        h = round(base.h * self.sizeY)

        super().__init__(x, y, w, h)