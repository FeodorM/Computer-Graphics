from util.matrix import Matrix
from math import cos, sin


def translation(x, y, z):
    return Matrix([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

#         den = (phi ** 2 + psi ** 2) ** .5
#         phi /= den
#         psi /= den
#         return Matrix([
#             [phi, -psi, 0],
#             [psi, phi,  0],
#             [0,   0,    1]
#         ])


def rotation_x(phi):
    c = cos(phi)
    s = sin(phi)
    return Matrix([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ])


def rotation_y(phi):
    c = cos(phi)
    s = sin(phi)
    return Matrix([
        [c,  0, s, 0],
        [0,  1, 0, 0],
        [-s, 0, c, 0],
        [0,  0, 0, 1]
    ])


def rotation_z(phi):
    c = cos(phi)
    s = sin(phi)
    return Matrix([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])


def scaling(kx, ky=None, kz=None):
    if ky is None and kz is None:
        ky = kz = kx
    return Matrix([
        [kx, 0,  0, 0],
        [0, ky,  0, 0],
        [0,  0, kz, 0],
        [0,  0,  0, 1]
    ])


mirroring_x = Matrix([
    [1,  0,  0, 0],
    [0, -1,  0, 0],
    [0,  0, -1, 0],
    [0,  0,  0, 1]
])

mirroring_y = Matrix([
    [-1, 0,  0, 0],
    [0,  1,  0, 0],
    [0,  0, -1, 0],
    [0,  0,  0, 1]
])

mirroring_z = Matrix([
    [-1,  0, 0, 0],
    [0,  -1, 0, 0],
    [0,   0, 1, 0],
    [0,   0, 0, 1]
])
