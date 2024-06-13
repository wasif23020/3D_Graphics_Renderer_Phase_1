from object_3d import *
from camera import *
from projection import *
import pygame as pyg


class Render:
    def __init__(self):
        pyg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1550, 800
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pyg.display.set_mode(self.RES)
        self.clock = pyg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pyg.Color('grey'))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pyg.event.get() if i.type == pyg.QUIT]
            pyg.display.set_caption(str(self.clock.get_fps()))
            pyg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = Render()
    app.run()