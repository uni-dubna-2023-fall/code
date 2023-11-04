import numpy as np


class Node:

    def __init__(self, idx):
        self.idx = idx
        self.phi = None
        self.edges = {}

    def attach(self, edge, direction):
        self.edges[edge.idx] = [edge, direction]


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
        self.Y = None
        self.J = None
        self.E = None

    def add_node(self, node):
        self.nodes[node.idx] = node

    def add_edge(self, edge):
        self.edges[edge.idx] = edge

    def _calculate_A(self):

        num_nodes = len(self.nodes)
        num_edges = len(self.edges)
        self.A = np.zeros((num_nodes, num_edges))
        for i, node_idx in enumerate(self.nodes):
            for j, edge_idx in enumerate(self.edges):
                if edge_idx in self.nodes[node_idx].edges:
                    self.A[i, j] = self.nodes[node_idx].edges[edge_idx][1]

    def _calculate_Y(self):

        num_edges = len(self.edges)
        self.Y = np.zeros((num_edges, num_edges))
        for edge_idx in self.edges:
            self.Y[edge_idx, edge_idx] = self.edges[edge_idx].y

    def _calculate_J(self):

        num_nodes = len(self.nodes)
        self.J = np.zeros((num_nodes, 1))
        for node_idx in self.nodes:
            if self.nodes[node_idx].phi is not None:
                self.J[node_idx, 0] = -self.nodes[node_idx].phi

    def _calculate_E(self):

        num_edges = len(self.edges)
        self.E = np.zeros((num_edges, 1))
        for edge_idx in self.edges:
            if self.edges[edge_idx].e is not None:
                self.E[edge_idx, 0] = self.edges[edge_idx].e

    def solve(self):
        self._calculate_A()
        self._calculate_Y()
        self._calculate_J()
        self._calculate_E()

circuit = Circuit()
