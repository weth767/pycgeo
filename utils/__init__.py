from core import Point


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def validate_points_filled(p: Point) -> bool:
        return not(p is None or p.x is None or p.y is None)
