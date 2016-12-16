from time import sleep

from util.matrix import Matrix


class Model3D:
    def __init__(self, vertices_file: str = None, verges_file: str = None,
                 invisible_edges_file: str = None, world_to_project_matrix: Matrix = None):
        self.vertices = [[], [], [], []]
        self.verges = []
        self.edges = []
        self.project_vertices = None
        self.invisible_edges_filename = invisible_edges_file

        if vertices_file is not None:
            self.load_vertices_from_file(vertices_file)

        if verges_file is not None:
            self.load_verges_from_file(verges_file)
            if world_to_project_matrix is not None:
                self.calc_project_vertices(world_to_project_matrix)

    def __getitem__(self, item):
        try:
            den = 1 / self.project_vertices[2][item]
        except ZeroDivisionError:
            # print(self.project_vertices)
            # print(self.vertices)
            sleep(1)
        return self.project_vertices[0][item] * den, self.project_vertices[1][item] * den

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
        # for _ in range(2000):
        #     self.add_vertex((0, 0, 0))

    def load_verges_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    verge = tuple(map(int, line.strip().split()))
                    self.verges.append(verge)
        self.load_edges_from_verges()

    def load_edges_from_verges(self):
        with open(self.invisible_edges_filename) as f:
            invis = set()
            for line in f:
                invis.add(tuple(map(int, line.strip().split())))
        edges = set()
        for verge in self.verges:
            edges.add((verge[0], verge[1]))
            edges.add((verge[1], verge[2]))
            edges.add((verge[2], verge[0]))
        edges = edges - invis
        self.edges.extend(list(edges))

    def calc_project_vertices(self, matrix):
        self.project_vertices = matrix * self.vertices
        # print(matrix)

    def apply(self, affine_transform: Matrix, world_to_project_matrix: Matrix):
        self.vertices = affine_transform * self.vertices
        self.calc_project_vertices(world_to_project_matrix)

    @property
    def center(self):
        den = 1 / self.vertices[3][0]
        return self.vertices[0][0] * den, self.vertices[1][0] * den, self.vertices[2][0] * den
