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
    posX: float
    posY: float
    sizeX: float
    sizeY: float

    def __init__(self, posX, posY, sizeX, sizeY, base: ()):
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        super().__init__(self.calculateParam(base[0], base[1]))

    def recalculate(self, parentBox):
        super().__init__(self.calculateParam(parentBox.w, parentBox.h))

    def calculateParam(self, w, h):
        x = round(w * self.posX)
        y = round(h * self.posY)
        w = round(w * self.sizeX)
        h = round(h * self.sizeY)
        return x, y, w, h


# debug"
"""
box1 = Box(0.1, 0.2, 0.5, 0.5, (100, 100))
print(box1)
box2 = Box(0, 0, 1, 1, (200, 200))
box1.recalculate(box2)
print(box1)
"""
