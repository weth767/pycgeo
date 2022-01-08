import abc
from enum import Enum

from core import Point
from errors import Messages
from resources import PygameCanvas, TkinterCanvas, Canvas


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, draw_module: Canvas):
        self.draw_module = draw_module
        self.canvas = None

    @abc.abstractmethod
    def draw(self, **kwargs):
        pass


class Circle(Shape):
    def __init__(self, draw_module: Canvas):
        super(Circle, self).__init__(draw_module)

    def draw(self, **kwargs):
        radius = kwargs.get('radius')
        point = kwargs.get('point')
        if radius is None:
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


class Triangle(Shape):
    def __init__(self, draw_module: Canvas):
        super(Triangle, self).__init__(draw_module)

    def draw(self, **kwargs):
        linear_bezier_curves = kwargs.get('linear_bezier_curves')
        if linear_bezier_curves is None or type(linear_bezier_curves) != list:
            raise Exception(Messages.C_MS02)
        # validar as regras do triangulo
        if len(linear_bezier_curves) != 3:
            raise Exception("O Triangulo precisa possuir 3 linhas de Bezier")
        # e criar uma lista de pontos
        points_lbc1 = linear_bezier_curves[0].build()
        points_lbc2 = linear_bezier_curves[1].build()
        points_lbc3 = linear_bezier_curves[2].build()
        self.draw_module.draw(points=points_lbc1 + points_lbc2 + points_lbc3)


class Rectangle(Shape):
    def __init__(self, draw_module: Canvas):
        super(Rectangle, self).__init__(draw_module)

    def draw(self, **kwargs):
        linear_bezier_curves = kwargs.get('linear_bezier_curves')
        if linear_bezier_curves is None or type(linear_bezier_curves) != list:
            raise Exception(Messages.C_MS02)
        # validar as regras do triangulo
        if len(linear_bezier_curves) != 4:
            raise Exception("O Quadrado precisa possuir 4 linhas de Bezier")
        # e criar uma lista de pontos
        points_lbc1 = linear_bezier_curves[0].build()
        points_lbc2 = linear_bezier_curves[1].build()
        points_lbc3 = linear_bezier_curves[2].build()
        points_lbc4 = linear_bezier_curves[3].build()
        self.draw_module.draw(points=points_lbc1 + points_lbc2 + points_lbc3 + points_lbc4)