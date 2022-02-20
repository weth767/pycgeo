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


class Consts:
    DEFAULT_SCREEN_WIDTH = 1000
    DEFAULT_SCREEN_HEIGHT = 1000
    DEFAULT_FONT_SIZE = 9
    DEFAULT_FONT_FAMILY = 'Arial'


class Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
