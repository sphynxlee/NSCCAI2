# adjacency_matrix = [
#     [False, True, False, False, False],
#     [False, False, True, False, False],
#     [False, False, False, True, False],
#     [False, False, False, False, True],
#     [True, False, False, False, False]
# ]


class Graph:
    def __init__(self, num_nodes) -> None:
        # self.num_nodes = num_nodes
        # self.adjacency_matrix = [[False for _ in range(num_nodes)] for _ in range(num_nodes)]

        self.adjacency_matrix = []
        for i in range(num_nodes):
            tmp = []
            for j in range(num_nodes):
                tmp.append(False)
            self.adjacency_matrix.append(tmp)

    def add_edge(self, node1, node2) -> None:
        self.adjacency_matrix[node1][node2] = True
        self.adjacency_matrix[node2][node1] = True

    def display_graph(self) -> None:
        # print(self.adjacency_matrix)
        for row in self.adjacency_matrix:
            print(row)


num_nodes = 5
graph = Graph(num_nodes)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)
graph.display_graph()