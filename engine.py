from color import Color
from image import Image
from point import Point
from ray import Ray


class RenderEngine:
    """
    Render 3D object into 2D objects using ray tracing
    """

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspectRatio = float(width) / height
        x0 = -1.0
        x1 = 1.0
        xStep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspectRatio
        y1 = 1.0 / aspectRatio
        # y0 = -1.0
        # y1 = 1.0
        yStep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j * yStep
            for i in range(width):
                x = x0 + i * xStep
                ray = Ray(camera, Point(x, y) - camera)
                pixels.setPixel(i, j, self.rayTrace(ray, scene))
            print("{:3.0f}%".format(float(j)/float(height)*100),end="\r")
        return pixels

    def rayTrace(self, ray, scene):
        color = Color(0, 0, 0)
        distHit, objHit = self.findNearest(ray, scene)
        if objHit is None:
            return color
        hitPos = ray.origin + ray.direction * distHit
        hitNormal = objHit.normal(hitPos)
        color += self.colorAt(objHit, hitPos, hitNormal, scene)
        return color

    def findNearest(self, ray, scene):
        distMin = None
        objHit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (objHit is None or dist < distMin):
                distMin = dist
                objHit = obj
        return (distMin, objHit)

    def colorAt(self, objHit, hitPos, normal, scene):
        material = objHit.material
        objColor = material.colorAt(hitPos)
        toCam = scene.camera - hitPos
        specular_k= 50
        color = material.ambient * Color.fromHEX("#000000")
        # Light Calculations
        for light in scene.lights:
            toLight = Ray(hitPos, light.position - hitPos)
            # Diffuse shading (Lambert)
            color += objColor * material.diffuse * max(normal.dotProduct(toLight.direction), 0)
            # Specular Shading
            halfVector= (toLight.direction+toCam).normalize()
            color += light.color* material.specular * max(normal.dotProduct(halfVector),0) ** specular_k

        return color
