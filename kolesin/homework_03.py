import numpy as np


class Node:

    def __init__(self, idx):
        self.idx = idx
        self.phi = None
        self.edges = {}

    def attach(self, edge, direction):
        self.edges[edge.idx] = [edge, direction]

    def get_phi(self):
        return self.phi


class Edge:

    def __init__(self, idx, r, e=None, j=None):
        self.idx = idx
        self.r = r
        self.e = e
        self.j = j
        self.y = 1.0 / self.r
        self.tip = None
        self.tail = None

    def attach_tip(self, node):
        self.tip = node
        node.attach(self, -1.0)

    def attach_tail(self, node):
        self.tail = node
        node.attach(self, 1.0)


class Circuit:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        len_nodes = len(self.nodes)

        A = [[0.0] * len_nodes for _ in range(len_nodes)]
        b = [0.0] * len_nodes

        for edge in self.edges:
            r = edge.r
            edge_e = edge.e - edge.j * r

            if edge.tip is not None:
                tip_idx = edge.tip.idx
                A[tip_idx][tip_idx] += 1 / r
                b[tip_idx] += edge_e / r

            if edge.tail is not None:
                tail_idx = edge.tail.idx
                A[tail_idx][tail_idx] += 1 / r
                b[tail_idx] -= edge_e / r

            if edge.tip is not None and edge.tail is not None:
                A[tip_idx][tail_idx] -= 1 / r
                A[tail_idx][tip_idx] -= 1 / r

        det_A = np.linalg.det(A)
        if det_A == 0:
            raise Exception("Matrix A is singular, circuit cannot be solved.")

        self.phi = np.linalg.solve(A, b)

        for i in range(len_nodes):
            self.nodes[i].phi = self.phi[i]
