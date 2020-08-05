from engine import RenderEngine
from image import Image
from color import Color
from light import Light
from material import Material
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector


def main():
    WIDTH = 800
    HEIGHT = 400
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.5, Material(Color.fromHEX("#FF0000"))),Sphere(Point(1, 0, 0), 0.5, Material(Color(0,1,0))),Sphere(Point(-1, 0, 0), 0.5, Material(Color(0,0,1)))]
    lights=[Light(Point(10,5,-10.0),Color.fromHEX("#FFFFFF"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("test.ppm", "w") as img_file:
        image.writePPM(img_file)


if __name__ == "__main__":
    main()
