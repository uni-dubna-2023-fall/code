import numpy as np


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.phi = None

    def get_phi(self):
        return self.phi

    def set_phi(self, phi):
        self.phi = phi


class Edge:
    def __init__(self, idx, r, e=0.0, j=0.0):
        self.idx = idx
        self.r = r
        self.e = e
        self.j = j
        self.tip = None
        self.tail = None

    def attach_tip(self, node):
        self.tip = node

    def attach_tail(self, node):
        self.tail = node


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

            if edge.tip is not None:
                tip_idx = edge.tip.idx
                Z[tip_idx][tip_idx] += 1 / r
                V[tip_idx] += edge_voltage / r

            if edge.tail is not None:
                tail_idx = edge.tail.idx
                Z[tail_idx][tail_idx] += 1 / r
                V[tail_idx] -= edge_voltage / r

            if edge.tip is not None and edge.tail is not None:
                tail_idx = edge.tail.idx
                tip_idx = edge.tip.idx
                Z[tip_idx][tail_idx] -= 1 / r
                Z[tail_idx][tip_idx] -= 1 / r

        self.phi = np.linalg.solve(Z, V)

        for i in range(num_nodes):
            self.a[i].set_phi(self.phi[i])
