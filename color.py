from vector import Vector

class Color(Vector):
    """
    Store color as RGB. Uses Vector.
    """
    @classmethod
    def fromHEX(cls,hexColor="#000000"):
        x = int(hexColor[1:3],16) / 255
        y = int(hexColor[3:5], 16) / 255
        z = int(hexColor[5:7], 16) / 255
        return cls(x,y,z)


