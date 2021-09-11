from directives.point import Point
from resources.pygamecanvas import PygameCanvas


def main():
    apoint = Point(x=100, y=100)
    bpoint = Point(x=150, y=150)
    cpoint = Point(x=50, y=50)
    canvas = PygameCanvas(width=500, height=500)
    canvas.draw(points=[apoint, bpoint, cpoint])


if __name__ == '__main__':
    main()
