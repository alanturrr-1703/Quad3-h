class Boundary:
    def __init__(self, x_center: float, y_center: float, half_width: float, half_height: float):
        """
        Initialize the boundary as a rectangle or square.
        """
        self.x_center = x_center
        self.y_center = y_center
        self.half_width = half_width
        self.half_height = half_height

    def contains_point(self, point: Point) -> bool:
        """
        Check if the boundary contains a given point.
        """
        return (self.x_center - self.half_width <= point.x <= self.x_center + self.half_width and
                self.y_center - self.half_height <= point.y <= self.y_center + self.half_height)

    def intersects(self, other: 'Boundary') -> bool:
        """
        Check if this boundary intersects with another boundary.
        """
        return not (other.x_center - other.half_width > self.x_center + self.half_width or
                    other.x_center + other.half_width < self.x_center - self.half_width or
                    other.y_center - other.half_height > self.y_center + self.half_height or
                    other.y_center + other.half_height < self.y_center - self.half_height)

    def overlap_percentage(self, other: 'Boundary') -> float:
        """
        Calculate the percentage of overlap between two boundaries.
        Useful for determining the degree of intersection.
        """
        dx = min(self.x_center + self.half_width, other.x_center + other.half_width) - max(self.x_center - self.half_width, other.x_center - other.half_width)
        dy = min(self.y_center + self.half_height, other.y_center + other.half_height) - max(self.y_center - self.half_height, other.y_center - other.half_height)

        if dx < 0 or dy < 0:
            return 0.0  # No overlap
        overlap_area = dx * dy
        this_area = 2 * self.half_width * 2 * self.half_height
        return overlap_area / this_area * 100  # Percentage of overlap

    def expand(self, factor: float) -> None:
        """
        Expand the boundary by a given factor. This is useful for extending query ranges.
        """
        self.half_width *= factor
        self.half_height *= factor

    def shrink(self, factor: float) -> None:
        """
        Shrink the boundary by a given factor. Useful for tighter bounding boxes.
        """
        self.half_width /= factor
        self.half_height /= factor

    def to_latlng(self, scale_factor: float = 1.0) -> dict:
        """
        Convert this boundary from a cartesian system to a latitude/longitude system.
        """
        return {
            "lat_min": self.y_center - self.half_height * scale_factor,
            "lat_max": self.y_center + self.half_height * scale_factor,
            "lng_min": self.x_center - self.half_width * scale_factor,
            "lng_max": self.x_center + self.half_width * scale_factor
        }

    def __repr__(self):
        return f"Boundary(center=({self.x_center}, {self.y_center}), half_width={self.half_width}, half_height={self.half_height})"
