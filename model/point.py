import math


class Point:
    def __init__(self, *args, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.z = kwargs.get('z')

    def __str__(self):
        if self.z is not None:
            return "(x = {x}, y = {y}, z = {z})".format(x=self.x, y=self.y, z=self.z)
        return "(x = {x}, y = {y})".format(x=self.x, y=self.y)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, point):
        ip1 = math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2)))
        ip2 = math.sqrt((math.pow(point.x, 2) + math.pow(point.y, 2)))
        return ip1 < ip2

    def __gt__(self, point):
        ip1 = math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2)))
        ip2 = math.sqrt((math.pow(point.x, 2) + math.pow(point.y, 2)))
        return ip1 > ip2

    def __eq__(self, point):
        ip1 = math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2)))
        ip2 = math.sqrt((math.pow(point.x, 2) + math.pow(point.y, 2)))
        return ip1 == ip2
