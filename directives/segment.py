import abc

from directives.point import Point


class Segment(metaclass=abc.ABCMeta):
    def __init__(self, apoint: Point, bpoint: Point):
        self.apoint = apoint
        self.bpoint = bpoint
