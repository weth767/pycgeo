import abc
import math

from numpy import longdouble
from core import Point, LinearBezierCurve, QuadraticBezierCurve, CubicBezierCurve
from errors import ErrorCodes, GeometryException
from geometry import Geometry
from utils import ShapeTypes, ShapeUtils, TriangleTypes


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

    def __init__(self, radius: longdouble, point: Point):
        super(Circle, self)
        self.radius = radius
        self.point = point
        self.__points__: list[Point] = []
        if radius is None or point is None:
            raise GeometryException(
                error_code=ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED)
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

    @property
    def area(self) -> longdouble:
        return math.pi * math.pow(self.radius, 2)

    @property
    def perimeter(self) -> longdouble:
        return 2 * math.pi * self.radius

    @property
    def diameter(self) -> longdouble:
        return 2 * self.radius


class LineSegment(Shape):
    def __init__(self, **kwargs):
        super(LineSegment, self)
        self.name = "LineSegment" + \
            (" " + kwargs.get('name') if kwargs.get('name') else "")
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')
        self.lbc = kwargs.get('lbc')
        self.__points__: list[Point] = []

        if self.a is not None and isinstance(self.a, Point) and self.b is not None and isinstance(self.b, Point):
            self.lbc = LinearBezierCurve(a=self.a, b=self.b)
            self.__points__ = self.lbc.build()
            return
        if self.lbc is not None and isinstance(self.lbc, LinearBezierCurve):
            self.__points__ = self.lbc.build()
            return
        raise GeometryException(
            "To draw is necessary to inform x and y or linear bezier curve params!", ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED)

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def size(self) -> float:
        f_point = self.__points__[0]
        l_point = self.__points__[-1]
        return f_point.distance(l_point)

    def __str__(self) -> str:
        a = self.__points__[0]
        b = self.__points__[-1]
        return self.name + " (a = " + str(a) + ", b = " + str(b) + ")"


class Triangle(Shape):
    def __init__(self, lines: list[LineSegment]):
        super(Triangle, self)
        self.lines = lines
        __points__: list[Point] = []
        if self.lines is None:
            raise GeometryException(
                "The lines field cannot be None", ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED)
        if len(self.lines) != 3:
            raise GeometryException(
                "A triangle need three lines to be drawn", ErrorCodes.ERROR_INVALID_PARAMETER_SIZE)
        if not (Geometry.consecutive_straight_lines(lines[0].points, lines[1].points) and
                Geometry.consecutive_straight_lines(lines[1].points, lines[2].points) and
                Geometry.consecutive_straight_lines(lines[0].points, lines[2].points)):
            raise GeometryException(
                "Each line of a triangle must be connected", ErrorCodes.ERROR_INVALID_PARAMETER_FORMAT)
        self.__points__ = [line.points for line in self.lines]

    @ property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def type(self) -> str:
        if (self.lines[0].size == self.lines[1].size and self.lines[1].size == self.lines[2].size):
            return ShapeUtils.get_shape_type(ShapeTypes.TRIANGLE, TriangleTypes.EQUILATERAL.value)
        if (self.lines[0].size == self.lines[1].size or self.lines[1].size == self.lines[2].size or self.lines[0].size == self.lines[2].size):
            return ShapeUtils.get_shape_type(ShapeTypes.TRIANGLE, TriangleTypes.ISOSCELES.value)
        return ShapeUtils.get_shape_type(ShapeTypes.TRIANGLE, TriangleTypes.SCALENE.value)

    def area(self) -> longdouble:
        # Heron's area formula
        a = 0
        b = 0
        c = 0
        if (self.lines[0].size > self.lines[1].size and self.lines[0].size > self.lines[2].size):
            c = self.lines[0].size
            a = self.lines[1].size
            b = self.lines[2].size
        elif (self.lines[1].size > self.lines[0].size and self.lines[1].size > self.lines[2].size):
            c = self.lines[1].size
            a = self.lines[0].size
            b = self.lines[2].size
        else:
            c = self.lines[2].size
            a = self.lines[0].size
            b = self.lines[1].size
        s = self.perimeter / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @property
    def perimeter(self) -> longdouble:
        return sum([line.size for line in self.lines])

    @property
    def height(self) -> longdouble:
        if self.type == TriangleTypes.EQUILATERAL.value:
            return
        return self.lines[0].size

    def __str__(self) -> str:
        return "Triangle: {}".format([str(line) for line in self.lines])


class Rectangle(Shape):
    def __init__(self, lines: list[LineSegment]):
        super(Rectangle, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException(
                "The lines field cannot be None", ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED)
        if len(self.lines) != 4:
            raise GeometryException(
                "A rectangle need four lines to be drawn", ErrorCodes.ERROR_INVALID_PARAMETER_SIZE)
        if not (Geometry.consecutive_straight_lines(lines[0].points, lines[1].points) and
                Geometry.consecutive_straight_lines(lines[3].points, lines[4].points)) or \
                (Geometry.consecutive_straight_lines(lines[0].points, lines[2].points) and
                 Geometry.consecutive_straight_lines(lines[1].points, lines[4].points)) or \
                (Geometry.consecutive_straight_lines(lines[0].points, lines[3].points) and
                 Geometry.consecutive_straight_lines(lines[1].points, lines[2].points)):
            raise GeometryException(
                "Rectangle lines must be connected", ErrorCodes.ERROR_INVALID_PARAMETER_FORMAT)
        if not ((lines[0].size == lines[1].size and lines[2].size == lines[3].size) or
                (lines[0].size == lines[2].size and lines[1].size == lines[3].size) or
                (lines[0].size == lines[3].size and lines[1].size == lines[2].size)):
            raise GeometryException(
                "A Rectangle need that two vertical lines and two horizontal line with same time", ErrorCodes.ERROR_INVALID_PARAMETER_SIZE)
        self.__points__ = [line.points for line in self.lines]

    @property
    def points(self) -> list[Point]:
        return self.__points__

    def __str__(self) -> str:
        return "Rectangle: {}".format([str(line) for line in self.lines])


class Square(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Square, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException(
                "The lines field cannot be None", ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED)
        if len(self.lines) != 4:
            raise GeometryException(
                "A square need four lines to be drawn", ErrorCodes.ERROR_INVALID_PARAMETER_SIZE)
        if not (Geometry.consecutive_straight_lines(lines[0].points, lines[1].points) and
                Geometry.consecutive_straight_lines(lines[3].points, lines[4].points)) or \
                (Geometry.consecutive_straight_lines(lines[0].points, lines[2].points) and
                 Geometry.consecutive_straight_lines(lines[1].points, lines[4].points)) or \
                (Geometry.consecutive_straight_lines(lines[0].points, lines[3].points) and
                 Geometry.consecutive_straight_lines(lines[1].points, lines[2].points)):
            raise GeometryException(
                "Square lines must be connected", ErrorCodes.ERROR_INVALID_PARAMETER_FORMAT)
        if not (lines[0].size == lines[1].size and lines[1].size == lines[2].size and lines[2].size == lines[3].size):
            raise GeometryException(
                "A square need that four lines have same size", ErrorCodes.ERROR_INVALID_PARAMETER_SIZE)
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def area(self):
        return self.lines[0].size ** 2

    @property
    def perimeter(self):
        return self.lines[0].size * 4

    @property
    def diagonal(self):
        return self.lines[0].size * math.sqrt(2)

    def __str__(self) -> str:
        return "Rectangle: {}".format([str(line) for line in self.lines])


class Rhombus(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Rhombus, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException(
                "The lines field cannot be None", ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED)
        if len(self.lines) != 4:
            raise GeometryException(
                "A rhombus need four lines to be drawn", ErrorCodes.ERROR_INVALID_PARAMETER_SIZE)
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class Pentagon(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Pentagon, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException("The lines field cannot be None")
        if len(self.lines) != 5:
            raise GeometryException(
                "A pentagon need five lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class Hexagon(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Hexagon, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException("The lines field cannot be None")
        if len(self.lines) != 6:
            raise GeometryException(
                "A hexagon need six lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class Heptagon(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Heptagon, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException("The lines field cannot be None")
        if len(self.lines) != 7:
            raise GeometryException(
                "A heptagon need seven lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class Octagon(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Octagon, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException("The lines field cannot be None")
        if len(self.lines) != 8:
            raise GeometryException(
                "A octagon need eight lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class Nonagon(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Nonagon, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException("The lines field cannot be None")
        if len(self.lines) != 9:
            raise GeometryException(
                "A nonagon need nine lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class Decagon(Shape):
    def __init__(self, lines: list[LineSegment]) -> None:
        super(Decagon, self)
        self.lines = lines
        self.__points__: list[Point] = []
        if self.lines is None:
            raise GeometryException("The lines field cannot be None")
        if len(self.lines) != 10:
            raise GeometryException(
                "A decagon need ten lines(StraightLine) to be drawn")
        points = []
        for line in self.lines:
            points += line.points
        self.__points__ = points

    @ property
    def points(self) -> list[Point]:
        return self.__points__


class SemiCurve(Shape):

    def __init__(self, points: list[Point]) -> None:
        self.__points__: list[Point] = []
        self.__qbc__: QuadraticBezierCurve
        if points is None:
            raise GeometryException("The points field cannot be None")
        if len(points) != 3:
            raise GeometryException(
                "The field points must have length equals to three")
        self.__qbc__ = QuadraticBezierCurve(
            a=points[0], b=points[1], c=points[2])
        self.__points__ = self.__qbc__.build()

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def qbc(self) -> QuadraticBezierCurve:
        return self.__qbc__


class Curve(Shape):
    def __init__(self, points: list[Point]) -> None:
        self.__points__: list[Point] = []
        self.__cbc__: CubicBezierCurve
        if points is None:
            raise GeometryException("The points field cannot be None")
        if len(points) != 4:
            raise GeometryException(
                "The field points must have length equals to four")
        self.__cbc__ = CubicBezierCurve(
            a=points[0], b=points[1], c=points[2], d=points[3])
        self.__points__ = self.__cbc__.build()

    @property
    def points(self) -> list[Point]:
        return self.__points__

    @property
    def cbc(self) -> CubicBezierCurve:
        return self.__cbc__
