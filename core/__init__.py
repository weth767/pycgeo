import math


class Point:
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.z = kwargs.get('z')

    def __str__(self):
        return f"x: {self.x}, y: {self.y}" if self.z is None else f"x: {self.x}, y: {self.y}, z: {self.z}"

    def distance(self, point: "Point"):
        if self.z is None and point.z is None:
            return math.sqrt((math.pow((self.x - point.x), 2) + math.pow((self.y - point.y), 2)))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return math.sqrt((math.pow((self.x - point.x), 2) + math.pow((self.y - point.y), 2)
                          + math.pow((self.z - point.z), 2)))

    def median_point(self, point: "Point"):
        if self.z is None and point.z is None:
            return Point(x=(self.x + point.x), y=(self.y + point.y))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return Point(x=(self.x + point.x), y=(self.y + point.y), z=(self.z + point.z))

    def __sub__(self, point: "Point"):
        if not isinstance(point, Point):
            raise ArithmeticError("Isn't possible to sub 'Point' with another type of data")
        if self.z is None and point.z is None:
            return Point(x=(self.x - point.x), y=(self.y - point.y))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return Point(x=(self.x - point.x), y=(self.y - point.y), z=(self.z - point.z))

    def __add__(self, point: "Point"):
        if not isinstance(point, Point):
            raise ArithmeticError("Isn't possible to add 'Point' with another type of data")
        if self.z is None and point.z is None:
            return Point(x=(self.x + point.x), y=(self.y + point.y))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return Point(x=(self.x + point.x), y=(self.y + point.y), z=(self.z + point.z))

    def __eq__(self, point: "Point"):
        if not isinstance(point, Point):
            raise AssertionError("Isn't possible to compare 'Point' with another type of data")
        if self.z is None and point.z is None:
            return self.x == point.x and self.y == point.y
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return self.x == point.x and self.y == point.y and self.z == point.z

    def __mul__(self, value):
        if value is None:
            raise ArithmeticError("Isn't possible to multiply a 'Point' with None value")
        if type(value) != float and type(value) != int:
            raise ArithmeticError("Isn't possible to multiply 'Point' with type different than int or float")
        if self.z is None:
            return Point(x=(self.x * value), y=(self.y * value))
        return Point(x=(self.x * value), y=(self.y * value), z=(self.z * value))


class LinearBezierCurve:
    def __init__(self, a: Point, b: Point, precision=0.001):
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
            xa = self._next_point(self.a.x, self.b.x, i)
            ya = self._next_point(self.a.y, self.b.y, i)
            xb = self._next_point(self.b.x, self.c.x, i)
            yb = self._next_point(self.b.y, self.c.y, i)
            x = self._next_point(xa, xb, i)
            y = self._next_point(ya, yb, i)
            points.append(Point(x=x, y=y))
            if i >= 1:
                break
            i += self.precision
        return points

    @staticmethod
    def _next_point(x, y, precision):
        diff = int(y - x)
        return x + (diff * precision)


class CubicBezierCurve:
    def __init__(self, a: Point, b: Point, c: Point, d: Point, precision=0.0001):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.precision = 1 if (precision is None or precision <= 0) else precision

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
