class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def setPixel(self, x, y, col):
        self.pixels[y][x] = col

    def writePPM(self, imgFile):

        def to_byte(c):
            # round in case of floating point
            # we chop off the numbers above 255 and below 0
            return round(max(min(c * 255, 255), 0))

        imgFile.write("P3 {} {} \n255\n".format(self.width,self.height))
        for row in self.pixels:
            for color in row:
                imgFile.write("{} {} {} ".format(to_byte(color.x), to_byte(color.y), to_byte(color.z)))
            imgFile.write("\n")