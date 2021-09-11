import abc

from directives.point import Point


class Segment(metaclass=abc.ABCMeta):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
