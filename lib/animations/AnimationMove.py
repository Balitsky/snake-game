from lib.animations.Animation import Animation

class AnimationMove(Animation):
    def update(self):
        leftTime = self.current_time_millis() - self._EndTime
        if leftTime > 0:
            deltX = (self.To.box.offsetX - self.From.box.offsetX) / leftTime
            deltY = (self.To.box.offsetY - self.From.box.offsetY) / leftTime
            self.Widget.box.offsetX += deltX
            self.Widget.box.offsetY += deltY
            self.From = self.Widget

        else:
            del self