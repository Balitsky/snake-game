import pygame
from lib.Scene import Scene
from lib.Widget import Widget

class MainScene(Scene):

    def setup(self):
        widget = Widget()
        widget.setBackground("#D98F8F")
        widget.setLayout(0.25, 0.25, 0.5, 0.5)
        
        widget1 = Widget()
        widget1.setBackground("#4026AE")
        widget1.setLayout(0.8, 0.8, 0.2, 0.2)
        
        widget2 = Widget()
        widget2.setBackground("#AA0303")
        widget2.setLayout(0.2, 0.2, 0.2, 0.2)
        
        widget3 = Widget()
        widget3.setBackground("#AA0303")
        widget3.setLayout(0.6, 0.2, 0.2, 0.2)
        
        widget4 = Widget()
        widget4.setBackground("#37B16B")
        widget4.setLayout(0.3, 0.6, 0.4, 0.2)
        
        widget.addChild(widget1)
        widget.addChild(widget2)
        widget.addChild(widget3)
        widget.addChild(widget4)

        widget2.addChild(widget.clone())        

        m1= widget2.clone()
        m1.box.offsetX = m1.box.offsetY = 0

        m2= widget2.clone()
        m2.box.offsetX = m2.box.offsetY = 1

        widget.addChild(m2)
        m1.setBackground("#23C946")
        
        self.addToScene(widget)
        self.addToScene(m1)

        m1.animator.move((0.5, 0.5))

