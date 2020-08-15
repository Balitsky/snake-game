import time


class Animation:
    global From
    global To
    global Widget
    Duration: int
    _EndTime: int
    current_time_millis = lambda: int(round(time.time() * 1000))

    def __init__(self, Widget):
        self.Widget = Widget

    def From(self, From) -> "Animation":
        self.From = From
        return self

    def To(self, To) -> "Animation":
        self.To = To
        return self

    def Duration(self, Duration: int) -> "Animation":
        self.Duration = Duration
        return self

    def start(self):
        self._EndTime = self.current_time_millis() + self.Duration

    def update(self):
        pass
