from base.bezier import LinerBezierCurve, QuadraticBezierCurve
from directives.point import Point
from resources.pygamecanvas import PygameCanvas


def main():
    apoint = Point(x=100, y=120)
    bpoint = Point(x=500, y=250)
    cpoint = Point(x=300, y=400)
    lbc = LinerBezierCurve(a=apoint, b=bpoint)
    qbc = QuadraticBezierCurve(a=apoint, b=bpoint, c=cpoint)
    points = lbc.build()
    points1 = qbc.build()
    canvas = PygameCanvas(width=500, height=500)
    canvas.draw(points=points1)


if __name__ == '__main__':
    main()
