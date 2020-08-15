import pygame
from lib.Scene import Scene
from lib.Widget import Widget


class MainScene(Scene):

    def setup(self):
        stvol = Widget()
        stvol.setBackground("#000000")
        stvol.setLayout(0.45, 0.7, 0.1, 0.3)

        osnova1 = Widget()
        osnova1.setBackground("#0f6e0a")
        osnova1.setLayout(0.25, 0.3, 0.5, 0.9)

        osnova = Widget()
        osnova.setBackground("#1beb10")
        osnova.setLayout(0.3, 0.2, 0.4, 0.5)
        osnova.addChild(osnova1)

        protoTree = Widget()
        protoTree.setBackground("#ffffff")
        protoTree.setLayout(0.2, 0.75, 0.2, 0.2)
        protoTree.image.set_alpha(0)
        protoTree.addChild(stvol)
        protoTree.addChild(osnova)

        sky = Widget()
        sky.setBackground("#1b5dcf")
        sky.setLayout(0, 0, 1, 1)

        grunt = Widget()
        grunt.setBackground("#544646")
        grunt.setLayout(0, 0.7, 1, 0.3)

        tree1 = protoTree.clone()
        tree1.box.offsetX = 0.2
        tree1.box.offsetY = 0.75

        tree2 = protoTree.clone()
        tree2.box.offsetX = 0.3
        tree2.box.offsetY = 0.75

        tree3 = protoTree.clone()
        tree3.box.offsetX = 0.7
        tree3.box.offsetY = 0.7

        tree4 = protoTree.clone()
        tree4.box.offsetX = 0.6
        tree4.box.offsetY = 0.6

        tree5 = tree1.clone()
        tree5.box.offsetX += 0.2
        tree5.box.offsetY += tree5.box.sizeY * 0.3
        tree5.box.offsetX += tree5.box.sizeX * 0.15
        tree5.box.sizeY *= 0.7
        tree5.box.sizeX *= 0.7

        sun = Widget()
        sun.setBackground("#e8da15")
        sun.setLayout(0, 0, 0.2, 0.2)

        self.addToScene(sky)
        self.addToScene(grunt)
        self.addToScene(tree1)
        self.addToScene(tree2)
        self.addToScene(tree3)
        self.addToScene(tree4)
        self.addToScene(tree5)
        self.addToScene(sun)

        sun.animator.move(tree5)
