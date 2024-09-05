import math


class Point:
    def __init__(self, x: float, y: float, data=None):
        """
        Initialize a point with x, y coordinates and optional data.
        """
        self.x = x
        self.y = y
        self.data = data

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, data={self.data})"

    def distance(self, other: 'Point') -> float:
        """
        Compute the Euclidean distance between this point and another point.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def midpoint(self, other: 'Point') -> 'Point':
        """
        Compute the midpoint between this point and another point.
        """
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def translate(self, dx: float, dy: float) -> 'Point':
        """
        Translate this point by a vector (dx, dy).
        """
        return Point(self.x + dx, self.y + dy, self.data)

    def rotate(self, angle: float, origin: 'Point' = None) -> 'Point':
        """
        Rotate this point around a given origin by the specified angle (in radians).
        If no origin is provided, it rotates around the origin (0,0).
        """
        if origin is None:
            origin = Point(0, 0)

        # Translate point back to the origin
        temp_x = self.x - origin.x
        temp_y = self.y - origin.y

        # Rotate point
        rotated_x = temp_x * math.cos(angle) - temp_y * math.sin(angle)
        rotated_y = temp_x * math.sin(angle) + temp_y * math.cos(angle)

        # Translate point back
        return Point(rotated_x + origin.x, rotated_y + origin.y, self.data)

    def is_bounded_by(self, x_min: float, x_max: float, y_min: float, y_max: float) -> bool:
        """
        Check if the point is within the specified bounding box.
        """
        return x_min <= self.x <= x_max and y_min <= self.y <= y_max

    def reflect_across_x_axis(self) -> 'Point':
        """
        Reflect the point across the x-axis (invert y-coordinate).
        """
        return Point(self.x, -self.y, self.data)

    def reflect_across_y_axis(self) -> 'Point':
        """
        Reflect the point across the y-axis (invert x-coordinate).
        """
        return Point(-self.x, self.y, self.data)

    def scale(self, factor_x: float, factor_y: float = None) -> 'Point':
        """
        Scale the point by a factor for x and y axes. If only factor_x is provided, scale uniformly.
        """
        if factor_y is None:
            factor_y = factor_x
        return Point(self.x * factor_x, self.y * factor_y, self.data)

    def to_dict(self) -> dict:
        """
        Convert the point data to a dictionary format, useful for serialization.
        """
        return {"x": self.x, "y": self.y, "data": self.data}

    @classmethod
    def from_dict(cls, data: dict) -> 'Point':
        """
        Create a Point instance from a dictionary.
        """
        return cls(data["x"], data["y"], data.get("data"))

    def manhattan_distance(self, other: 'Point') -> float:
        """
        Compute the Manhattan distance between this point and another point.
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def equals(self, other: 'Point') -> bool:
        """
        Check if two points are equal in terms of coordinates.
        """
        return self.x == other.x and self.y == other.y

    def quadrant(self) -> int:
        """
        Determine the quadrant in which the point lies.
        1: First Quadrant (x > 0, y > 0)
        2: Second Quadrant (x < 0, y > 0)
        3: Third Quadrant (x < 0, y < 0)
        4: Fourth Quadrant (x > 0, y < 0)
        """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 < self.y:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 > self.y:
            return 4
        return 0  # Origin or on an axis

    def bearing_to(self, other: 'Point') -> float:
        """
        Calculate the bearing from this point to another point, in radians.
        """
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.atan2(delta_y, delta_x)

    def as_tuple(self) -> tuple:
        """
        Return the point coordinates as a tuple (x, y).
        """
        return self.x, self.y
