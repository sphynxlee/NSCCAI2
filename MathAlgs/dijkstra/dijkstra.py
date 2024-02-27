# draw a graph for thinking
# Reference: https://www.youtube.com/watch?v=QsAUil2eBZs
#  A --2-- C\
#  |       | \ 5
# 1|      4|  E
#  |       | / 6
#  B --3-- D/
#
# vertices = [A, B, C, D, E]
# Edges = [(A, B), (A, C), (B, D), (C, D), (C, E), (D, E)]
# weights = {
#     (A, B): 1,
#     (A, C): 2,
#     (B, D): 3,
#     (C, D): 4,
#     (C, E): 5,
#     (D, E): 6
# }
# adjacency_matrix = {
#    "A": {"B": 1, "C": 2},
#    "B": {"A": 1, "D": 3},
#    "C": {"A": 2, "D": 4, "E": 5},
#    "D": {"B": 3, "C": 4, "E": 6},
#    "E": {"C": 5, "D": 6}
# }


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 1: Create a graph by using adjacency matrix
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# create a graph by using adjacency matrix
class Graph:
    def __init__(self, vertices, edges, weights):
        self.vertices = vertices
        self.edges = edges
        self.weights = weights
        self.adjacency_matrix = self.generate_adjacency_matrix()

    def generate_adjacency_matrix(self):
        # Create an empty matrix with all values set to 0
        matrix = {vertex: {} for vertex in self.vertices}

        for edge in self.edges:
            v1, v2 = edge
            weight = self.weights[edge]

            # Add the edge to the adjacency matrix
            matrix[v1][v2] = weight
            matrix[v2][v1] = weight

        return matrix

# Define the graph
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
weights = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('B', 'D'): 3,
    ('C', 'D'): 4,
    ('C', 'E'): 5,
    ('D', 'E'): 6
}

my_graph = Graph(vertices, edges, weights)

# print the adjacency matrix of the graph
print("Adjacency Matrix:")
for vertex, neighbors in my_graph.adjacency_matrix.items():
    print(f"{vertex}: {neighbors}")


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Part 2: Implement Dijkstra's algorithm
# # # # # # # # # # # # # # # # # # # # # # # # # # # #


def dijkstra(graph, start, end):
    # in the beginning, the distance from first(start) vertex to other all vertices is set to infinity
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0

    # Create a dictionary to store the previous vertex for each vertex
    previous_vertices = {vertex: None for vertex in graph.vertices}

    # Create a set to keep track of vertices that have already been visited
    unvisited_vertices = set(graph.vertices)

    # Loop until all vertices have been visited
    while unvisited_vertices:
        # Select the unvisited vertex with the smallest distance from the start vertex
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])

        # Remove the current vertex from the set of unvisited vertices
        unvisited_vertices.remove(current_vertex)

        # If the current vertex is the end vertex, break the loop
        if current_vertex == end:
            break

        # Update the distances and previous_vertices for the neighbors of the current vertex
        for neighbor, weight in graph.adjacency_matrix[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_vertices[neighbor] = current_vertex

    # Create a list to store the shortest path from the start vertex to the end vertex
    path = []
    current_vertex = end

    # Traverse the previous_vertices to construct the shortest path
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    # Add the start vertex to the shortest path
    path.insert(0, start)

    return path, distances[end]

# test: the shortest path and distance from 'A' to 'E'
start_vertex = 'A'
end_vertex = 'E'
shortest_path, distance = dijkstra(my_graph, start_vertex, end_vertex)
print(f"Shortest path from {start_vertex} to {end_vertex}: {shortest_path}")
