from math import cos, sin

from util.matrix import Matrix


class Model:
    def __init__(self, vertices_file: str = None, edges_file: str = None):
        self.vertices_initial = [[], [], []]
        self.edges = []

        if vertices_file is not None:
            self.load_vertices_from_file(vertices_file)

        if edges_file is not None:
            self.load_edges_from_file(edges_file)

        self.x_p = 0
        self.y_p = 0
        self.alpha = 0
        self.kx = 1
        self.ky = 1

        self.vertices_current = None
        self._calc_current_vertices()

    def __getitem__(self, item):
        den = 1 / self.vertices_current[2][item]
        return self.vertices_current[0][item] * den, self.vertices_current[1][item] * den

    @property
    def center(self):
        return self[0]

    @staticmethod
    def line_to_skip(line):
        return line.startswith('#') or line == '\n'

    def add_vertex(self, xy):
        self.vertices_initial[0].append(xy[0])
        self.vertices_initial[1].append(xy[1])
        self.vertices_initial[2].append(1)

    def load_vertices_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    self.add_vertex(tuple(map(float, line.strip().split())))

    def load_edges_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    edge = tuple(map(int, line.strip().split()))
                    self.edges.append(edge)

    def _calc_current_vertices(self):
        x, y, kx, ky = self.x_p, self.y_p, self.kx, self.ky
        c = cos(self.alpha)
        s = sin(self.alpha)
        self.vertices_current = Matrix([
            [kx * c, - ky * s, x],
            [kx * s,   ky * c, y],
            [0,        0,      1]
        ]) * self.vertices_initial

    # Affine transforms (setters, actually)

    def translate(self, x, y):
        self.x_p += x
        self.y_p += y
        self._calc_current_vertices()

    def rotate(self, alpha):
        self.alpha += alpha

        self._calc_current_vertices()
