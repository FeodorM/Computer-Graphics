from util.matrix import Matrix


class Model2D:
    def __init__(self, vertices_file: str = None, edges_file: str = None):
        self.vertices = [[0], [0], [1]]
        self.edges = []

        if vertices_file is not None:
            self.load_vertices_from_file(vertices_file)

        if edges_file is not None:
            self.load_edges_from_file(edges_file)

    def __getitem__(self, item):
        den = 1 / self.vertices[2][item]
        return self.vertices[0][item] * den, self.vertices[1][item] * den

    @staticmethod
    def line_to_skip(line):
        return line.startswith('#') or line == '\n'

    def add_vertex(self, xy):
        self.vertices[0].append(xy[0])
        self.vertices[1].append(xy[1])
        self.vertices[2].append(1)

    def load_vertices_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    self.add_vertex(tuple(map(float, line.strip().split())))

    def load_edges_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    edge = tuple(map(lambda x: int(x) + 1, line.strip().split()))
                    self.edges.append(edge)

    def apply(self, a: Matrix):
        self.vertices = a * self.vertices

    @property
    def center(self):
        return self[0]
