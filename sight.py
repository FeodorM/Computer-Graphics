from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


class Main:
    top     = 0
    left    = 0
    right   = 800
    bottom  = 600

    speed = 3

    def __init__(self):
        self.x = self.right // 2
        self.y = self.bottom // 2
        self.r = 20

        self.quadratic = gluNewQuadric()

        pygame.init()
        pygame.display.set_mode((self.right, self.bottom), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption("My Title")

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(self.top, self.right, self.bottom, self.left)

        self.mainloop()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glTranslatef(self.x, self.y, 0.0)
        self.x = self.y = 0

        # Draw circle
        gluDisk(self.quadratic, self.r - 1, self.r + 1, 100, 32)

        # Draw lines
        glBegin(GL_LINES)

        glVertex2f(0, -self.r)
        glVertex2f(0,  self.r)

        glVertex2f(-self.r, 0)
        glVertex2f( self.r, 0)

        glEnd()

        # glVertex2f(self.x, self.y - self.r)
        # glVertex2f(self.x, self.y + self.r)
        #
        # glVertex2f(self.x - self.r, self.y)
        # glVertex2f(self.x + self.r, self.y)
        # glBegin(GL_LINES)
        #
        #
        # if self.first_diagonal:
        #     glVertex2f(self.left, self.top)
        #     glVertex2f(self.right, self.bottom)
        #
        # if self.second_diagonal:
        #     glVertex2f(self.right, self.top)
        #     glVertex2f(self.left, self.bottom)
        #
        # glEnd()

    def input(self):
        mpb = pygame.mouse.get_pressed()  # mouse pressed buttons
        kpb = pygame.key.get_pressed()  # keyboard pressed buttons
        msh = pygame.mouse.get_rel()  # mouse shift

        # If left mouse button pressed
        if mpb[0]:
            self.x += msh[0]
            self.y += msh[1]

        # If arrows pressed
        if kpb[pygame.K_UP]:
            self.y -= self.speed
        if kpb[pygame.K_DOWN]:
            self.y += self.speed

        if kpb[pygame.K_RIGHT]:
            self.x += self.speed
        if kpb[pygame.K_LEFT]:
            self.x -= self.speed

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            self.input()
            self.draw()

            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == '__main__':
    Main()
