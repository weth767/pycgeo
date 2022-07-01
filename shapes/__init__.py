import abc
from core import Point, LinearBezierCurve, QuadraticBezierCurve, CubicBezierCurve
from errors import Messages


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, **kwargs) -> None:
        """
        :param kwargs:
        """
        self.canvas = None

    @property
    def points(self) -> list[Point]:
        """
        Return a list of points that defines a shape
        :return list[Point]:
        """
        return []


# Bresenham's algorithm
class Circle(Shape):
    def __init__(self, radius: float, point: Point):
        super(Circle, self)
        self.radius = radius
        self.point = point
        self.__points__ = []

        if radius is None or point is None:
            raise Exception(Messages.C_MS02)

        x = radius
        error = 1 - x
        y = 0

        while y <= x:
            self.points.append(Point(x=x + point.x, y=y + point.y))
            self.points.append(Point(x=y + point.x, y=x + point.y))
            self.points.append(Point(x=-x + point.x, y=y + point.y))
            self.points.append(Point(x=-y + point.x, y=x + point.y))
            self.points.append(Point(x=-x + point.x, y=-y + point.y))
            self.points.append(Point(x=-y + point.x, y=-x + point.y))
            self.points.append(Point(x=x + point.x, y=-y + point.y))
            self.points.append(Point(x=y + point.x, y=-x + point.y))
            y = y + 1
            if error < 0:
                error += 2 * y + 1
            else:
                x = x - 1
                error += 2 * (y - x + 1)

    @property
    def points(self) -> list[Point]:
        return self.__points__


class LineSegment(Shape):
    __points__: list[Point] = []

    def __init__(self, linear_bezier_curve=None, a=None, b=None):
        super(LineSegment, self)
        self.a = a
        self.b = b
        self.lbc = linear_bezier_curve

        if self.a is not None and isinstance(self.a, Point) and self.b is not None and isinstance(self.b, Point):
            self.lbc = LinearBezierCurve(a=self.a, b=self.b)
            self.__points__ = self.lbc.build()
            return
        if self.lbc is not None and isinstance(self.lbc, LinearBezierCurve):
            self.__points__ = self.lbc.build()
            return
        raise Exception("To draw is necessary to inform x and y or linear bezier curve params!")

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def size(self) -> float:
        f_point = self.__points__[0]
        l_point = self.__points__[-1]
        if self.a is None or self.b is None:
            return f_point.distance(l_point)
        return self.a.distance(self.b)


class Triangle(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]):
        super(Triangle, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        # validar as outras regras do triangulo(conectividade dos pontos iniciais e finais de cada linha)
        if len(self.lines) != 3:
            raise Exception("A triangle need three lines(StraightLine) to be drawn")
        self.__points__ = self.lines[0].points + self.lines[1].points + self.lines[2].points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Rectangle(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]):
        super(Rectangle, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        # validar as regras do retangulo
        if len(self.lines) != 4:
            raise Exception("A rectangle need four lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Square(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Square, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        # validar as regras do retangulo
        if len(self.lines) != 4:
            raise Exception("A square need four lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Rhombus(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Rhombus, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        # validar as regras do retangulo
        if len(self.lines) != 4:
            raise Exception("A square need four lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Pentagon(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Pentagon, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        if len(self.lines) != 5:
            raise Exception("A pentagon need five lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Hexagon(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Hexagon, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        if len(self.lines) != 6:
            raise Exception("A hexagon need six lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Heptagon(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Heptagon, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        if len(self.lines) != 7:
            raise Exception("A heptagon need seven lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Octagon(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Octagon, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        if len(self.lines) != 8:
            raise Exception("A octagon need eight lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Nonagon(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Nonagon, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        if len(self.lines) != 9:
            raise Exception("A nonagon need nine lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Decagon(Shape):
    __points__: list[Point] = []

    def __init__(self, lines: list[LineSegment]) -> None:
        super(Decagon, self)
        self.lines = lines
        if self.lines is None:
            raise Exception("The lines field cannot be None")
        if len(self.lines) != 10:
            raise Exception("A decagon need ten lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class SemiCurve(Shape):
    __points__: list[Point] = []
    __qbc__: QuadraticBezierCurve

    def __init__(self, points: list[Point]) -> None:
        if points is None:
            raise Exception("The points field cannot be None")
        if len(points) != 3:
            raise Exception("The field points must have length equals to three")
        self.__qbc__ = QuadraticBezierCurve(a=points[0], b=points[1], c=points[2])
        self.__points__ = self.__qbc__.build()

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def qbc(self) -> QuadraticBezierCurve:
        return self.__qbc__


class Curve(Shape):
    __points__: list[Point] = []
    __cbc__: CubicBezierCurve

    def __init__(self, points: list[Point]) -> None:
        if points is None:
            raise Exception("The points field cannot be None")
        if len(points) != 4:
            raise Exception("The field points must have length equals to four")
        self.__cbc__ = CubicBezierCurve(a=points[0], b=points[1], c=points[2], d=points[3])
        self.__points__ = self.__cbc__.build()

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def cbc(self) -> CubicBezierCurve:
        return self.__cbc__
