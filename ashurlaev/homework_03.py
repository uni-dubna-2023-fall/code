class Node:
    def __init__(self, idx):
        self.idx = idx
        self.phi = 0.0

    def get_phi(self):
        return self.phi


class Edge:
    def __init__(self, idx, r, e=0.0, j=0.0):
        self.idx = idx
        self.r = r
        self.e = e
        self.j = j
        self.tip_node = None
        self.tail_node = None

    def attach_tip(self, node):
        self.tip_node = node

    def attach_tail(self, node):
        self.tail_node = node


class Circuit:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def solve(self):
        n = len(self.nodes)
        A = [[0.0] * n for _ in range(n)]
        B = [0.0] * n

        for edge in self.edges:
            tip_idx = edge.tip_node.idx
            tail_idx = edge.tail_node.idx

            A[tip_idx][tip_idx] += 1.0 / edge.r
            A[tip_idx][tail_idx] -= 1.0 / edge.r

            if edge.e != 0.0:
                B[tip_idx] += edge.e / edge.r

            if edge.j != 0.0:
                B[tip_idx] -= edge.j

            if edge.tip_node != edge.tail_node:
                A[tail_idx][tail_idx] += 1.0 / edge.r
                A[tail_idx][tip_idx] -= 1.0 / edge.r

        for i in range(n):
            max_row = i

            for j in range(i + 1, n):
                if abs(A[j][i]) > abs(A[max_row][i]):
                    max_row = j

            A[i], A[max_row] = A[max_row], A[i]
            B[i], B[max_row] = B[max_row], B[i]

            for j in range(i + 1, n):
                ratio = A[j][i] / A[i][i]

                for k in range(i, n):
                    A[j][k] -= ratio * A[i][k]

                B[j] -= ratio * B[i]

        for i in range(n - 1, -1, -1):
            self.nodes[i].phi = B[i] / A[i][i]
            print(f"Node {i}: phi = {self.nodes[i].phi}")
