import pygame

from directives.curve import Curve
from directives.point import Point
from resources.pygamecanvas import PygameCanvas


def main():
    apoint = Point(x=100, y=100)
    bpoint = Point(x=150, y=150)
    cpoint = Point(x=50, y=50)
    pygame.init()

    canvas = pygame.display.set_mode((300, 300))
    c = Curve(points=[apoint, bpoint, cpoint], segments=[], canvas=canvas)
    c.show()


if __name__ == '__main__':
    main()
