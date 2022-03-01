import abc

from core import Point, LinearBezierCurve
from errors import Messages


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.canvas = None

    @property
    def points(self) -> list[Point]:
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
    """
    Straight Line Class that implements all methods of Shape Abstract Class and implements build method of Linear
    Bézier curve to represent a Straight Line geometric shape
    """
    def __init__(self):
        """
        Class constructor method
        :return None:
        """
        super(StraightLine, self)

    def build(self, **kwargs):
        """
        Implementation of abstract class Shape method to transcribe figure to any graphic module(draw_module).
        This method draw a straight line on screen using draw module informed on class init
        :param kwargs:
        :keyword a(Point)
        :keyword b(Point)
        :keyword linear_bezier_curve(LinearBezierCurve)
        :return None:
        """
        x = kwargs.get('a'),
        y = kwargs.get('b'),
        linear_bezier_curve = kwargs.get('linear_bezier_curve')
        if x is not None and isinstance(x, Point) and y is not None and isinstance(y, Point):
            lbc = LinearBezierCurve(a=x, b=y)
            points = lbc.build()
            return points
        if linear_bezier_curve is not None and isinstance(linear_bezier_curve, LinearBezierCurve):
            points = linear_bezier_curve.build()
            return points
        raise Exception("To draw is necessary to inform x and y or linear bezier curve params!")


class Triangle(Shape):
    """
    Triangle Class, that implements all methods of Shape Abstract Class to represent a triangle geometric shape
    """
    def __init__(self):
        """
       Class constructor method, to set draw module
       :return None:
       """
        super(Triangle, self)

    def build(self, **kwargs) -> list[Point]:
        """
        Implementation of abstract class Shape method to transcribe figure to any graphic module(draw_module)
        :param kwargs:
        :keyword lines(list[StraightLine]) List of StraightLines, with length equal three, where,
        the lines are interconnected
        :return:
        """
        lines: list[StraightLine] = kwargs.get('lines')
        if lines is None:
            raise Exception("Field cannot be None")
        # validar as outras regras do triangulo(conectividade dos pontos iniciais e finais de cada linha)
        if len(lines) != 3:
            raise Exception("A triangle need three lines(StraightLine) to be drawn")
        points_lbc1 = lines[0].build()
        points_lbc2 = lines[1].build()
        points_lbc3 = lines[2].build()
        return points_lbc1 + points_lbc2 + points_lbc3


class Rectangle(Shape):
    def __init__(self):
        """
        Class constructor method, to set draw module
        :return None:
        """
        super(Rectangle, self)

    def build(self, **kwargs) -> list[Point]:
        """
            Implementation of abstract class Shape method to transcribe figure to any graphic module(draw_module)
            :param kwargs:
            :keyword lines(list[StraightLine]) List of StraightLines, with length equal four, where,
            the lines are interconnected
            :return:
        """
        lines: list[StraightLine] = kwargs.get('lines')
        if lines is None:
            raise Exception("Field cannot be None")
        # validar as regras do retangulo
        if len(lines) != 4:
            raise Exception("A triangle need three lines(StraightLine) to be drawn")
        # e criar uma lista de pontos
        points_lbc1 = lines[0].build()
        points_lbc2 = lines[1].build()
        points_lbc3 = lines[2].build()
        points_lbc4 = lines[3].build()
        return points_lbc1 + points_lbc2 + points_lbc3 + points_lbc4
        