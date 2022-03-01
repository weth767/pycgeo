from core import LinearBezierCurve, Point
from resources import PygameCanvas, TkinterCanvas
from shapes import Triangle, Rectangle, Circle, StraightLine


def main():
    apoint = Point(x=100, y=80)
    bpoint = Point(x=160, y=200)
    cpoint = Point(x=220, y=80)
    circle = Circle(radius=10, point=apoint)
    canvas = PygameCanvas(show_cartesian_plan=True)
    canvas2 = TkinterCanvas(show_cartesian_plan=True)
    canvas.draw(shapes=[circle])
    canvas2.draw(shapes=[circle])


if __name__ == '__main__':
    main()
