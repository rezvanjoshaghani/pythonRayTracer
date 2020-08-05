from color import Color


class Light:
    """Point light source of a specific color"""

    def __init__(self, position, color=Color.fromHEX("#FFFFFF")):
        self.position = position
        self.color = color
