from abc import ABC, abstractmethod, abstractclassmethod


class ShapeABC_2D(ABC):

    @abstractmethod
    def perimetr(self) -> float:
        """
        Вычисляеет периметр фигуры
        """

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры
        """
        pass

    @abstractclassmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Возвращает название фигуры
        """
        pass


class ShapeABC_3D(ABC):

    @abstractmethod
    def volume(self) -> float:
        """
        Вычисляеет периметр фигуры
        """
        pass

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры
        """
        pass

    @abstractclassmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Возвращает название фигуры
        """
        pass
