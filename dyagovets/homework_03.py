

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

        def gauss_elimination(n, m, A, b):
            for i in range(n - 1):
                for j in range(i + 1, n):
                    factor = A[j][i] / A[i][i]
                    for k in range(i, m):
                        A[j][k] -= factor * A[i][k]
                    b[j] -= factor * b[i]
            return A, b

        def back_substitution(n, A, b):
            x = [0.0] * n
            for i in range(n - 1, -1, -1):
                x[i] = b[i]
                for j in range(i + 1, n):
                    x[i] -= A[i][j] * x[j]
                x[i] /= A[i][i]
            return x

        A, b = gauss_elimination(len_nodes, len_nodes, A, b)
        self.phi = back_substitution(len_nodes, A, b)

        for i in range(len_nodes):
            self.nodes[i].set_phi(self.phi[i])
