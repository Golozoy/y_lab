from math import pi

from base import ShapeABC_3D
from shapes_2D import Circle, Square, Rectangle, Triangle


class Sphere(ShapeABC_3D, Circle):

    def __init__(self, radius: float) -> None:
        self._radius = radius

    def volume(self) -> float:
        return 3 * pi * self._radius**3 / 3

    def area(self) -> float:
        return Circle.area(self) * 4

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Cylinder(ShapeABC_3D, Circle):

    def __init__(self, radius: float, height: float) -> None:
        self._radius = radius
        self._height = height

    def volume(self) -> float:
        return Circle.area(self) * self._height

    def area(self) -> float:
        return Circle.area(self) * 2 + self._height * Circle.perimetr(self)

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Cone(ShapeABC_3D, Circle):

    def __init__(self, radius: float, height: float) -> None:
        self._radius = radius
        self._height = height

    def volume(self) -> float:
        return Circle.area(self) * self._height / 3

    def area(self) -> float:
        return pi * self._radius * (self._radius +
               self._radius**2 + self._height**2)**0.5

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Cube(ShapeABC_3D, Square):

    def __init__(self, side: float) -> None:
        self._side = side

    def volume(self) -> float:
        return Square.area(self) * self._side

    def area(self) -> float:
        return Square.area(self) * 6

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Parallelepiped(ShapeABC_3D, Rectangle):

    def __init__(self, lenght: float, width: float, height: float) -> None:
        self._lenght = lenght
        self._width = width
        self._height = height

    def volume(self) -> float:
        return Rectangle.area(self) * self._height

    def area(self) -> float:
        return Rectangle.area(self) * 2 + self._lenght * self._height * 2 + \
                self._width*self._height*2

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Pyramid_Square(ShapeABC_3D, Square):

    def __init__(self, side: float,  height: float) -> None:
        self._side = side
        self._height = height

    def volume(self) -> float:
        return Square.area(self) * self._height

    def area(self) -> float:
        l = self._height**2 + (2**0.5 * self._side)**0.5 / 2
        return Square.area(self) + 4 * Triangle(l, l, l).area()

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__
