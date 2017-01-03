from math import cos, sin
from pygame import K_UP, K_DOWN

from coolstuff.base_scene import BaseScene
from coolstuff.moving_model import MovingModel
from util.events import *


class Scene2(BaseScene):
    def _init(self):
        self.model = MovingModel(lambda t: t * cos(t), lambda t: t * sin(t),
                                 lambda t: cos(t) - t * sin(t), lambda t: sin(t) + t * cos(t),
                                 '../data/coolstuff/vertices', '../data/coolstuff/edges')

    def event_handler(self, event):
        pass

    def input(self):
        keyboard_pressed_buttons = pygame.key.get_pressed()

        if keyboard_pressed_buttons[K_UP]:
            self.model.inc()
        if keyboard_pressed_buttons[K_DOWN]:
            self.model.dec()


if __name__ == '__main__':
    Scene2()
