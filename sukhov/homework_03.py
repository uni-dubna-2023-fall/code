class Node:
    def __init__(self, idx):
        self.idx = idx
        self.phi = 0.0

    def get_phi(self):
        return self.phi


class Edge:
    def __init__(self, idx, r, e=0.0, j=0.0):
        self.idx = idx
        self.r = r
        self.e = e
        self.j = j
        self.tip_node = None
        self.tail_node = None

    def attach_tip(self, node):
        self.tip_node = node

    def attach_tail(self, node):
        self.tail_node = node


class Circuit:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        n = len(self.nodes)
        A = [[0.0 for _ in range(n)] for _ in range(n)]
        B = [0.0 for _ in range(n)]

        for edge in self.edges:
            if edge.tip_node and edge.tail_node:
                i = edge.tip_node.idx
                j = edge.tail_node.idx
                A[i][i] += 1 / edge.r
                A[j][j] += 1 / edge.r
                A[i][j] -= 1 / edge.r
                A[j][i] -= 1 / edge.r
                B[i] += edge.e
                B[j] -= edge.e

        phi = [0.0] * n
        for i in range(n):
            phi[i] = B[i] / A[i][i]

        for node in self.nodes:
            node.phi = phi[node.idx]
