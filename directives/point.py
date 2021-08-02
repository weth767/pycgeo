import math


class Point:
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.z = kwargs.get('z')

    def __str__(self):
        return f"x: {self.x}, y: {self.y}" if self.z is None else f"x: {self.x}, y: {self.y}, z: {self.z}"

    def distance(self, point: "Point"):
        if self.z is None and point.z is None:
            return math.sqrt((math.pow((self.x - point.x), 2) + math.pow((self.y - point.y), 2)))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return math.sqrt((math.pow((self.x - point.x), 2) + math.pow((self.y - point.y), 2)
                          + math.pow((self.z - point.z), 2)))

    def median_point(self, point: "Point"):
        if self.z is None and point.z is None:
            return Point(x=(self.x + point.x), y=(self.y + point.y))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return Point(x=(self.x + point.x), y=(self.y + point.y), z=(self.z + point.z))

    def __sub__(self, point: "Point"):
        if not isinstance(point, Point):
            raise ArithmeticError("Isn't possible to sub 'Point' with another type of data")
        if self.z is None and point.z is None:
            return Point(x=(self.x - point.x), y=(self.y - point.y))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return Point(x=(self.x - point.x), y=(self.y - point.y), z=(self.z - point.z))

    def __add__(self, point: "Point"):
        if not isinstance(point, Point):
            raise ArithmeticError("Isn't possible to add 'Point' with another type of data")
        if self.z is None and point.z is None:
            return Point(x=(self.x + point.x), y=(self.y + point.y))
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return Point(x=(self.x + point.x), y=(self.y + point.y), z=(self.z + point.z))

    def __eq__(self, point: "Point"):
        if not isinstance(point, Point):
            raise AssertionError("Isn't possible to compare 'Point' with another type of data")
        if self.z is None and point.z is None:
            return self.x == point.x and self.y == point.y
        if self.z is None:
            self.z = 0
        if point.z is None:
            point.z = 0
        return self.x == point.x and self.y == point.y and self.z == point.z

    def __mul__(self, value):
        if value is None:
            raise ArithmeticError("Isn't possible to multiply a 'Point' with None value")
        if type(value) != float and type(value) != int:
            raise ArithmeticError("Isn't possible to multiply 'Point' with type different than int or float")
        if self.z is None:
            return Point(x=(self.x * value), y=(self.y * value))
        return Point(x=(self.x * value), y=(self.y * value), z=(self.z * value))

    def show(self):
        raise NotImplementedError("Need to override and implement this method with your favorite graphics library")
