import abc
from enum import Enum
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
