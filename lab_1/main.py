# Task number: 8
import math
from OpenGL.GL import glMatrixMode, glLoadIdentity, glViewport, GL_PROJECTION
from OpenGL.GLU import gluOrtho2D
from lab_1.drawable import Drawable
from util.events import *


class Main:
    def __init__(self):
        self.W = 600
        self.H = 600
        self.elliptical = False
        self.drawable = Drawable(lambda x: .3 * math.sin(5 * x) + 2, self.W, self.H, - 2 * math.pi, 2 * math.pi, c=2)

        pygame.init()
        pygame.display.set_mode((self.W, self.H), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption("Lab 1")

        self.resize()

        self.mainloop()

    @staticmethod
    def change_plot_type_event(event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE

    def resize(self):
        pygame.display.set_mode((self.W, self.H), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.W, self.H, 0)
        glViewport(0, 0, self.W, self.H)
        # gluOrtho2D(self.L * (self.W / self.H), self.R * (self.W / self.H), self.B, self.T)
        # gluOrtho2D(self.L, self.R, self.B, self.T)
        pygame.display.flip()

    def input(self):
        mouse_pressed_buttons = pygame.mouse.get_pressed()  # mouse pressed buttons
        # kpb = pygame.key.get_pressed()  # keyboard pressed buttons
        mouse_shift = pygame.mouse.get_rel()  # mouse shift

        # If left mouse button pressed, move plot
        if mouse_pressed_buttons[0]:
            self.drawable.move(mouse_shift[0], mouse_shift[1])

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if is_quit_event(event):
                    pygame.quit()
                    quit()
                elif event.type == pygame.VIDEORESIZE:
                    self.W, self.H = event.size
                    self.resize()
                    self.drawable.set_width_height(event.size)
                    self.drawable.same_scale()
                elif is_zoom_in_event(event):
                    self.drawable.rescale(pygame.mouse.get_pos(), 11 / 10)
                elif is_zoom_out_event(event):
                    self.drawable.rescale(pygame.mouse.get_pos(), 10 / 11)
                elif self.change_plot_type_event(event):
                        self.elliptical = not self.elliptical
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     # right button pressed
                #     if event.button == 3:
                #         self.drawable.same_scale()
                #     # left button pressed
                #     elif event.button == 1:
                #         x, y = pygame.mouse.get_pos()
                #         print(x, y)
                #         print(self.drawable.x_screen_to_world(x), self.drawable.y_screen_to_world(y))
                #         print()

            self.input()
            self.drawable.draw_axes()

            if self.elliptical:
                self.drawable.elliptical_plot()
            else:
                self.drawable.plot()

            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == '__main__':
    Main()
