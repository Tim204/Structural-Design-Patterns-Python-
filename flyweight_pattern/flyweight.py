from enum import Enum


class Point:
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = icon

    def draw(self):
        print(f"{self.icon} at {self.x, self.y}")


class PointIcon:
    """
       The Flyweight stores a common portion of the state (also called intrinsic
       state) that belongs to multiple real business entities. The Flyweight
       accepts the rest of the state (extrinsic state, unique for each entity) via
       its method parameters.
       """
    def __init__(self, type, icon):
        self.type = type
        self.icon = icon

    def get_type(self):
        return self.type

    def __str__(self):
        return str(self.type.name)


class PointIconFactory:
    """
        The Flyweight Factory creates and manages the Flyweight objects. It ensures
        that flyweights are shared correctly. When the client requests a flyweight,
        the factory either returns an existing instance or creates a new one, if it
        doesn't exist yet.
    """
    _icons = {}

    def get_point_icon(self, type):
        if not self._icons.__contains__(type):
            icon = PointIcon(type, None)
            self._icons[type] = icon
        return self._icons.get(type)

class PointType(Enum):
    HOSPITAL = 1
    CAFE = 2
    RESTAURANT = 3


class PointService:

    def __init__(self, icon_factory):
        self._icon_factory = icon_factory

    def get_points(self):
        points = []
        point = Point(1, 2, self._icon_factory.get_point_icon(PointType.CAFE))
        points.append(point)

        return points


def client():
    service = PointService(PointIconFactory())
    for point in service.get_points():
        point.draw()


client()
