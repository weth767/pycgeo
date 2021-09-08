import abc
import sys
import pygame
from directives.point import Point


class PointCircle:
    def __init__(self, xc, yc, x, y):
        self.xc = xc
        self.yc = yc
        self.x = x
        self.y = y


class Curve(metaclass=abc.ABCMeta):
    def __init__(self, apoint: Point, bpoint: Point, cpoint: Point):
        self.apoint = apoint
        self.bpoint = bpoint
        self.cpoint = cpoint

    @staticmethod
    def draw_circle_simetricpoints(screen: pygame.display, points: list):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((255, 255, 255))
            for point in points:
                pygame.draw.circle(screen, (0, 0, 0), (point.xc + point.x, point.yc + point.y), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc - point.x, point.yc + point.y), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc + point.x, point.yc - point.y), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc - point.x, point.yc - point.y), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc + point.y, point.yc + point.x), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc - point.y, point.yc + point.x), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc + point.y, point.yc - point.x), 1, 10)
                pygame.draw.circle(screen, (0, 0, 0), (point.xc - point.y, point.yc - point.x), 1, 10)
            pygame.display.update()

    def draw_circle_midpoint(self, xc, yc, radius):
        p = 1 - radius
        y = radius
        pygame.init()
        screen = pygame.display.set_mode((300, 300))
        points = []
        for x in range(y + 1):
            points.append(PointCircle(xc, yc, x, y))
            if p < 0:
                p += 2 * x + 1
            else:
                y = y - 1
                p += 2 * (x - y) + 1
        self.draw_circle_simetricpoints(screen, points)
