
from lib.animations.Animation import Animation
from lib.animations.AnimationMove import AnimationMove

class Animator:
    global widget
    currentAnimation: Animation

    def __init__(self, widget):
        self.widget = widget

    def update(self):
        if self.currentAnimation:
            self.currentAnimation.update()

    def move(self, target):
        self.currentAnimation = AnimationMove(self.widget).From(self.widget).To(target).Duration(5000)
        self.currentAnimation.start()







