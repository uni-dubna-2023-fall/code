import numpy


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.phi = None

    def get_phi(self):
        return self.phi

    def set_phi(self, phi):
        self.phi = phi


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
        self.nodes = {}
        self.edges = {}
        self.A = None
        self.AT = None
        self.Y = None
        self.J = None
        self.E = None

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        len_nodes = len(self.nodes)

        coefficient_matrix = [[0.0] * len_nodes for i in range(len_nodes)]
        rhs_vector = [0.0] * len_nodes

        for edge in self.edges:
            resistance = edge.r
            edge_e = edge.e - edge.j * resistance

            if edge.tip is not None:
                tip_idx = edge.tip.idx
                coefficient_matrix[tip_idx][tip_idx] += 1 / resistance
                rhs_vector[tip_idx] += edge_e / resistance

            if edge.tail is not None:
                tail_idx = edge.tail.idx
                coefficient_matrix[tail_idx][tail_idx] += 1 / resistance
                rhs_vector[tail_idx] -= edge_e / resistance

            if edge.tip is not None and edge.tail is not None:
                coefficient_matrix[tip_idx][tail_idx] -= 1 / resistance
                coefficient_matrix[tail_idx][tip_idx] -= 1 / resistance

        self.phi = numpy.linalg.solve(coefficient_matrix, rhs_vector)

        for i in range(len_nodes):
            self.nodes[i].set_phi(self.phi[i])
