from core import LinearBezierCurve, Point
from resources import PygameCanvas
from shapes import Triangle, Rectangle, Circle


def main():
    apoint = Point(x=100, y=80)
    bpoint = Point(x=160, y=140)
    cpoint = Point(x=220, y=80)
    # apoint = Point(x=100, y=260)
    # bpoint = Point(x=160, y=200)
    # cpoint = Point(x=220, y=260)
    lbc = LinearBezierCurve(a=apoint, b=bpoint)
    lbc2 = LinearBezierCurve(a=bpoint, b=cpoint)
    lbc3 = LinearBezierCurve(a=cpoint, b=apoint)
    triangle = Triangle(draw_module=PygameCanvas())
    triangle.draw(linear_bezier_curves=[lbc, lbc2, lbc3])
    # circle = Circle(draw_module=PygameCanvas())
    # circle.draw(point=apoint, radius=50)
    ### rectangle
    # dpoint = Point(x=100, y=40)
    # epoint = Point(x=100, y=120)
    # fpoint = Point(x=180, y=120)
    # gpoint = Point(x=180, y=40)
    # lbc = LinerBezierCurve(a=dpoint, b=epoint)
    # lbc2 = LinerBezierCurve(a=epoint, b=fpoint)
    # lbc3 = LinerBezierCurve(a=fpoint, b=gpoint)
    # lbc4 = LinerBezierCurve(a=gpoint, b=dpoint)
    # rectangle = Rectangle(draw_module=PygameCanvas())
    # rectangle.draw(linear_bezier_curves=[lbc, lbc2, lbc3, lbc4])


if __name__ == '__main__':
    main()