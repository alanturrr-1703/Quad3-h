class Node:
    def __init__(self, boundary: Boundary, capacity: int):
        """
        Initialize a Node with a given boundary and capacity.
        """
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

        # Child nodes
        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None

    def subdivide(self):
        """
        Subdivide the node into four quadrants. Each new quadrant will have its own boundary.
        """
        x = self.boundary.x_center
        y = self.boundary.y_center
        half_width = self.boundary.half_width / 2
        half_height = self.boundary.half_height / 2

        # Create four child boundaries
        nw_boundary = Boundary(x - half_width, y - half_height, half_width, half_height)
        ne_boundary = Boundary(x + half_width, y - half_height, half_width, half_height)
        sw_boundary = Boundary(x - half_width, y + half_height, half_width, half_height)
        se_boundary = Boundary(x + half_width, y + half_height, half_width, half_height)

        # Create the child nodes
        self.northwest = Node(nw_boundary, self.capacity)
        self.northeast = Node(ne_boundary, self.capacity)
        self.southwest = Node(sw_boundary, self.capacity)
        self.southeast = Node(se_boundary, self.capacity)

        self.divided = True

    def insert(self, point: Point) -> bool:
        """
        Insert a point into the node. If the node's capacity is exceeded, subdivide and insert into the appropriate child node.
        """
        if not self.boundary.contains_point(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            return (self.northwest.insert(point) or
                    self.northeast.insert(point) or
                    self.southwest.insert(point) or
                    self.southeast.insert(point))

    def remove(self, point: Point) -> bool:
        """
        Remove a point from the node. If the point is found, it's removed.
        """
        if point in self.points:
            self.points.remove(point)
            return True

        if self.divided:
            return (self.northwest.remove(point) or
                    self.northeast.remove(point) or
                    self.southwest.remove(point) or
                    self.southeast.remove(point))
        return False

    def merge(self):
        """
        Merge the node if the children are empty. Useful for balancing the tree.
        """
        if self.divided and not (self.northwest.points or self.northeast.points or self.southwest.points or self.southeast.points):
            self.northwest = self.northeast = self.southwest = self.southeast = None
            self.divided = False

    def count_points(self) -> int:
        """
        Count all the points contained in this node and its children.
        """
        count = len(self.points)
        if self.divided:
            count += self.northwest.count_points()
            count += self.northeast.count_points()
            count += self.southwest.count_points()
            count += self.southeast.count_points()
        return count

    def query(self, range_boundary: Boundary, found_points: list = None) -> list:
        """
        Query the node for all points within a given range.
        """
        if found_points is None:
            found_points = []

        if not self.boundary.intersects(range_boundary):
            return found_points

        for point in self.points:
            if range_boundary.contains_point(point):
                found_points.append(point)

        if self.divided:
            self.northwest.query(range_boundary, found_points)
            self.northeast.query(range_boundary, found_points)
            self.southwest.query(range_boundary, found_points)
            self.southeast.query(range_boundary, found_points)

        return found_points

    def nearest_neighbor(self, target_point: Point, best_point: Point = None, best_distance: float = float('inf')) -> tuple:
        """
        Find the nearest neighbor of a target point using a recursive search.
        Returns the closest point and the distance to it.
        """
        for point in self.points:
            dist = point.distance(target_point)
            if dist < best_distance:
                best_point = point
                best_distance = dist

        if self.divided:
            for child in [self.northwest, self.northeast, self.southwest, self.southeast]:
                if child.boundary.contains_point(target_point) or child.boundary.intersects(self.boundary):
                    best_point, best_distance = child.nearest_neighbor(target_point, best_point, best_distance)

        return best_point, best_distance

    def __repr__(self):
        return f"Node(boundary={self.boundary}, points={self.points}, divided={self.divided})"
