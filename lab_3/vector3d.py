from numbers import Number
from typing import Sequence


class Vector:
    def __init__(self, x, y, z):
        if isinstance(x, Sequence) and y is None and z is None:
            self.__x, self.__y, self.__z = x
        elif isinstance(x, Vector) and y is None and z is None:
            self.__x = x.x
            self.__y = x.y
            self.__z = x.z
        else:
            self.__x = x
            self.__y = y
            self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @property
    def norm(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** .5

    def __mul__(self, other):
        """
        Умнодение вектора на число
        :param other: Number
        :return: Vector
        """
        assert isinstance(other, Number), "Multiplier should be a number"
        return Vector(self.x * other, self.y * other, self.z * other)

    def normalised(self):
        """
        Возвращает нормированный вектор
        :return: Vector
        """
        norm = self.norm
        return Vector(self.x / norm, self.y / norm, self.z / norm)

    def dot(self, other):
        """
        Скалярное произведение
        :return: Number >= 0
        """
        assert isinstance(other, Vector), "Multiplier should be a vector"
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        """
        Векторное произведение
        :param other: Vector
        :return: Vector
        """
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )


