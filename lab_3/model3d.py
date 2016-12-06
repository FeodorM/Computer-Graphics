from util.matrix import Matrix


class Model3D:
    def __init__(self, vertices_file: str = None, verges_file: str = None):
        self.vertices = [[0], [0], [0], [1]]
        self.verges = []
        self.edges = []

        if vertices_file is not None:
            self.load_vertices_from_file(vertices_file)

        if verges_file is not None:
            self.load_verges_from_file(verges_file)

    def __getitem__(self, item):
        den = 1 / self.vertices[3][item]
        return self.vertices[0][item] * den, self.vertices[1][item] * den, self.vertices[2][item] * den

    @staticmethod
    def line_to_skip(line):
        return line.startswith('#') or line == '\n'

    def add_vertex(self, xyz):
        self.vertices[0].append(xyz[0])
        self.vertices[1].append(xyz[1])
        self.vertices[2].append(xyz[2])
        self.vertices[3].append(1)

    def load_vertices_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if self.line_to_skip(line):
                    continue
                self.add_vertex(tuple(map(float, line.strip().split())))

    def load_verges_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    verge = tuple(map(lambda x: int(x) + 1, line.strip().split()))
                    self.verges.append(verge)
        self.load_edges_from_verges()

    def load_edges_from_verges(self):
        edges = set()
        for verge in self.verges:
            edges.add((verge[0], verge[1]))
            edges.add((verge[1], verge[2]))
            edges.add((verge[2], verge[0]))
        self.edges.extend(list(edges))

    def apply(self, a: Matrix):
        self.vertices = a * self.vertices

    @property
    def center(self):
        return self[0]
