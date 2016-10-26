from typing import Callable

from OpenGL.GL import *
# from OpenGL.GLU import *
from math import pi, sinh, sin, cosh, cos

# Task number: 8


class Drawable:
    """
    W -- ширина области
    H -- высота
    phi_r -- правая граница для параметра \varphi эллиптической системы координат
    phi_l -- левая граница
    c -- коэффициент в эллиптической системе координат.
    """
    # noinspection PyShadowingNames
    def __init__(self, func: Callable[[float], float], width: int, height: int, phi_l: float, phi_r: float, c: float):
        self.R = +2
        self.B = -2
        self.T = +2
        self.L = -2

        self.H = height
        self.W = width

        self.phi_r = phi_r
        self.phi_l = phi_l
        self.c = c

        self.func = func

    def x_screen_to_world(self, x):
        return self.L + (self.R - self.L) * (x + .5) / self.W

    def y_screen_to_world(self, y):
        return self.T - (self.T - self.B) * (y + .5) / self.H

    def x_world_to_screen(self, x):
        return int((x - self.L) * self.W / (self.R - self.L))

    def y_world_to_screen(self, y):
        return int((self.T - y) * self.H / (self.T - self.B))

    def lrtbwh(self):
        return self.L, self.R, self.T, self.B, self.W, self.H

    def draw_axes(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_LINES)

        glVertex2f(self.x_world_to_screen(0), self.y_world_to_screen(self.B))
        glVertex2f(self.x_world_to_screen(0), self.y_world_to_screen(self.T))

        glVertex2f(self.x_world_to_screen(self.L), self.y_world_to_screen(0))
        glVertex2f(self.x_world_to_screen(self.R), self.y_world_to_screen(0))

        glEnd()

        # glVertex2f(self.x_world_to_screen(self.R), self.y_world_to_screen(self.T))
        # glVertex2f(self.x_world_to_screen(self.L), self.y_world_to_screen(self.B))

    def plot(self):
        number_of_points = self.W * 10
        h = (self.R - self.L) / number_of_points

        xs = [self.L + i * h for i in range(number_of_points)]
        points = [(self.x_world_to_screen(x), self.y_world_to_screen(self.func(x))) for x in xs]

        glBegin(GL_LINES)

        for p1, p2 in zip(points, points[1:]):
            glVertex2i(*p1)
            glVertex2i(*p2)

        glEnd()

        # for x in range(self.W):
        #     x = self.x_screen_to_world(x)
        #     glVertex2i(self.x_world_to_screen(x), self.y_world_to_screen(self.func(x)))
        #     glVertex2i(self.x_world_to_screen(x+1), self.y_world_to_screen(self.func(x+1)))

    def elliptical_plot(self):
        number_of_points = round(self.phi_r - self.phi_l) * 10
        h = (self.phi_r - self.phi_l) / number_of_points
        phis = [-2 * pi + i * h for i in range(number_of_points)]
        rs = [self.func(phi) for phi in phis]

        xs = [self.x_world_to_screen(self.c * cosh(r) * cos(phi)) for (r, phi) in zip(rs, phis)]
        ys = [self.y_world_to_screen(self.c * sinh(r) * sin(phi)) for (r, phi) in zip(rs, phis)]

        points = [(x, y) for x, y in zip(xs, ys)]

        glBegin(GL_LINES)

        for p1, p2 in zip(points, points[1:]):
            glVertex2i(*p1)
            glVertex2i(*p2)

        glEnd()

    def set_width_height(self, wh):
        self.W, self.H = wh

    def same_scale(self):
        L, R, T, B, W, H = self.lrtbwh()
        self.L = (L + R) / 2 - (T - B) / 2 * W / H
        self.R = (L + R) / 2 + (T - B) / 2 * W / H

    def rescale(self, pos, k):
        x = self.x_screen_to_world(pos[0])
        y = self.y_screen_to_world(pos[1])
        # print(x, y)
        L, R, T, B, W, H = self.lrtbwh()
        self.L = x - (x - L) / k
        self.R = x + (R - x) / k
        self.B = y - (y - B) / k
        self.T = y + (T - y) / k

    def move(self, dx, dy):
        L, R, T, B, W, H = self.lrtbwh()
        dxw = dx * (R - L) / W
        dyw = dy * (T - B) / H
        self.R -= dxw
        self.L -= dxw
        self.T += dyw
        self.B += dyw
