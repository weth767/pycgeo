from pygame import Surface
from pygame import init
from resources.canvas import Canvas


class PygameCanvas(Canvas, Surface):
    screen: Surface = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        init()
        self.screen = Surface.__init__(self, size=[kwargs.get('width'), kwargs.get('height')])
