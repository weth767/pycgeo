from model.point import Point


def find_most_bottom_point(points):
    y = min(points)
    return y


a = Point(x=1, y=2)
b = Point(x=3, y=5)
c = Point(x=6, y=2)
d = Point(x=15, y=3)
e = Point(x=12, y=6)
print(find_most_bottom_point([a, b, c, d, e]))
