from model.point import Point
import matplotlib.pyplot as plt 


class HullConvex:
    def __init__(self, points):
        self.points = points


a = Point(x=1, y=4)
b = Point(x=6, y=2)
c = Point(x=4, y=12)
d = Point(x=8, y=9)
e = Point(x=15, y=6)
f = Point(x=17, y=23)
p = [a, b, c, d, e, f]
_stack = []


def find_most_bottom_right_point(points: list):
    if len(points) == 0:
        return None
    less_y = [points[0]]
    for i in range(1, len(points)):
        if points[i].y < less_y[0].y:
            less_y[0] = points[i]
            continue
        if points[i].y == less_y[0].y:
            less_y.append(points[i])
            continue
    if len(less_y) > 1:
        less_x = less_y[0]
        for i in range(1, len(less_y)):
            if less_y[i].x > less_x.x:
                less_x = less_y
        return less_x
    points.remove(less_y[0])
    points.sort()
    return less_y[0]


def polar_angle(p1, p2):
    return 0


point0 = find_most_bottom_right_point(p)
remaining_points = p
print(point0)
print(remaining_points)
