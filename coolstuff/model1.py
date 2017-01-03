from math import cos, sin

from coolstuff.base_model import BaseModel
from util.matrix import Matrix


def update_model(func):
    def wrapped(self, *args):
        func(self, *args)
        self._calc_current_vertices()
    return wrapped


class Model1(BaseModel):
    def __init__(self, vertices_file: str = None, edges_file: str = None):
        super().__init__(vertices_file, edges_file)

        self.x_p = 0
        self.y_p = 0
        self.alpha = 0
        self.kx = 1
        self.ky = 1

        self._calc_current_vertices()

    def _calc_current_vertices(self):
        x, y, kx, ky = self.x_p, self.y_p, self.kx, self.ky
        c = cos(self.alpha)
        s = sin(self.alpha)
        self.vertices_current = Matrix([
            [kx * c, - ky * s, x],
            [kx * s,   ky * c, y],
            [0,        0,      1]
        ]) * self.vertices_initial

    @update_model
    def translate(self, x, y):
        self.x_p += x
        self.y_p += y

    @update_model
    def rotate(self, alpha):
        self.alpha += alpha

    @update_model
    def scale(self, kx, ky=None):
        if ky is None:
            ky = kx
        self.kx *= kx
        self.ky *= ky

    @update_model
    def mirror(self):
        self.kx *= -1
        self.ky *= -1

    @update_model
    def mirror_x(self):
        self.ky *= -1

    @update_model
    def mirror_y(self):
        self.kx *= -1
