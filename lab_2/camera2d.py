from OpenGL.GL import *
from OpenGL.GL import glMatrixMode, glLoadIdentity, glViewport, GL_PROJECTION
from OpenGL.GLU import gluOrtho2D
import pygame


class Camera2D:
    """
    W -- ширина области
    H -- высота
    # phi_r -- правая граница для параметра \varphi эллиптической системы координат
    # phi_l -- левая граница
    # c -- коэффициент в эллиптической системе координат.
    """
    # noinspection PyShadowingNames
    def __init__(self, title: str = "Lab 2", left: float = -2, right: float = 2, bottom: float = -2, top: float = 2,
                 width: int = 600, height: int = 600):
        self.R = right
        self.B = bottom
        self.T = top
        self.L = left

        self.H = height
        self.W = width

        pygame.init()
        pygame.display.set_mode((self.W, self.H), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption(title)

        self.resize_window()

    def resize_window(self):
        pygame.display.set_mode((self.W, self.H), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.W, self.H, 0)
        glViewport(0, 0, self.W, self.H)
        # gluOrtho2D(self.L * (self.W / self.H), self.R * (self.W / self.H), self.B, self.T)
        # gluOrtho2D(self.L, self.R, self.B, self.T)
        pygame.display.flip()

    def _x_screen_to_world(self, x):
        return self.L + (self.R - self.L) * (x + .5) / self.W

    def _y_screen_to_world(self, y):
        return self.T - (self.T - self.B) * (y + .5) / self.H

    def _x_world_to_screen(self, x):
        return int((x - self.L) * self.W / (self.R - self.L))

    def _y_world_to_screen(self, y):
        return int((self.T - y) * self.H / (self.T - self.B))

    def lrtbwh(self):
        return self.L, self.R, self.T, self.B, self.W, self.H

    # noinspection PyMethodMayBeStatic
    def clear_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def draw_axes(self):
        glBegin(GL_LINES)

        glVertex2f(self._x_world_to_screen(0), self._y_world_to_screen(self.B))
        glVertex2f(self._x_world_to_screen(0), self._y_world_to_screen(self.T))

        glVertex2f(self._x_world_to_screen(self.L), self._y_world_to_screen(0))
        glVertex2f(self._x_world_to_screen(self.R), self._y_world_to_screen(0))

        glEnd()

        # glVertex2f(self.x_world_to_screen(self.R), self.y_world_to_screen(self.T))
        # glVertex2f(self.x_world_to_screen(self.L), self.y_world_to_screen(self.B))

    def draw_line(self, x0, y0, x1, y1):
        glBegin(GL_LINES)

        glVertex2f(self._x_world_to_screen(x0), self._y_world_to_screen(y0))
        glVertex2f(self._x_world_to_screen(x1), self._y_world_to_screen(y1))

        glEnd()

    def set_width_height(self, wh):
        self.W, self.H = wh
        self.resize_window()

    def same_scale(self):
        L, R, T, B, W, H = self.lrtbwh()
        self.L = (L + R) / 2 - (T - B) / 2 * W / H
        self.R = (L + R) / 2 + (T - B) / 2 * W / H

    # def plot(self):
    #     number_of_points = self.W * 10
    #     h = (self.R - self.L) / number_of_points
    #
    #     xs = [self.L + i * h for i in range(number_of_points)]
    #     points = [(self.x_world_to_screen(x), self.y_world_to_screen(self.func(x))) for x in xs]
    #
    #     glBegin(GL_LINES)
    #
    #     for p1, p2 in zip(points, points[1:]):
    #         glVertex2i(*p1)
    #         glVertex2i(*p2)
    #
    #     glEnd()
    #
    #     # for x in range(self.W):
    #     #     x = self.x_screen_to_world(x)
    #     #     glVertex2i(self.x_world_to_screen(x), self.y_world_to_screen(self.func(x)))
    #     #     glVertex2i(self.x_world_to_screen(x+1), self.y_world_to_screen(self.func(x+1)))
    #
    # def elliptical_plot(self):
    #     number_of_points = round(self.phi_r - self.phi_l) * 10
    #     h = (self.phi_r - self.phi_l) / number_of_points
    #     phis = [-2 * pi + i * h for i in range(number_of_points)]
    #     rs = [self.func(phi) for phi in phis]
    #
    #     xs = [self.x_world_to_screen(self.c * cosh(r) * cos(phi)) for (r, phi) in zip(rs, phis)]
    #     ys = [self.y_world_to_screen(self.c * sinh(r) * sin(phi)) for (r, phi) in zip(rs, phis)]
    #
    #     points = [(x, y) for x, y in zip(xs, ys)]
    #
    #     glBegin(GL_LINES)
    #
    #     for p1, p2 in zip(points, points[1:]):
    #         glVertex2i(*p1)
    #         glVertex2i(*p2)
    #
    #     glEnd()
    #
    # def rescale(self, pos, k):
    #     x = self.x_screen_to_world(pos[0])
    #     y = self.y_screen_to_world(pos[1])
    #     # print(x, y)
    #     L, R, T, B, W, H = self.lrtbwh()
    #     self.L = x - (x - L) / k
    #     self.R = x + (R - x) / k
    #     self.B = y - (y - B) / k
    #     self.T = y + (T - y) / k
    #
    # def move(self, dx, dy):
    #     L, R, T, B, W, H = self.lrtbwh()
    #     dxw = dx * (R - L) / W
    #     dyw = dy * (T - B) / H
    #     self.R -= dxw
    #     self.L -= dxw
    #     self.T += dyw
    #     self.B += dyw
