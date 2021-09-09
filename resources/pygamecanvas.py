import pygame

from resources.canvas import Canvas


class PygameCanvas(Canvas, pygame.display):
    screen = None

    def __init__(self, **kwargs):
        self.screen = pygame.init()
