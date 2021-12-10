from core import LinerBezierCurve, QuadraticBezierCurve, CubicBezierCurve, Point
from resources import PygameCanvas
from shapes import Triangle


def main():
    apoint = Point(x=100, y=120)
    bpoint = Point(x=500, y=250)
    cpoint = Point(x=50, y=400)
    dpoint = Point(x=250, y=420)
    lbc = LinerBezierCurve(a=apoint, b=bpoint)
    lbc2 = LinerBezierCurve(a=bpoint, b=cpoint)
    lbc3 = LinerBezierCurve(a=cpoint, b=dpoint)
    # qbc = QuadraticBezierCurve(a=apoint, b=bpoint, c=cpoint)
    # cbc = CubicBezierCurve(a=apoint, b=bpoint, c=cpoint, d=dpoint)
    # points = lbc.build()
    # points1 = qbc.build()
    # points2 = cbc.build()
    # canvas = PygameCanvas(width=500, height=500)
    # canvas.draw(points=points2)
    triangle = Triangle(draw_module=PygameCanvas())
    triangle.draw(linear_bezier_curves=[lbc, lbc2, lbc3])


if __name__ == '__main__':
    main()
