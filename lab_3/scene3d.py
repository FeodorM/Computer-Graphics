import pygame
from pygame.locals import *

from lab_3.camera3d import Camera3D
from lab_3.model3d import Model3D
from util.events import is_quit_event
from lab_3.affine_transform import *


class Scene3D(Camera3D):
    def __init__(self, *args, **kwargs):
        super(Scene3D, self).__init__(*args, *kwargs)

        self.model = Model3D(
            '../data/3/vertices',
            '../data/3/verges',
            '../data/3/invisible_edges',
            self.world_to_project
        )

        print('started.')
        self.mainloop()

    def draw_model(self):
        for edge in self.model.edges:
            x0, y0 = self.model[edge[0]]
            x1, y1 = self.model[edge[1]]
            self.draw_line(x0, y0, x1, y1)

    def input(self):
        mouse_pressed_buttons = pygame.mouse.get_pressed()
        keyboard_pressed_buttons = pygame.key.get_pressed()
        mouse_shift = pygame.mouse.get_rel()

        if mouse_pressed_buttons[0]:
            self.model.apply(rotation_y(mouse_shift[0] / 500), self.world_to_project)
            self.model.apply(rotation_x(mouse_shift[1] / 500), self.world_to_project)

        if keyboard_pressed_buttons[K_LEFT]:
            self.model.apply(translation(-.01, 0, 0), self.world_to_project)
        if keyboard_pressed_buttons[K_RIGHT]:
            self.model.apply(translation(.01, 0, 0), self.world_to_project)
        if keyboard_pressed_buttons[K_UP]:
            self.model.apply(translation(0, 0.01, 0), self.world_to_project)
        if keyboard_pressed_buttons[K_DOWN]:
            self.model.apply(translation(0, -0.01, 0), self.world_to_project)
        if keyboard_pressed_buttons[K_KP_PLUS]:
            # self.model.apply(translation(0, 0, 0.05), self.world_to_project)
            self.set_distance(self.D + .6)
            self.model.calc_project_vertices(self.world_to_project)
        if keyboard_pressed_buttons[K_KP_MINUS]:
            # self.model.apply(translation(0, 0, -0.05), self.world_to_project)
            self.set_distance(self.D - .6)
            self.model.calc_project_vertices(self.world_to_project)
        if keyboard_pressed_buttons[K_x]:
            x, y, z = self.model.center
            self.model.apply(translation(x, y, z) * rotation_x(.01) * translation(-x, -y, -z), self.world_to_project)
        if keyboard_pressed_buttons[K_y]:
            x, y, z = self.model.center
            self.model.apply(translation(x, y, z) * rotation_y(.01) * translation(-x, -y, -z), self.world_to_project)
        if keyboard_pressed_buttons[K_z]:
            x, y, z = self.model.center
            self.model.apply(translation(x, y, z) * rotation_z(.01) * translation(-x, -y, -z), self.world_to_project)
        # if keyboard_pressed_buttons[K_SPACE]:
        #     x, y, z = self.model.center
        #     self.model.apply(translation(-x, -y, -z), self.world_to_project)

            # If left mouse button pressed, move plot
            # if mouse_pressed_buttons[0]:
            #     self.model.apply(translation(self._x_screen_to_world(mouse_shift[0]), -self._y_screen_to_world(mouse_shift[1])))

    # def scale(self, k):
    #     x, y = pygame.mouse.get_pos()
    #     x = self._x_screen_to_world(x)
    #     y = self._y_screen_to_world(y)
    #     self.model.apply(translation(x, y) * scaling(k) * translation(-x, -y))

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if is_quit_event(event):
                    pygame.quit()
                    quit()
                elif event.type == VIDEORESIZE:
                    self.set_width_height(event.size)
                    self.same_scale()
                    # elif event.type == KEYDOWN and event.key == K_SPACE:
                    #     self.model.apply(translation(.1, .1))
                    # elif event.type == KEYDOWN and event.key == K_KP_PLUS:
                    #     self.model.apply(scaling(11 / 10))
                    # elif event.type == KEYDOWN and event.key == K_KP_MINUS:
                    #     self.model.apply(scaling(10 / 11))
                    # elif is_zoom_in_event(event):
                    #     self.scale(11 / 10)
                    # elif is_zoom_out_event(event):
                    #     self.scale(10 / 11)

            self.input()

            self.clear_screen()
            # self.draw_axes()
            self.draw_model()

            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == '__main__':
    Scene3D()
