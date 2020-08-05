class Ray:
    """
    ray is a half line with origin and direction
    """

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
