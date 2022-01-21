import abc

from core import Point, LinearBezierCurve
from errors import Messages
from resources import Canvas
from utils import Utils


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, draw_module: Canvas):
        self.draw_module = draw_module
        self.canvas = None

    @abc.abstractmethod
    def draw(self, **kwargs):
        pass


class Circle(Shape):
    """
    Circle class, that implements all methods of Shape Abstract Class and

    """
    def __init__(self, draw_module: Canvas):
        super(Circle, self).__init__(draw_module)

    def draw(self, **kwargs):
        radius = kwargs.get('radius')
        point = kwargs.get('point')
        if radius is None or point is None:
            raise Exception(Messages.C_MS02)
        x = radius
        error = 1 - x
        y = 0
        points = []
        while y <= x:
            points.append(Point(x=x + point.x, y=y + point.y))
            points.append(Point(x=y + point.x, y=x + point.y))
            points.append(Point(x=-x + point.x, y=y + point.y))
            points.append(Point(x=-y + point.x, y=x + point.y))
            points.append(Point(x=-x + point.x, y=-y + point.y))
            points.append(Point(x=-y + point.x, y=-x + point.y))
            points.append(Point(x=x + point.x, y=-y + point.y))
            points.append(Point(x=y + point.x, y=-x + point.y))
            y = y + 1
            if error < 0:
                error += 2 * y + 1
            else:
                x = x - 1
                error += 2 * (y - x + 1)
        self.draw_module.draw(points=points)


class StraightLine(Shape):
    """
    Straight Line Class that implements all methods of Shape Abstract Class and implements build method of Linear
    Bézier curve to represent a Straight Line geometric shape
    """
    def __init__(self, draw_module: Canvas = None, a: Point = None, b: Point = None):
        """
        Class constructor method, to set draw module or/and a and b points
        :param draw_module(Canvas)
        :return None:
        """
        self.b = b
        self.a = a
        self.draw_module = draw_module
        super(StraightLine, self).__init__(draw_module)

    def build(self) -> list[Point]:
        """
        This method only to return a list of Point, not calling the draw module to set data on screen
        :return List[Point]:
        """
        if not(Utils.validate_points_filled(self.a)) or not(Utils.validate_points_filled(self.b)):
            raise Exception("To execute build method, 'a' and 'b' must not be None")
        lbc = LinearBezierCurve(self.a, self.b)
        return lbc.build()

    def draw(self, **kwargs):
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
        if self.draw_module is None:
            raise Exception("Draw module cannot be None on draw method call!")
        if x is not None and isinstance(x, Point) and y is not None and isinstance(y, Point):
            lbc = LinearBezierCurve(a=x, b=y)
            points = lbc.build()
            self.draw_module.draw(points=points)
            return
        if linear_bezier_curve is not None and isinstance(linear_bezier_curve, LinearBezierCurve):
            points = linear_bezier_curve.build()
            self.draw_module.draw(points=points)
            return
        raise Exception("To draw is necessary to inform x and y or linear bezier curve params!")


class Triangle(Shape):
    """
    Triangle Class, that implements all methods of Shape Abstract Class to represent a triangle geometric shape
    """
    def __init__(self, draw_module: Canvas):
        """
       Class constructor method, to set draw module
       :param draw_module(Canvas)
       :return None:
       """
        super(Triangle, self).__init__(draw_module)

    def draw(self, **kwargs):
        """
        Implementation of abstract class Shape method to transcribe figure to any graphic module(draw_module)
        :param kwargs:
        :keyword lines(list[StraightLine]) List of StraightLines, with minimum length equal three, where,
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
        self.draw_module.draw(points=points_lbc1 + points_lbc2 + points_lbc3)


class Rectangle(Shape):
    def __init__(self, draw_module: Canvas):
        """
        Class constructor method, to set draw module
        :param draw_module(Canvas)
        :return None:
        """
        super(Rectangle, self).__init__(draw_module)

    def draw(self, **kwargs):
        """
            Implementation of abstract class Shape method to transcribe figure to any graphic module(draw_module)
            :param kwargs:
            :keyword lines(list[StraightLine]) List of StraightLines, with minimum length equal four, where,
            the lines are interconnected
            :return:
        """
        linear_bezier_curves = kwargs.get('linear_bezier_curves')
        if linear_bezier_curves is None or type(linear_bezier_curves) != list:
            raise Exception(Messages.C_MS02)
        # validar as regras do retangulo
        if len(linear_bezier_curves) != 4:
            raise Exception("O Quadrado precisa possuir 4 linhas de Bezier")
        # e criar uma lista de pontos
        points_lbc1 = linear_bezier_curves[0].build()
        points_lbc2 = linear_bezier_curves[1].build()
        points_lbc3 = linear_bezier_curves[2].build()
        points_lbc4 = linear_bezier_curves[3].build()
        self.draw_module.draw(points=points_lbc1 + points_lbc2 + points_lbc3 + points_lbc4)