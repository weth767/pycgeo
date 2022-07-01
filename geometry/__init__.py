from shapes import StraightLine
import math


class Geometry:
    @staticmethod
    def slope(straight_line: StraightLine) -> float:
        last_point = straight_line.points[-1]
        first_point = straight_line.points[0]
        # variation between points that this line pass through
        # s = (Y(b) - Y(a)) / (X(b) - X(a))
        print(first_point)
        print(last_point)
        print(last_point.y - first_point.y)
        print(last_point.x - first_point.x)
        return (last_point.y - first_point.y) / (last_point.x - first_point.x)

    @staticmethod
    def angle_between_straight_lines(straight_line1: StraightLine, straight_line2: StraightLine) -> float:
        slope_sl1 = Geometry.slope(straight_line1)
        slope_sl2 = Geometry.slope(straight_line2)
        # Theta = M1 - M2 / 1 + M1 * M2, where M1 and M2 are slopes of straight line 1 and straight line 2 consecutively
        theta = (slope_sl1 - slope_sl2) / (1 + (slope_sl1 * slope_sl2))
        # descobrir o erro no calculo
        print('theta =', theta)
        # angle is tangent of theta
        return math.tan(theta)
