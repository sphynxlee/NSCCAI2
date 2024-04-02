# https://www.youtube.com/watch?v=0KjG8Pg6LGk
# Gauss's magic shoelace area formula and its calculus companion

def shoelace_area(vertices):
    n = len(vertices)
    area = 0

    for i in range(n - 1):
        area += vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1]

    area += vertices[n - 1][0] * vertices[0][1] - vertices[0][0] * vertices[n - 1][1]

    return abs(area) / 2

# Example usage:
polygon_vertices = [(1, 1), (4, 5), (7, 2), (5, -2), (-1, -2)]
area = shoelace_area(polygon_vertices)
print("Area of the polygon:", area)
