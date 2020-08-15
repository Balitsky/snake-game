from lib.animations.Animation import Animation
from lib.animations.AnimationMove import AnimationMove

class Animator:
    widget: object
    currentAnimation: Animation

    def __init__(self, widget):
        self.widget = widget
        self.currentAnimation = None

    def update(self):
        if self.currentAnimation:
            if not self.currentAnimation.update():
                self.currentAnimation = None

    def move(self, pos: ()):
        target = self.widget.clone()
        target.box.offsetX = pos[0]
        target.box.offsetY = pos[1]
        fw = self.widget.clone()
        self.currentAnimation = AnimationMove(self.widget).From(fw).To(target).Duration(5000)
        self.currentAnimation.start()



