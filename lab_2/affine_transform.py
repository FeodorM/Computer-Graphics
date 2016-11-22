from util.matrix import Matrix
from math import cos, sin


def translation(x, y):
    return Matrix([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1]
    ])


def rotation(phi, psi=None):
    if psi is None:
        c = cos(phi)
        s = sin(phi)
        return Matrix([
            [c, -s, 0],
            [s,  c, 0],
            [0,  0, 1]
        ])
    else:
        Matrix([
            [phi, -psi, 0],
            [psi, phi,  0],
            [0,   0,    1]
        ])


def scaling(kx, ky):
    return Matrix([
        [kx, 0, 0],
        [0, ky, 0],
        [0,  0, 1]
    ])


mirroring_x = Matrix([
    [1,  0, 0],
    [0, -1, 0],
    [0,  0, 1]
])

mirroring_y = Matrix([
    [-1, 0, 0],
    [0,  1, 0],
    [0,  0, 1]
])

mirroring = Matrix([
    [-1,  0, 0],
    [0,  -1, 0],
    [0,   0, 1]
])

T = translation
R = rotation
S = scaling
Mx = mirroring_x
My = mirroring_y
M0 = mirroring

