import abc
import sys
import pygame
from errors import Messages


class Canvas(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def draw(self, **kwargs):
        pass


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
        self.screen = pygame.display.set_mode((self.w, self.h))

    """
    Args:
        screen: (Surface, optional) New Pygame Surface if user need override screen
        points: (list) List of Point that will be drawn on screen
        color: (tuple, optional) Tuple represent intensity of RGB color of drawn points
        background_color: (tuple, optional) Tuple represent intensity of RGB color of screen background

    Returns:
        None
    """

    """
        draw(screen=None, points=[], color=(0, 0, 0), background_color=(255, 255, 255)) -> None
        Set list of points on screen
    """
    def draw(self, **kwargs) -> None:
        self.screen = kwargs.get('screen') if kwargs.get('screen') is not None else self.screen
        points = kwargs.get('points') if kwargs.get('points') is not None else []
        color = kwargs.get('color') if kwargs.get('color') is not None else (0, 0, 0)
        background_color = kwargs.get('background_color') if kwargs.get('background_color') is not None else \
            (255, 255, 255)
        pygame.display.set_caption('Canvas')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(background_color)
            for point in points:
                pygame.draw.circle(self.screen, color, (point.x, self.h - point.y), 1, 1)
            pygame.display.update()


class TkinterCanvas(Canvas):
    def __init__(self, **kwargs):
        pass

    def draw(self, **kwargs):
        pass