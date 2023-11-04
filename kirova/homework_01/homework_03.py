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
        self.AT = None
        self.Y = None
        self.J = None
        self.E = None
    
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

    def prepare(self):
        # calculate A
        self._calculate_A()
        # calculate A^T
        self.AT = []
        for i in range(len(self.A[0])):
            column = []
            for j in range(len(self.A)):
                column.append(self.A[j][i])
            self.AT.append(column)
        # calculate Y
        self.Y = []
        for edge_idx in self.edges:
            self.Y.append([self.edges[edge_idx].y])
        # calculate J
        self.J = []
        for edge_idx in self.edges:
            if self.edges[edge_idx].j is not None:
                self.J.append([self.edges[edge_idx].j])
            else:
                self.J.append([0.0])
        # calculate E
        self.E = []
        for edge_idx in self.edges:
            if self.edges[edge_idx].e is not None:
                self.E.append([self.edges[edge_idx].e])
            else:
                self.E.append([0.0])
        # calculate AYA^T
        AYA_T = []
        for i in range(len(self.A)):
            row = []
            for j in range(len(self.AT)):
                sum_result = 0
                for k in range(len(self.A[0])):
                    sum_result += self.A[i][k] * self.Y[k][j] * self.AT[j][k]
                row.append(sum_result)
            AYA_T.append(row)
        # calculate -A(J + YE)
        AYE = []
        for i in range(len(self.A)):
            row = []
            for j in range(len(self.J)):
                sum_result = 0
                sum_result += self.J[i][j] + self.E[i][j]
                row.append(sum_result)
            AYE.append(row)

        _AJYE = []
        for i in range(len(self.A)):
            row = []
            for j in range(len(AYE[0])):
                sum_result = 0
                for k in range(len(self.AT)):
                    sum_result += self.A[i][k] * AYE[k][j]
                row.append(-sum_result)
            _AJYE.append(row)
        return _AJYE

    def solve(self):
        AJYE = self.prepare()
        AYAE_T = np.add(AYA_T, AJYE)
        YAE_inv = np.linalg.inv(AYAE_T)
        YAJE = np.dot(YAE_inv, self.J)
        YAE = np.dot(YAE_inv, self.E)
        
        for edge_idx in self.edges:
            self.edges[edge_idx].e = YAE[edge_idx]
            self.edges[edge_idx].j = YAJE[edge_idx]
