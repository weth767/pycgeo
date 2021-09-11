import sys

import pygame

from errors.messages import Messages
from resources.canvas import Canvas


class PygameCanvas(Canvas):
    screen = None
    width = 500
    height = 500

    def __init__(self, **kwargs):
        pygame.init()
        self.w = kwargs.get('width') if kwargs.get('width') is not None else 500
        self.h = kwargs.get('height') if kwargs.get('height') is not None else 500
        if self.w is None or self.h is None:
            print(Messages.CV_MS01)
        self.screen = pygame.display.set_mode(self.w, self.h)

    def draw(self, **kwargs):
        self.screen = kwargs.get('screen') if kwargs.get('screen') is not None else self.screen
        points = kwargs.get('points') if kwargs.get('points') is not None else []
        color = kwargs.get('color') if kwargs.get('color') is not None else (0, 0, 0)
        background_color = kwargs.get('background_color') if kwargs.get('background_color') is not None else (255, 255, 255)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(background_color)
            for point in points:
                pygame.draw.circle(self.screen, color, (point.x, point.y))
            pygame.display.update()

