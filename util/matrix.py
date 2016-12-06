from typing import Sequence
from numbers import Number
from tabulate import tabulate


class Matrix(Sequence):
    def __init__(self, matrix: Sequence[Sequence[float]]):
        assert (isinstance(matrix, Sequence) and
                isinstance(matrix, Sequence)), "Wrong data"
        self.__matrix = [[float(x) for x in row] for row in matrix]

    @staticmethod
    def one(rows: int, columns: int):
        return [
            [1 if i == j else 0 for j in range(columns)] for i in range(rows)
        ]

    @staticmethod
    def zero(rows: int, columns: int):
        return [[0] * columns for _ in range(rows)]

    def __repr__(self):
        return 'Matrix({})'.format(self.__matrix)

    def __str__(self):
        return tabulate(self.__matrix)

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, item):
        return self.__matrix.__getitem__(item)

    def __iter__(self):
        return iter(self.__matrix)

    def __mul__(self, other):
        assert isinstance(other, Sequence)
        # Количество столбцов равно количеству строк / элементов
        assert len(self.__matrix[0]) == len(other), "Wrong data"
        if isinstance(other[0], Sequence):
            return Matrix([
                [
                    sum(self[i][k] * other[k][j] for k in range(len(other))) for j in range(len(other[0]))
                ] for i in range(len(self))
            ])
        else:
            return [
                sum(x * y for x, y in zip(row, other)) for row in self
            ]

    def __rmul__(self, other):
        assert isinstance(other, Number)
        return Matrix([
            [other * x for x in row] for row in self.__matrix
        ])

    def __add__(self, other):
        # and all(len(other) == len(row) for row in other)), "Wrong data"
        assert (isinstance(other, Sequence) and
                isinstance(other[0], Sequence) and
                len(self) == len(other) and
                len(self[0]) == len(other[0])), "Wrong data"
        return Matrix([
            [x + y for x, y in zip(r1, r2)] for r1, r2 in zip(self.__matrix, other)
        ])

    def __neg__(self):
        return Matrix([
            [-x for x in row] for row in self.__matrix
        ])

    def __sub__(self, other):
        assert (isinstance(other, Sequence) and
                isinstance(other[0], Sequence) and
                all(len(other) == len(row) for row in other)), "Wrong data"
        return Matrix([
            [x - y for x, y in zip(r1, r2)] for r1, r2 in zip(self, other)
        ])

    @property
    def shape(self):
        return len(self.__matrix), len(self.__matrix[0])


if __name__ == '__main__':
    m = Matrix([[1, 2, 1], [2, 3, 0]])
    a = Matrix([[1, 0, 0], [2, 1, 0], [1, 1, 0]])
    # print(m, m.shape)
    # print(a, a.shape)
    print(m * a)
