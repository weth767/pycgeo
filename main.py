from model.linestraight import LineStraight
from model.point import Point

if __name__ == "__main__":
    point_b = Point(1, 1)
    point_a = Point(2, 2)
    st = LineStraight(point_a, point_b)
    print(st)