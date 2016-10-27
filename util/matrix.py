from typing import Sequence

from tabulate import tabulate


class Matrix:
    def __init__(self, matrix: Sequence[Sequence[float]]):
        assert (isinstance(matrix, Sequence) and
                isinstance(matrix, Sequence) and
                all(len(matrix) == len(row) for row in matrix)), "Wrong data"
        self.__matrix = [[float(x) for x in row] for row in matrix]

    @staticmethod
    def one(size: int):
        return [
            [1 if i == j else 0 for j in range(size)] for i in range(size)
        ]

    @staticmethod
    def zero(size):
        return [[0] * size for _ in range(size)]

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
        if isinstance(other[0], Sequence):
            assert all(len(other) == len(row) for row in other), "Each row should have same length"
            return Matrix([
                [
                    sum(self[i][k] * other[k][j] for k in range(len(self))) for j in range(len(self))
                ] for i in range(len(self))
            ])
        else:
            return [
                sum(x * y for x, y in zip(row, other)) for row in self
            ]

    def __add__(self, other):
        assert (isinstance(other, Sequence) and
                isinstance(other[0], Sequence) and
                all(len(other) == len(row) for row in other)), "Wrong data"
        return Matrix([
            [x + y for x, y in zip(r1, r2)] for r1, r2 in zip(self, other)
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


if __name__ == '__main__':
    m = Matrix([[1, 2], [2, 3]])
    print(m * [1, 1])
