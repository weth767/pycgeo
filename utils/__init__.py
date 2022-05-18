from core import Point


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def validate_points_filled(p: Point) -> bool:
        return not(p is None or p.x is None or p.y is None)

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int):
        return '#{:X}{:X}{:X}'.format(r, g, b)

    @staticmethod
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
