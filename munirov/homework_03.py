import numpy


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.phi = None

    def get_phi(self):
        return self.phi

    def set_phi(self, phi):
        self.phi = phi

    def attach(self, edge, direction):
        self.edges[edge.idx] = [edge, direction]


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
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        len_nodes = len(self.nodes)

        coefficient_matrix = [[0.0] * len_nodes for i in range(len_nodes)]
        rhs_vector = [0.0] * len_nodes

        for edge in self.edges:
            r = edge.r
            edge_e = edge.e - edge.j * r

            if edge.tip is not None:
                tip_idx = edge.tip.idx
                coefficient_matrix[tip_idx][tip_idx] += 1 / r
                rhs_vector[tip_idx] += edge_e / r

            if edge.tail is not None:
                tail_idx = edge.tail.idx
                coefficient_matrix[tail_idx][tail_idx] += 1 / r
                rhs_vector[tail_idx] -= edge_e / r

            if edge.tip is not None and edge.tail is not None:
                coefficient_matrix[tip_idx][tail_idx] -= 1 / r
                coefficient_matrix[tail_idx][tip_idx] -= 1 / r

        self.phi = numpy.linalg.solve(coefficient_matrix, rhs_vector)

        for i in range(len_nodes):
            self.nodes[i].set_phi(self.phi[i])
