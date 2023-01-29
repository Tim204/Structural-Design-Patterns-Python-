from enum import Enum


class Point:
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = icon

    def draw(self):
        print(f"{self.icon.name} at {self.x, self.y}")


class PointIcon:
    """The Flyweight"""
    def __init__(self, type, icon):
        self.type = type
        self.icon = icon

    def get_type(self):
        return self.type


class PointIconFactory:
    def get_point_icon(self, type):
        icons = {PointType(type): PointIcon(type)}

class PointType(Enum):
    HOSPITAL = 1
    CAFE = 2
    RESTAURANT = 3


class PointService:

    def get_points(self):
        points = []
        point = Point(1, 2, PointType.CAFE)
        points.append(point)

        return points


def client():
    service = PointService()
    for point in service.get_points():
        point.draw()


client()