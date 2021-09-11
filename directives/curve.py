import abc
import sys

import pygame
from pygame.surface import Surface

from directives.point import Point
from directives.segment import Segment
from errors.messages import Messages
from resources.canvas import Canvas


class Curve(metaclass=abc.ABCMeta):
    pygame.init()
    screen = pygame.display.set_mode((300, 300))

    def __init__(self, segments: list, points: list, canvas: Surface):
        self._useSegments = False
        self._usePoints = False
        self.a = None
        self.b = None
        self.c = None
        self.seg1 = None
        self.seg2 = None
        if canvas is not None:
            self.canvas = canvas
        try:
            if len(points) == 3:
                self.a: Point = points[0]
                self.b: Point = points[1]
                self.c: Point = points[2]
                self._usePoints = True
                return
            if len(segments) == 2:
                self.seg1: Segment = segments[0]
                self.seg2: Segment = segments[1]
                self._useSegments = True
                return
        except TypeError:
            print(Messages.C_MS01)

    def _verifyRules(self):
        if not self._useSegments and not self._usePoints:
            raise ValueError(Messages.SP_MS01)
        if self._useSegments and not self._usePoints and (self.seg1 is None or self.seg2 is None):
            raise ValueError(Messages.SP_MS02)
        if self._usePoints and not self._useSegments and (self.a is None or self.b is None or self.c is None):
            raise ValueError(Messages.SP_MS03)

    def show(self):
        self._verifyRules()
