from shapes_2D import Circle, Rectangle, Rhombus, Square, Trapezoid, Triangle
from shapes_3D import Sphere, Cylinder, Cone, Cube, Parallelepiped, Pyramid_Square


class ShapesControl:

    def __init__(self):
        self.__shapes_2d_dict = {
                Circle.get_name(): Circle,
                Trapezoid.get_name(): Trapezoid,
                Triangle.get_name(): Triangle,
                Square.get_name(): Square,
                Rectangle.get_name(): Rectangle,
                Rhombus.get_name(): Rhombus
                }
        self.__shapes_3d_dict = {
                Sphere.get_name(): Sphere,
                Cylinder.get_name(): Cylinder,
                Cone.get_name(): Cone,
                Cube.get_name(): Cube,
                Parallelepiped.get_name(): Parallelepiped,
                Pyramid_Square.get_name(): Pyramid_Square
                }

    def get_shapes_2d(self):
        return self.__shapes_2d_dict

    def get_shapes_3d(self):
        return self.__shapes_3d_dict

    def get_shapes_all(self):
        return self.__shapes_2d_dict | self.__shapes_3d_dict

    @staticmethod
    def str_to_object(_class: str) -> object:
        return ShapesControl().get_shapes_all()[_class]
    
    @staticmethod
    def get_arguments(_class: object) -> list:
        try:
            _class()
        except TypeError as error:
            error = str(error)
            index = error.find(':') + 1
            arguments_lsit = error[index:].split("'")
            return arguments_lsit[1::2]