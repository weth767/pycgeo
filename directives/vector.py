from directives.point import Point
import math


class Vector:
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.z = kwargs.get('z')
        self.point = Point(x=self.x, y=self.y, z=self.z)

    def __str__(self):
        return self.point.__str__().replace("x", "a").replace("y", "b").replace("z", "c")

    def modulus(self):
        if self.point.x is None or self.point.y is None:
            raise ArithmeticError("Isn't possible to calculate vector modules if one of components is None")
        if self.point.z is None:
            return math.sqrt((math.pow(self.point.x, 2)) + (math.pow(self.point.y, 2)))
        return math.sqrt((math.pow(self.point.x, 2)) + (math.pow(self.point.y, 2)) + (math.pow(self.point.z, 2)))

    def __add__(self, vector: "Vector"):
        return self.point + vector.point

    def __sub__(self, vector: "Vector"):
        return self.point + vector.point

    def __mul__(self, value):
        if type(value) == Vector:
            if self.z is None:
                return Vector(x=(self.x * value.x), y=(self.y * value.y))
            return Vector(x=(self.x * value.x), y=(self.y * value.y), z=(self.z * value.z))
        return self.point.__mul__(value)
