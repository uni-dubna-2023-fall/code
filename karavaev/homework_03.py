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
    def __init__(self, idx, resistance, voltage_source=0.0, current_source=0.0):
        self.idx = idx
        self.resistance = resistance
        self.voltage_source = voltage_source
        self.current_source = current_source
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
        num_nodes = len(self.nodes)

        A = np.zeros((num_nodes, num_nodes), dtype=float)
        b = np.zeros(num_nodes, dtype=float)

        for edge in self.edges:
            r = edge.resistance
            edge_voltage = edge.voltage_source - edge.current_source * r

            if edge.tip is not None:
                tip_idx = edge.tip.idx
                A[tip_idx, tip_idx] += 1 / r
                b[tip_idx] += edge_voltage / r

            if edge.tail is not None:
                tail_idx = edge.tail.idx
                A[tail_idx, tail_idx] += 1 / r
                b[tail_idx] -= edge_voltage / r

            if edge.tip is not None and edge.tail is not None:
                A[tip_idx, tail_idx] -= 1 / r
                A[tail_idx, tip_idx] -= 1 / r

        self.phi = np.linalg.solve(A, b)

        for i in range(num_nodes):
            self.nodes[i].set_phi(self.phi[i])
