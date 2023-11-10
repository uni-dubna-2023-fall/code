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

        det_A = self.determinant(A)
        if det_A == 0:
            raise Exception("Matrix A is singular, circuit cannot be solved.")

        self.phi = self.solve_equations(A, b, len_nodes)

        for i in range(len_nodes):
            self.nodes[i].set_phi(self.phi[i])

    def determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        sign = 1
        det = 0

        for i in range(n):
            sub_matrix = [[0.0] * (n - 1) for _ in range(n - 1)]
            for j in range(1, n):
                aux = 0
                for k in range(n):
                    if k != i:
                        sub_matrix[j - 1][aux] = matrix[j][k]
                        aux += 1
            det += sign * matrix[0][i] * self.determinant(sub_matrix)
            sign *= -1

        return det

    def solve_equations(self, matrix, vector, n):
        x = [0.0] * n
        for k in range(n):
            pivot = matrix[k][k]
            for i in range(k + 1, n):
                factor = matrix[i][k] / pivot
                vector[i] -= factor * vector[k]
                for j in range(k, n):
                    matrix[i][j] -= factor * matrix[k][j]

        x[n - 1] = vector[n - 1] / matrix[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            sum = vector[i]
            for j in range(i + 1, n):
                sum -= matrix[i][j] * x[j]
            x[i] = sum / matrix[i][i]

        return x
