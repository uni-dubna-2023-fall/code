"""def multi(matriza, vektor):
    resultat = []

    if len(matriza[0]) != len(vektor):
        print("Невозможно выполнить умножение")
        return None

    for riad in matriza:
        riad_resultat = 0
        for i  in range(len(riad)):
            riad_resultat = riad_resultat + (riad[i] * vektor[i])
        resultat.append(riad_resultat)

    return resultat """""
import numpy as np


class Node:

    def init(self, idx):
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

    def init(self, idx, r, e=None, j=None):
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
        self.AY = None
        self.AYAT = None
        self.U = None
        self.YE = None
        self.JYE = None
        self.AJYE = None

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
        for edge_idx in range(self.nodes):
            row = []
            for node_idx in range(self.nodes):
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

    def _calculate_AY(self):
        self.AY = []
        for nq in range(self.nodes):
            row = []
            for eq in range(self.edges):
                summ = 0.0
                for edge_idx in range(self.edges):
                    summ += self.A[nq][edge_idx] * self.Y[eq][edge_idx]
                row.append(summ)
            self.AY.append(row)

    def _calculate_AYAT(self):
        self.AYAT = []
        for nq in range(self.nodes):
            row = []
            for eq in range(self.nodes):
                summ = 0.0
                for edge_idx in range(self.edges):
                    summ += self.AY[nq][edge_idx] * self.AT[edge_idx][eq]
                row.append(summ)
            self.AY.append(row)

    def _calculate_U(self):
        self.U = []
        self.U = np.linalg.solve(self.AYAT, self.AJYE)

    def _calculate_YE(self):
        self.YE = []
        for edge_idx1 in range(self.edges):
            summ = 0.0
            for edge_idx2 in range(self.edges):
                summ += self.Y[edge_idx1][edge_idx2] * self.E[edge_idx1][0]
            self.YE.append(summ)

    def _calculate_JYE(self):
        self.JYE = []
        summ = 0.0
        for edge_idx in range(self.nodes):
            row = []
            summ = self.J[edge_idx] + self.YE[edge_idx]
            row.append(summ)
            self.JYE.append(row)

    def _calculate_AJYE(self):
        self.AJYE = []
        summ = 0.0
        for node_idx in range(self.nodes):
            summ = 0.0
            for edge_idx in range(self.nodes):
                row = []
                summ += self.A[node_idx][edge_idx] * self.J[edge_idx][0]
            if summ == 0:
                row.append(0.0)
                self.AJYE.append(row)
            else:
                row.append(-summ)
                self.AJYE

    def prepare(self):
        # calculate A
        self._calculate_A()
        # calculate A^T
        self._calculate_AT()
        # calculate Y
        self._calculate_Y()
        # calculate J
        self._calculate_J()
        # calculate E
        self._calculate_E()
        # calculate AY
        self._calculate_AY()
        # calculate AYA^T
        self._calculate_AYAT()
        # calculate YE
        self._calculate_YE
        # calculate JYE
        self._calculate_JYE
        # calculate -A(J + YE)
        self._calculate_AJYE()
        # calculate U
        self._calculate_U()
        for node_idx in (self.nodes):
            self.nodes[node_idx].set_phi(self.U[node_idx][0])
