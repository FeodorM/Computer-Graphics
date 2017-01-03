from lab_2.camera2d import Camera2D
from util.events import *


class BaseScene(Camera2D):
    def __init__(self, title: str = "Cool stuff", left: float = -2, right: float = 2, bottom: float = -2,
                 top: float = 2, width: int = 600, height: int = 600):
        super().__init__(title, left, right, bottom, top, width, height)
        self.model = None
        self._init()
        self.mainloop()

    def _init(self):
        """Implement it in subclass. Create model in this method"""
        raise NotImplementedError()

    def draw_model(self):
        for edge in self.model.edges:
            x0, y0 = self.model[edge[0]]
            x1, y1 = self.model[edge[1]]
            self.draw_line(x0, y0, x1, y1)

    def input(self):
        raise NotImplementedError()

    def event_handler(self, event):
        raise NotImplementedError()

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if is_quit_event(event):
                    pygame.quit()
                    quit()
                elif is_screen_resize_event(event):
                    self.set_width_height(event.size)
                    self.same_scale()
                else:
                    self.event_handler(event)

            self.input()
            self.clear_screen()
            self.draw_model()

            pygame.display.flip()
            pygame.time.wait(10)
