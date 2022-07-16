from enum import Enum
import locale


class Utils:
    def __init__(self):
        pass

    @ staticmethod
    def rgb_to_hex(r: int, g: int, b: int):
        return '#{:X}{:X}{:X}'.format(r, g, b)

    @ staticmethod
    def rgb_tuple_to_rex(rgb: tuple) -> str:
        if len(rgb) != 3:
            return ''
        return '#{:X}{:X}{:X}'.format(rgb[0], rgb[1], rgb[2])


class Consts:
    DEFAULT_SCREEN_WIDTH = 800
    DEFAULT_SCREEN_HEIGHT = 800
    DEFAULT_FONT_SIZE = 9
    DEFAULT_FONT_FAMILY = 'Arial'


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 127, 0)
    PURPLE = (255, 0, 255)
    PINK = (255, 0, 127)
    GRAY = (127, 127, 127)
    DARK_BLUE = (0, 0, 127)
    DARK_RED = (127, 0, 0)
    DARK_GREEN = (0, 127, 0)
    LIGHT_GREEN = (127, 255, 0)
    LIGHT_RED = (255, 80, 80)
    LIGHT_BLUE = (0, 200, 255)
    LIME = (0, 255, 127)


class Languages(Enum):
    PT_BR = 'pt_BR'
    EN_US = 'en_US'
    ES_ES = 'es_ES'


class ShapeTypes(Enum):
    LINESEGMENT = 'LINESEGMENT'
    CIRCLE = 'CIRCLE'
    TRIANGLE = 'TRIANGLE'
    RECTANGLE = 'RECTANGLE'
    SQUARE = 'SQUARE'
    PENTAGON = 'PENTAGON'
    HEXAGON = 'HEXAGON'
    HEPTAGON = 'HEPTAGON'
    OCTAGON = 'OCTAGON'
    NONAGON = 'NONAGON'
    DECAGON = 'DECAGON'
    RHOMBUS = 'RHOMBUS'
    SEMICURVE = 'SEMICURVE'
    CURVE = 'CURVE'


class TriangleTypes(Enum):
    EQUILATERAL = 'EQUILATERAL'
    ISOSCELES = 'ISOSCELES'
    SCALENE = 'SCALENE'


class ShapeUtils:
    __types__ = {
        "TRIANGLE": {
            Languages.PT_BR.value: {
                "EQUILATERAL": "Triângulo Equilátero",
                "ISOSCELES": "Triângulo Isósceles",
                "SCALENE": "Triângulo Escaleno"
            },
            Languages.EN_US.value: {
                "EQUILATERAL": "Equilateral Triangle",
                "ISOSCELES": "Isosceles Triangle",
                "SCALENE": "Scalene Triangle"
            },
            Languages.ES_ES.value: {
                "EQUILATERAL": "Triangulo Equilátero",
                "ISOSCELES": "Triangulo Isósceles",
                "SCALENE": "Triangulo Escaleno"
            }
        }
    }

    @staticmethod
    def get_shape_type(shape: ShapeTypes, specific_type=None) -> str:
        language = locale.getdefaultlocale()[0]
        if specific_type is not None:
            return ShapeUtils.__types__[shape.value][language][specific_type]
        return ShapeUtils.__types__[shape.value][language]
