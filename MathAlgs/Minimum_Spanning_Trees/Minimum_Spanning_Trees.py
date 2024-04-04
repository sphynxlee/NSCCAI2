# Sort Edges by Weight:
# A-C: 1
# D-E: 2
# B-E: 3
# A-B: 6
# B-C: 5
# C-D: 5
# C-E: 6
# A-D: 5


# Start with the Smallest Edge (A-C: 1):
# - Add edge A-C to the MST.

# Next Smallest Edge (D-E: 2):
# - Add edge D-E to the MST.

# Next Smallest Edge (B-E: 3):
# - Add edge B-E to the MST.

# Next Smallest Edge (A-B: 6):
# - Add edge A-B to the MST.

#      A
#    /   \
#   C     B
#         |
#         E
#         |
#         D
# Total weight of MST: 1 + 2 + 3 + 6 = 12


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        self.parent[root1] = root2


def kruskal_mst(graph):
    mst = []
    vertices = list(graph.keys())
    edges = [(u, v, weight) for u in vertices for v, weight in graph[u]]
    edges.sort(key=lambda edge: edge[2])
    disjoint_set = DisjointSet(vertices)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            disjoint_set.union(u, v)

    return mst


graph = {
    'A': [('B', 6), ('C', 1), ('D', 5)],
    'B': [('A', 6), ('C', 5), ('E', 3)],
    'C': [('A', 1), ('B', 5), ('D', 5), ('E', 6)],
    'D': [('A', 5), ('C', 5), ('E', 2)],
    'E': [('B', 3), ('C', 6), ('D', 2)]
}

mst = kruskal_mst(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):")
for edge in mst:
    print(edge)
