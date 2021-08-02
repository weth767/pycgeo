from directives.point import Point
import pygame
import sys


#
# class MyPoint(Point):
#     def show_point(self):
#         pygame.init()
#         screen = pygame.display.set_mode((640, 480))
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#             screen.fill((255, 255, 255))
#             pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 1, 1)
#             pygame.display.update()
#
#
# my_point = MyPoint(x=10, y=20)
# my_point1 = MyPoint(x=10, y=40)
#
# my_point.show_point()
# my_point1.show_point()
from directives.vector import Vector


class ConcretePoint(Point):
    def show(self):
        print("showing")


def main():
    # p1 = Point(x=2, y=10)
    # p2 = ConcretePoint(x=1, y=5)
    # print(p1 + p2)
    v1 = Vector(x=3, y=4)
    # print(v1 + v1)
    # print((v1 * 3) + (v1 * 2))
    print(v1.modulus())


main()
