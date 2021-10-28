import abc
import pygame
from directives.point import Point
from directives.segment import Segment
from errors.messages import Messages


class Curve(metaclass=abc.ABCMeta):
    pygame.init()
    screen = pygame.display.set_mode((300, 300))

    def __init__(self, segments: list, points: list, radius: float):
        self._useSegments = False
        self._usePoints = False
        self.a = None
        self.b = None
        self.c = None
        self.seg1 = None
        self.seg2 = None
        self.radius = radius
        try:
            if len(points) == 3:
                self.a: Point = points[0]
                self.b: Point = points[1]
                self.c: Point = points[2]
                self._usePoints = True
                return
            if len(segments) == 2:
                self.seg1: Segment = segments[0]
                self.seg2: Segment = segments[1]
                self._useSegments = True
                return
        except TypeError:
            print(Messages.C_MS01)

    def _verifyRules(self):
        if not self._useSegments and not self._usePoints:
            raise ValueError(Messages.SP_MS01)
        if self._useSegments and not self._usePoints and (self.seg1 is None or self.seg2 is None):
            raise ValueError(Messages.SP_MS02)
        if self._usePoints and not self._useSegments and (self.a is None or self.b is None or self.c is None):
            raise ValueError(Messages.SP_MS03)

    def buildShape(self):
        self._verifyRules()
        points = []
        xm = 0
        ym = 0
        a = 0
        b = 0
        if self._usePoints:
            xm = self.a.x
            ym = self.a.y
            a = self.c.x
            b = self.c.y
        elif self._useSegments:
            xm = self.seg1.a.x
            ym = self.seg1.a.y
            a = self.seg2.b.x
            b = self.seg2.b.y
        x = -a
        y = 0
        e2 = b
        dx = (1 + 2 * x) * e2 * e2
        dy = x * x
        err = dx + dy
        while x <= 0:
            points.append(Point(x=xm - x, y=ym + y))
            points.append(Point(x=xm + x, y=ym + y))
            # points.append(Point(x=xm + x, y=ym - y))
            # points.append(Point(x=xm - x, y=ym - y))
            e2 = 2 * err
            if e2 >= (x * 2 + 1) * (b * b):
                x += 1
                err += (x * 2 + 1) * (b * b)
            if e2 <= (y * 2 + 1) * (a * a):
                y += 1
                err += (y * 2 + 1) * (a * b)
        while y < b:
            y += 1
            points.append(Point(x=xm, y=ym + y))
            points.append(Point(x=xm, y=ym - y))
        return points

    def buildForm(self):
        self._verifyRules()
        points = []
        # based to besier curve algorithm
        x0 = y0 = x1 = y1 = x2 = y2 = 0
        xy = 0
        dx = dy = err = 0
        if self._usePoints:
            x0 = self.a.x
            y0 = self.a.y
            x1 = self.b.x
            y1 = self.b.y
            x2 = self.c.x
            y2 = self.c.y
        elif self._useSegments:
            x0 = self.seg1.a.x
            y0 = self.seg1.a.y
            x1 = self.seg1.b.x
            y1 = self.seg1.b.y
            x2 = self.seg2.b.x
            y2 = self.seg2.b.y
        # valores relativos para checagem da curvatura
        sx = x2 - x1
        sy = y2 - y1
        xx = x0 - x1
        yy = y0 - y1
        cur = xx * sy - yy * sx
        assert ((xx * sx) <= 0 and (yy * sy) <= 0)
        if (sx * (sx + sy) * sy) > ((xx * xx) + (yy * yy)):
            x2 = x0
            x0 = sx + x1
            y2 = y0
            y0 = sy + y1
            cur = -cur
        if cur != 0:
            xx += sx
            xx *= sx
            sx = 1 if x0 < x2 else -1
            yy += sy
            yy *= sy
            sy = 1 if y0 < y2 else -1
            xy = 2 * xx * yy
            xx *= xx
            yy *= yy
            if cur * sx * sy < 0:
                xx = -xx
                yy = -yy
                xy = -xy
                cur = -cur
            dx = 4.0 * sy * cur * (x1 - x0) + xx - xy
            dy = 4.0 * sx * cur * (y0 - y1) + yy - xy
            xx += xx
            yy += yy
            err = dx + dy + xy
            while dy <= dx:
                print(x0, y0)
                points.append(Point(x=x0, y=y0))
                if x0 == x2 and y0 == y2:
                    return points
                y1 = 2 * err < dx
                if 2 * err > dy:
                    x0 += sx
                    dx -= xy
                    err += dy
                    err += yy
                if y1:
                    y0 += sy
                    dy -= xy
                    err += dx
                    err += xx
            points.append(Point(x=x0, y=y0))
            points.append(Point(x=x2, y=y2))
        return points






