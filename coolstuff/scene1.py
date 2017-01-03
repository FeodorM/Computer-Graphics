from coolstuff.model1 import Model1
from coolstuff.base_scene import BaseScene
from util.events import *
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_s, K_SPACE


class Scene1(BaseScene):
    def _init(self):
        self.model = Model1('../data/coolstuff/vertices', '../data/coolstuff/edges')
        self.speed = .03

    def event_handler(self, event):
        if is_zoom_in_event(event):
            self.model.scale(11 / 10)
        elif is_zoom_out_event(event):
            self.model.scale(10 / 11)
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            self.model.mirror_x()

    def input(self):
        mouse_pressed_buttons = pygame.mouse.get_pressed()
        keyboard_pressed_buttons = pygame.key.get_pressed()
        mouse_shift = pygame.mouse.get_rel()

        if keyboard_pressed_buttons[K_UP]:
            self.model.translate(0, self.speed)
        if keyboard_pressed_buttons[K_DOWN]:
            self.model.translate(0, -self.speed)
        if keyboard_pressed_buttons[K_LEFT]:
            self.model.translate(-self.speed, 0)
        if keyboard_pressed_buttons[K_RIGHT]:
            self.model.translate(self.speed, 0)
        if keyboard_pressed_buttons[K_a]:
            self.model.rotate(self.speed)
        if keyboard_pressed_buttons[K_s]:
            self.model.rotate(-self.speed)

        if mouse_pressed_buttons[0]:
            self.model.translate(0.007 * mouse_shift[0], -0.007 * mouse_shift[1])


if __name__ == '__main__':
    Scene1()
