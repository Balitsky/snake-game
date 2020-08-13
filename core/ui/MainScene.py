import pygame
from lib.Scene import Scene
from lib.Widget import Widget


class MainScene(Scene):

    def setup(self):
        widget = Widget()
        widget.setBackground("#D98F8F")
        widget.setLayout(0.1, 0.1, 0.8, 0.8)

        grunt = Widget()
        grunt.setBackground("#544646")
        grunt.setLayout(0, 0.7, 1, 0.3)

        prototip = Widget()
        prototip.setBackground("#ffffff")
        prototip.setLayout(0.2, 0.75, 0.2, .2)

        stvol = Widget()
        stvol.setBackground("#000000")
        stvol.setLayout(0.45, 0.7, 0.1, 0.3)

        osnova = Widget()
        osnova.setBackground("#1beb10")
        osnova.setLayout(0.3, 0.2, 0.4, 0.5)

        osnova1 = Widget()
        osnova1.setBackground("#0f6e0a")
        osnova1.setLayout(0.25, 0.3, 0.5, 0.9)

        tree3 = prototip.clone()
        tree3.box.offsetY = 0.8
        tree3.box.offsetX = 0.48

        widget.addChild(grunt)
        widget.addChild(prototip)
        prototip.addChild(stvol)
        prototip.addChild(osnova)
        osnova.addChild(osnova1)
        widget.addChild(tree3)
        widget.addChild(prototip.clone())

        self.addToScene(widget)
