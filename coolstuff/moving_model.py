from coolstuff.base_model import BaseModel
from util.matrix import Matrix


class MovingModel(BaseModel):
    def __init__(self, x, y, x_derivative, y_derivative, vertices_file: str = None, edges_file: str = None):
        super().__init__(vertices_file, edges_file)

        self.x_func = x
        self.y_func = y
        self.x_der_func = x_derivative
        self.y_der_func = y_derivative

        self._t = 0

        self._calc_current_vertices()

    @property
    def x(self):
        return self.x_func(self.t)

    @property
    def y(self):
        return self.y_func(self.t)

    @property
    def x_der(self):
        return self.x_der_func(self.t)

    @property
    def y_der(self):
        return self.y_der_func(self.t)

    @property
    def cos(self):
        x = self.x_der
        y = self.y_der
        return x / (x ** 2 + y ** 2) ** .5

    @property
    def sin(self):
        x = self.x_der
        y = self.y_der
        return y / (x ** 2 + y ** 2) ** .5

    def _calc_current_vertices(self):
        c, s = self.cos, self.sin
        self.vertices_current = Matrix([
            [c, -s, self.x],
            [s,  c, self.y],
            [0,  0,      1]
        ]) * self.vertices_initial

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value
        self._calc_current_vertices()

    def inc(self, value=.01):
        self.t += value

    def dec(self, value=.01):
        self.t -= value
