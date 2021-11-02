from directives.point import Point


class LinerBezierCurve:
    def __init__(self, a: Point, b: Point, precision=0.0001):
        self.a = a
        self.b = b
        self.precision = 1 if (precision is None or precision <= 0) else precision

    def build(self):
        points = []
        variation = 0
        while True:
            px = (1 - variation) * self.a.x + variation * self.b.x
            py = (1 - variation) * self.a.y + variation * self.b.y
            points.append(Point(x=px, y=py))
            variation += self.precision
            if variation >= 1:
                break
        return points


class QuadraticBezierCurve:
    def __init__(self, a: Point, b: Point, c: Point, precision=0.0001):
        self.a = a
        self.b = b
        self.c = c
        self.precision = 1 if (precision is None or precision <= 0) else precision

    def build(self):
        points = []
        i = 0
        while True:
            xa = self._nextPoint(self.a.x, self.b.x, i)
            ya = self._nextPoint(self.a.y, self.b.y, i)
            xb = self._nextPoint(self.b.x, self.c.x, i)
            yb = self._nextPoint(self.b.y, self.c.y, i)
            x = self._nextPoint(xa, xb, i)
            y = self._nextPoint(ya, yb, i)
            points.append(Point(x=x, y=y))
            if i >= 1:
                break
            i += self.precision
        return points

    @staticmethod
    def _nextPoint(x, y, precision):
        diff = int(y - x)
        return x + (diff * precision)


class CubicBezierCurve:
    def __init__(self, a: Point, b: Point, c: Point, d: Point, precision=0.0001):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.precision = 1 if (precision is None or precision <= 0) else precision

    @staticmethod
    def _nextPoint(x, y, precision):
        diff = int(y - x)
        return x + (diff * precision)

    def build(self):
        points = []
        i = 0
        while True:
            x = pow(1 - i, 3) * self.a.x + 3 * i * pow(1 - i, 2) * self.b.x + 3 * i * i * (1 - i) * self.c.x + \
                pow(i, 3) * self.d.x
            y = pow(1 - i, 3) * self.a.y + 3 * i * pow(1 - i, 2) * self.b.y + 3 * i * i * (1 - i) * self.c.y + \
                pow(i, 3) * self.d.y
            points.append(Point(x=x, y=y))
            if i >= 1:
                break
            i += self.precision
        return points
