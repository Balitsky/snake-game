from lib.animations.Animation import Animation

class AnimationMove(Animation):


    def update(self) -> bool:
        fps = 60
        leftTime = self._EndTime - Animation.current_time_millis()
        frames = (self.Duration * fps) / 1000
        print(leftTime)
        if leftTime > 0:
            deltX = (self.To.box.offsetX - self.From.box.offsetX) / frames
            deltY = (self.To.box.offsetY - self.From.box.offsetY) / frames
            print("delt")
            print(self.From.box.offsetX)
            self.Widget.box.offsetX += deltX
            self.Widget.box.offsetY += deltY
            return True
        else:
            self.Widget.box.offsetX = self.To.box.offsetX
            self.Widget.box.offsetY = self.To.box.offsetY
            return False

