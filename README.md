# QuadTree Package - Quad3-h

## Overview

The `Quad3-h` package provides an efficient quadtree data structure for organizing and querying spatial data. It also includes the ability to store images as points and integrates with map APIs like Google Maps.

### Features
- **Efficient Quadtree Implementation**: Spatial indexing for points with dynamic insertion and querying.
- **Point Class**: Represents spatial points with optional metadata (such as images).
- **Boundary Class**: Defines boundaries for quadtree nodes and regions.
- **K-Nearest Neighbors**: Quickly find the `k` nearest neighbors to a given point.
- **Image Store**: Save and retrieve images associated with points.
- **GeoJSON Export**: Export the tree structure in GeoJSON format for use with mapping libraries.