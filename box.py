class Coordinate:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Rectangle:
    def __init__(self, initial, width, length):
        self.first = initial
        self.second = Coordinate(initial.x + length, initial.y, initial.z)
        self.third = Coordinate(initial.x, initial.y + width, initial.z)
        self.fourth = Coordinate(initial.x + length, initial.y + width, initial.z)

class Box:
    def __init__(self, bottom_left_corner, width, length, height):
        self.width = width
        self.length = length
        self.height = height

        top_left_corner = Coordinate(bottom_left_corner.x, bottom_left_corner.y, bottom_left_corner.z + self.height)
        self.bottom = Rectangle(bottom_left_corner, self.width, self.length)
        self.top = Rectangle(top_left_corner, self.width, self.length)
