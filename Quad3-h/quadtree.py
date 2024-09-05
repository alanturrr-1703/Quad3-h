from boundary import Boundary
from node import Node
from point import Point


class QuadTree:
    def __init__(self, boundary: Boundary, capacity: int):
        """
        Initialize the QuadTree with a root node boundary and a point capacity per node.
        """
        self.root = Node(boundary, capacity)

    def insert(self, point: Point) -> bool:
        """
        Insert a point into the quadtree.
        """
        return self.root.insert(point)

    def remove(self, point: Point) -> bool:
        """
        Remove a point from the quadtree.
        """
        return self.root.remove(point)

    def query(self, range_boundary: Boundary) -> list:
        """
        Query the quadtree for all points within a given range.
        """
        return self.root.query(range_boundary)

    def nearest_neighbor(self, point: Point) -> Point:
        """
        Find the nearest neighbor of a given point in the quadtree.
        """
        return self.root.nearest_neighbor(point)[0]

    def rebalance(self):
        """
        Rebalance the tree by merging and re-subdividing nodes if necessary.
        """
        self.root.merge()

    def export_to_geojson(self) -> dict:
        """
        Export the quadtree to a GeoJSON format for use with mapping applications.
        """
        geojson = {
            "type": "FeatureCollection",
            "features": []
        }
        self._add_node_to_geojson(self.root, geojson["features"])
        return geojson

    def _add_node_to_geojson(self, node: Node, features: list):
        """
        Recursively add nodes and points to the GeoJSON structure.
        """
        for point in node.points:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [point.x, point.y]
                },
                "properties": {
                    "data": point.data
                }
            })
        if node.divided:
            self._add_node_to_geojson(node.northwest, features)
            self._add_node_to_geojson(node.northeast, features)
            self._add_node_to_geojson(node.southwest, features)
            self._add_node_to_geojson(node.southeast, features)

    def __repr__(self):
        return f"QuadTree(root={self.root})"
