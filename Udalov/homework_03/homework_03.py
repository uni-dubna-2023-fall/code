import numpy as np


class Node:

    def __init__(self, x):
        self.x = x

    def get_b(self, x2, y2, epsilon):
        return self.b

    def set_b(self, b):
        self.b = b


class Edge:
    def __init__(self, idx, r, e=0.0, j=0.0):
        self.idx = idx
        self.r = r
        self.e = e
        self.j = j
        self.node = None
        self.node2 = None

    def attach_tip(self, node):
        self.node = node

    def attach_tail(self, node):
        self.node2 = node


class Circuit:
    def __init__(self):
        self.a = []
        self.b = []

    def add_node(self, node):
        self.a.append(node)

    def add_edge(self, edge):
        self.b.append(edge)

    def solve(self):
        num_nodes = len(self.a)

        Z = np.zeros((num_nodes, num_nodes), dtype=float)
        V = np.zeros(num_nodes, dtype=float)

        for edge in self.b:
            r = edge.r
            edge_voltage = edge.e - edge.j * r

            if edge.node is not None:
                tip_idx = edge.tip.idx
                Z[tip_idx][tip_idx] += 1 / r
                V[tip_idx] += edge_voltage / r

            if edge.node2 is not None:
                tail_idx = edge.tail.idx
                Z[tail_idx][tail_idx] += 1 / r
                V[tail_idx] -= edge_voltage / r

            if edge.node is not None and edge.node2 is not None:
                tail_idx = edge.tail.idx
                tip_idx = edge.tip.idx
                Z[tip_idx][tail_idx] -= 1 / r
                Z[tail_idx][tip_idx] -= 1 / r

        self.phi = np.linalg.solve(Z, V)

        for i in range(num_nodes):
            self.a[i].set_phi(self.phi[i])
