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
        self.YE = None
        self.J_YE = None
        self._AJ_YE = None
        self.AY = None
        self.AYAT = None
        self.U = None

    def add_node(self, node):
        self.nodes[node.idx] = node

    def add_edge(self, edge):
        self.edges[edge.idx] = edge

    def _calculate_A(self):
        self.A = []
        for node_idx in self.nodes:
            row = []
            for edge_idx in self.edges:
                if edge_idx in self.nodes[node_idx].edges:
                    row.append(self.nodes[node_idx].edges[edge_idx][1])
                else:
                    row.append(0.0)
            self.A.append(row)

    def _calculate_AT(self):
        self.AT = []
        for edge_idx in self.edges:
            row = []
            for node_idx in self.nodes:
                row.append(self.A[node_idx][edge_idx])
            self.AT.append(row)

    def _calculate_Y(self):
        self.Y = []
        for edge_idx1 in self.edges:
            row = []
            for edge_idx2 in self.edges:
                if edge_idx1 == edge_idx2:
                    row.append(self.edges[edge_idx1].y)
                else:
                    row.append(0.0)
            self.Y.append(row)

    def _calculate_J(self):
        self.J = []
        for edge_idx in self.edges:
            if self.edges[edge_idx].j is None:
                self.J.append(0.0)
            else:
                self.J.append(self.edges[edge_idx].j)

    def _calculate_E(self):
        self.E = []
        for edge_idx in self.edges:
            row = []
            if self.edges[edge_idx].e is None:
                row.append(0.0)
                self.E.append(row)
            else:
                row.append(self.edges[edge_idx].e)
                self.E.append(row)

    def _calculate_YE(self):
        self.YE = []
        for edge_idx1 in self.edges:
            i = 0.0
            for edge_idx2 in self.edges:
                i += self.Y[edge_idx1][edge_idx2] * self.E[edge_idx1][0]
            self.YE.append(i)

    def _calculate_J_YE(self):
        self.J_YE = []
        i = 0.0
        for edge_idx in self.edges:
            row = []
            i = self.J[edge_idx] + self.YE[edge_idx]
            row.append(i)
            self.J_YE.append(row)

    def _calculate_AJ_YE(self):
        self.AJ_YE = []
        for node_idx in self.nodes:
            i = 0.0
            for edge_idx in self.edges:
                row = []
                i += self.A[node_idx][edge_idx] * self.J_YE[edge_idx][0]
            if i == 0:
                row.append(0.0)
                self.AJ_YE.append(row)
            else:
                row.append(-i)
                self.AJ_YE.append(row)

    def _calculate_AY(self):
        self.AY = []
        for node_idx in self.nodes:
            row = []
            for ei1 in self.edges:
                i = 0.0
                for ei2 in self.edges:
                    i += self.A[node_idx][ei2] * self.Y[ei1][ei2]
                row.append(i)
            self.AY.append(row)

    def _calculate_AYAT(self):
        self.AYAT = []
        for ni1 in self.nodes:
            row = []
            for ni2 in self.nodes:
                i = 0.0
                for edge_idx in self.edges:
                    i += self.AY[ni1][edge_idx] * self.AT[edge_idx][ni2]
                row.append(i)
            self.AYAT.append(row)

    def _calculate_U(self):
        self.U = []
        self.U = np.linalg.solve(self.AYAT, self.AJ_YE)

    def solve(self):
        self._calculate_A()
        self._calculate_AT()
        self._calculate_Y()
        self._calculate_J()
        self._calculate_E()
        self._calculate_AY()
        self._calculate_AYAT()
        self._calculate_YE()
        self._calculate_J_YE()
        self._calculate_AJ_YE()
        self._calculate_U()
        for node_idx in self.nodes:
            self.nodes[node_idx].set_phi(self.U[node_idx][0])
