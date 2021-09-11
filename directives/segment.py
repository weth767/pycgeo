import abc

from directives.point import Point


class Segment(metaclass=abc.ABCMeta):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def is_connect(self, s: "Segment"):
        return self.a.__eq__(s.a) or self.a.__eq__(s.b) or self.b.__eq__(s.a) or self.b.__eq__(s.b)
