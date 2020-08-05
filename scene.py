class Scene:
    """
    All information for the raytrace3r engine
    """

    def __init__(self, camera, objects,lights, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
        self.lights = lights

