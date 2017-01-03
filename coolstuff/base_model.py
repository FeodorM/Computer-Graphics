class BaseModel:
    def __init__(self, vertices_file: str = None, edges_file: str = None):
        self.vertices_initial = [[], [], []]
        self.edges = []

        if vertices_file is not None:
            self.load_vertices_from_file(vertices_file)

        if edges_file is not None:
            self.load_edges_from_file(edges_file)

        self._init()

    def _init(self):
        raise NotImplementedError()

    def __getitem__(self, item):
        den = 1 / self.vertices_current[2][item]
        return self.vertices_current[0][item] * den, self.vertices_current[1][item] * den

    @property
    def center(self):
        return self[0]

    @staticmethod
    def line_to_skip(line):
        return line.startswith('#') or line == '\n'

    def _add_vertex(self, xy):
        self.vertices_initial[0].append(xy[0])
        self.vertices_initial[1].append(xy[1])
        self.vertices_initial[2].append(1)

    def load_vertices_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    self._add_vertex(tuple(map(float, line.strip().split())))

    def load_edges_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if not self.line_to_skip(line):
                    edge = tuple(map(int, line.strip().split()))
                    self.edges.append(edge)
