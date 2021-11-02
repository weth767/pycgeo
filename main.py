from base.bezier import LinerBezierCurve, QuadraticBezierCurve, CubicBezierCurve
from directives.point import Point
from resources.pygamecanvas import PygameCanvas


def main():
    apoint = Point(x=100, y=120)
    bpoint = Point(x=500, y=250)
    cpoint = Point(x=50, y=400)
    dpoint = Point(x=250, y=420)
    lbc = LinerBezierCurve(a=apoint, b=bpoint)
    qbc = QuadraticBezierCurve(a=apoint, b=bpoint, c=cpoint)
    cbc = CubicBezierCurve(a=apoint, b=bpoint, c=cpoint, d=dpoint)
    points = lbc.build()
    points1 = qbc.build()
    points2 = cbc.build()
    canvas = PygameCanvas(width=500, height=500)
    canvas.draw(points=points2)


if __name__ == '__main__':
    main()
