from math import sqrt


class Sphere:
    """
    Sphere has redius, canter and material
    """

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """
        chaecks if the ray intersects with the sphere
        :return distance to intersection or None if there is no intersection
        """

        sphereToRay = ray.origin - self.center

        # a =1
        b = 2 * ray.direction.dotProduct(sphereToRay)
        c = sphereToRay.dotProduct(sphereToRay) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None

    def normal(self,surfacePoint):
        return (surfacePoint-self.center).normalize()
