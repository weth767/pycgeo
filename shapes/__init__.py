import abc
from core import Point, LinearBezierCurve
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


class Circle(Shape):
    __points__ = []

    def __init__(self, radius: float, point: Point):
        super(Circle, self)
        self.radius = radius
        self.point = point

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


class StraightLine(Shape):
    __points__ = []

    def __init__(self, linear_bezier_curve=None, a=None, b=None):
        super(StraightLine, self)
        self.a = a
        self.b = b
        self.lbc = linear_bezier_curve

        if self.a is not None and isinstance(self.a, Point) and self.b is not None and isinstance(self.b, Point):
            self.lbc = LinearBezierCurve(a=self.a, b=self.b)
            self.__points__ = self.lbc.build()
        if self.lbc is not None and isinstance(self.lbc, LinearBezierCurve):
            self.__points__ = self.lbc.build()
        raise Exception("To draw is necessary to inform x and y or linear bezier curve params!")

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Triangle(Shape):
    __points__ = []

    def __init__(self, lines=None):
        super(Triangle, self)
        lines: list[StraightLine] = lines
        if lines is None:
            raise Exception("Field cannot be None")
        # validar as outras regras do triangulo(conectividade dos pontos iniciais e finais de cada linha)
        if len(lines) != 3:
            raise Exception("A triangle need three lines(StraightLine) to be drawn")
        self.__points__ = lines[0].points + lines[1].points + lines[2].points

    @property
    def points(self) -> list[Point]:
        return self.__points__


class Rectangle(Shape):
    __points__ = []

    def __init__(self, lines=None):
        super(Rectangle, self)
        lines: list[StraightLine] = lines
        if lines is None:
            raise Exception("Field cannot be None")
        # validar as regras do retangulo
        if len(lines) != 4:
            raise Exception("A triangle need three lines(StraightLine) to be drawn")
        self.__points__ = lines[0].points + lines[1].points + lines[2].points + lines[3].points

    @property
    def points(self) -> list[Point]:
        return self.__points__

