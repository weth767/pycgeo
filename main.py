from directives.curve import Curve
from directives.point import Point


def main():
    apoint = Point(x=10, y=10)
    bpoint = Point(x=10, y=10)
    cpoint = Point(x=10, y=10)
    c = Curve(apoint, bpoint, cpoint)
    c.draw_circle_midpoint(100, 100, 50)


if __name__ == '__main__':
    main()
