class Node:
    def __init__(self, idx):
        self.idx = idx
        self.phi = 0.0

    def get_phi(self):
        return self.phi


class Edge:
    def __init__(self, idx, q, w=0.0, e=0.0):
        self.idx = idx
        self.q = q
        self.w = w
        self.e = e
        self.tip_node = None
        self.tail_node = None

    def attach_top(self, node):
        self.tip_node = node


class Circuit:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def solve(self):
        n = len(self.nodes)
        Q = [[0.0 for _ in range(n)] for _ in range(n)]
        W = [0.0 for _ in range (n)]

        for edge in self.edges:
            if edge.tip_node and edge.tail_node:
                z = edge.tip_node.idx
                x = edge.tail_node.idx
                Q[z][z] += 1 / edge.r
                Q[x][x] += 1 / edge.r
                Q[z][x] -= 1 / edge.r
                Q[x][z] -= 1 / edge.r
                W[z] += edge.e
                W[x] -= edge.e

        C = [0.0] * n
        for z in range(n):
            C[z] = W[z] / Q[z][z]

        for node in self.nodes:
            node.C = C[node.idx]
