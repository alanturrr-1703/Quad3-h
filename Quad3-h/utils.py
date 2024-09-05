# utils.py

import math
from point import Point


def distance_between_points(p1: Point, p2: Point) -> float:
    """
    Calculate the Euclidean distance between two points.
    :param p1: First point.
    :param p2: Second point.
    :return: Euclidean distance between p1 and p2.
    """
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def convert_cartesian_to_latlng(x: float, y: float, scale: float = 1.0) -> tuple:
    """
    Convert cartesian coordinates (x, y) to latitude and longitude.
    :param x: X-coordinate.
    :param y: Y-coordinate.
    :param scale: Scaling factor for conversion.
    :return: Tuple of (latitude, longitude).
    """
    lat = y * scale
    lng = x * scale
    return lat, lng


def convert_latlng_to_cartesian(lat: float, lng: float, scale: float = 1.0) -> tuple:
    """
    Convert latitude and longitude to cartesian coordinates (x, y).
    :param lat: Latitude.
    :param lng: Longitude.
    :param scale: Scaling factor for conversion.
    :return: Tuple of (x, y) coordinates.
    """
    x = lng / scale
    y = lat / scale
    return x, y
