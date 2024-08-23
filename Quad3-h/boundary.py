class Boundary:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def contains(self, point):
        x, y = point
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

    def intersects(self, other):
        return not (self.x_max < other.x_min or self.x_min > other.x_max or
                    self.y_max < other.y_min or self.y_min > other.y_max)

    def get_cell_width(self, grid_columns):
        return (self.x_max - self.x_min) / grid_columns

    def get_cell_height(self, grid_rows):
        return (self.y_max - self.y_min) / grid_rows

    def get_grid_coordinates(self, point, grid_rows, grid_columns):
        x, y = point
        if not self.contains(point):
            raise ValueError("Point is outside the boundary.")

        cell_width = self.get_cell_width(grid_columns)
        cell_height = self.get_cell_height(grid_rows)

        column = int((x - self.x_min) // cell_width)
        row = int((y - self.y_min) // cell_height)

        return row, column
