from abc import ABC, abstractmethod


class Image:
    pass


class Filter(ABC):
    """Abs implementation of filter"""
    @abstractmethod
    def apply(self, image):
        pass


class VividFilter(Filter):
    """Concrete implementation of filter"""
    def apply(self, image):
        print("Applying vivid filter")


class Caramel:
    """Imaginary class from a third party library, therefore can't implement
    The filter interface"""
    def init(self):
        pass

    def render(self, image):
        print("Applying Caramel filter")


class CaramelAdapter(Filter):
    """Caramel adapter works as an adapter by using Composition"""

    def __init__(self):
        self._caramel = Caramel()

    def apply(self, image):
        self._caramel.init()
        self._caramel.render(image)


class ImageView:

    def __init__(self, image):
        self._image = image

    def apply(self, filter):
        filter.apply(self._image)


imageView = ImageView(Image)

imageView.apply(CaramelAdapter())