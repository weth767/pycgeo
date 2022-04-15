from core import LinearBezierCurve, Point
from resources import Board, TkinterScreen, Canvas, PygameScreen
from shapes import Triangle, Rectangle, Circle, StraightLine


def main():
    apoint = Point(x=100, y=80)
    bpoint = Point(x=160, y=200)
    cpoint = Point(x=220, y=80)
    circle = Circle(radius=10, point=apoint)
    canvas1 = Canvas(250, 250, Point(x=200, y=200), "canvas1", [circle], show_cp=True)
    canvas2 = Canvas(260, 260, Point(x=450, y=450), "canvas2", [circle], show_cp=True)
    canvas3 = Canvas(270, 270, Point(x=710, y=710), "canvas3", [circle], show_cp=True)
    canvas_list = [canvas1, canvas2, canvas3]
    screen = PygameScreen()
    screen.configure(canvas_list)
    board = Board(screen)
    board.draw_at()


if __name__ == '__main__':
    main()
