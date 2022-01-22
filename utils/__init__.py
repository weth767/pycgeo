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
