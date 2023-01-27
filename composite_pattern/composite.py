from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def move(self):
        pass
    pass


class Shape(Component):

    def move(self):
        print("Move shape")

    def render(self):
        print("Render shape")


class Group(Component):

    def __init__(self):
        self._components = []

    def add(self, shape):
        self._components.append(shape)

    def render(self):
        for component in self._components:
            component.render()

    def move(self):
        for component in self._components:
            component.move()


group1 = Group()
group1.add(Shape())  # Imaginary square shapes
group1.add(Shape())

group2 = Group()
group2.add(Shape())  # Imaginary circle shapes
group2.add(Shape())

group = Group()  # Creating a group that contains groups

group.add(group1)
group.add(group2)

group.render()
group.move()