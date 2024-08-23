import math


class Point:
    def __init__(self, x, y, data=None):
        self.x = x
        self.y = y
        self.data = data

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.data})'

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def translate(self, x, y):
        # This function translates the point into vector
        return Point(self.x + x, self.y + y, self.data)

    def rotate(self, angle, origin=None):
        if origin is None:
            origin = Point(0, 0)

            # Translate the point back to the origin
        temp_x = self.x - origin.x
        temp_y = self.y - origin.y

        # Rotate the point
        rotated_x = temp_x * math.cos(angle) - temp_y * math.sin(angle)
        rotated_y = temp_x * math.sin(angle) + temp_y * math.cos(angle)

        # Translate the point back
        return Point(rotated_x + origin.x, rotated_y + origin.y, self.data)

    def is_bounded_by(self, x_min, x_max, y_min, y_max):
        return x_min <= self.x <= x_max and y_min <= self.y <= y_max
