from model.point import Point

class LineStraight:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        
    def __str__(self):
        return str(self.point_a, self.point_b)