from coolstuff.model import Model
from lab_2.camera2d import Camera2D
from util.events import *

from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_s


class Scene(Camera2D):
    def __init__(self, title: str = "Cool stuff", left: float = -2, right: float = 2, bottom: float = -2, top: float = 2,
                 width: int = 600, height: int = 600):
        super().__init__(title, left, right, bottom, top, width, height)

        self.model = Model('../data/coolstuff/vertices', '../data/coolstuff/edges')

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

        if keyboard_pressed_buttons[K_UP]:
            self.model.translate(0, 0.05)
        if keyboard_pressed_buttons[K_DOWN]:
            self.model.translate(0, -0.05)
        if keyboard_pressed_buttons[K_LEFT]:
            self.model.translate(-0.05, 0)
        if keyboard_pressed_buttons[K_RIGHT]:
            self.model.translate(0.05, 0)
        if keyboard_pressed_buttons[K_a]:
            self.model.rotate(0.05)
        if keyboard_pressed_buttons[K_s]:
            self.model.rotate(-0.05)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if is_quit_event(event):
                    pygame.quit()
                    quit()
                elif is_screen_resize_event(event):
                    self.set_width_height(event.size)
                    self.same_scale()
                # elif is_zoom_in_event(event):
                #     self.scale(11 / 10)
                # elif is_zoom_out_event(event):
                #     self.scale(10 / 11)

            self.input()
            self.clear_screen()
            self.draw_model()

            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == '__main__':
    Scene()
