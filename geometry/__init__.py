import math
from re import L

from core import Point


class Geometry:
    # todo, melhorar esse lixo
    @staticmethod
    def consecutive_straight_lines(points_line1: list[Point], points_line2: list[Point]) -> bool:
        if points_line1 is None or points_line2 is None:
            return False
        line1 = []
        for point in points_line1:
            line1.append(("{:.2f}".format(point.x), "{:.2f}".format(point.y)))
        result = False
        for point in points_line2:
            value = ("{:.2f}".format(point.x), "{:.2f}".format(point.y))
            if value in line1:
                result = True
                break
        return result

    @staticmethod
    def slope(first_point: Point, last_point: Point) -> float:
        return (last_point.y - first_point.y) / (last_point.x - first_point.x)

    @staticmethod
    def is_perpendicular(line1: list[Point], line2: list[Point]) -> bool:
        if line1 is None or line2 is None:
            return False
        return math.floor(Geometry.slope(line1[0], line1[1]) * Geometry.slope(line2[0], line2[1])) == -1

    @staticmethod
    def angle_between_straight_lines(points_line1: list[Point], points_line2: list[Point]) -> float:
        slope_sl1 = Geometry.slope(points_line1[0], points_line1[-1])
        slope_sl2 = Geometry.slope(points_line2[0], points_line2[-1])
        theta = (slope_sl1 - slope_sl2) / (1 + (slope_sl1 * slope_sl2))
        return math.atan(theta)
