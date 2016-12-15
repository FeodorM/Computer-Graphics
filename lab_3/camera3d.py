import pygame

from lab_2.camera2d import Camera2D
from lab_3.vector3d import Vector
from util.matrix import Matrix


class Camera3D(Camera2D):
    def __init__(self, title: str = "Lab 3",
                 left: float = -2, right: float = 2,
                 bottom: float = -2, top: float = 2,
                 width: int = 600, height: int = 600,
                 screen_center: Vector = Vector(0, 0, -3), normal: Vector = Vector(0, 0, 1),
                 top_direction: Vector = Vector(0, 1, 0), distance: float = 10):
        super().__init__(title, left, right, bottom, top, width, height)

        self.Ov = screen_center
        self.N = normal
        self.Top = top_direction
        self.D = distance

        self.__S_w_to_v = None
        self.__S_v_to_p = None
        self.__S_w_to_p = None
        self._calc_matrices()

    @property
    def world_to_view(self):
        return self.__S_w_to_v

    @property
    def view_to_project(self):
        return self.__S_v_to_p

    @property
    def world_to_project(self):
        return self.__S_w_to_p

    def _calc_matrices(self):
        kv = self.N.normalised()
        iv = self.Top.cross_product(self.N).normalised()
        jv = kv.cross_product(iv)
        self.__S_w_to_v = Matrix([
            [iv.x, iv.y, iv.z, -iv.dot(self.Ov)],
            [jv.x, jv.y, jv.z, -jv.dot(self.Ov)],
            [kv.x, kv.y, kv.z, -kv.dot(self.Ov)],
            [0,       0,    0,                1]
        ])
        self.__S_v_to_p = Matrix([
            [1, 0,           0, 0],
            [0, 1,           0, 0],
            [0, 0, -1 / self.D, 1]
        ])
        self.__S_w_to_p = self.__S_v_to_p * self.__S_w_to_v
