from math import pi, sin

from base import ShapeABC_2D


class Circle(ShapeABC_2D):

    def __init__(self, radius: float) -> None:
        self._radius = radius

    def perimetr(self) -> float:
        return 2 * pi * self._radius

    def area(self) -> float:
        return pi * self._radius**2

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Trapezoid(ShapeABC_2D):

    def __init__(self, top_side: float, bottom_side: float,
                 left_side: float, right_side: float) -> None:
        self._top_side = top_side
        self._bottom_side = bottom_side
        self._left_side = left_side
        self._right_side = right_side

    def perimetr(self) -> float:
        return self._top_side + self._bottom_side + \
               self._left_side + self._right_side

    def __get_hight(self):
        return (
                self._left_side**2 -
                (((self._bottom_side - self._top_side)**2 +
                   self._left_side**2 - self._right_side**2) /
                 (2 * (self._bottom_side - self._top_side)))**2
                ) ** 0.5

    def area(self) -> float:
        return ((self._top_side + self._bottom_side) / 2) * self.__get_hight()

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Triangle(ShapeABC_2D):

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def perimetr(self) -> float:
        return self._side_a + self._side_b + self._side_c

    def area(self) -> float:
        p = self.perimetr() / 2
        return (p*(p - self._side_a)*(p - self._side_b)*(p - self._side_c))**0.5

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Square(ShapeABC_2D):

    def __init__(self, side: float) -> None:
        self._side = side

    def perimetr(self) -> float:
        return 4 * self._side

    def area(self) -> float:
        return self._side ** 2

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Rectangle(Square):

    def __init__(self, lenght: float, width: float) -> None:
        self._lenght = lenght
        self._width = width

    def perimetr(self) -> float:
        return 2 * (self._lenght + self._width)

    def area(self) -> float:
        return self._lenght * self._width

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Rhombus(Square):

    def __init__(self, side: float, top_corner: float) -> None:
        self._side = side
        self._top_corner = top_corner

    def perimetr(self) -> float:
        return super().perimetr()

    def area(self) -> float:
        return self._side**2 * sin(self._top_corner) * 0.5

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__
