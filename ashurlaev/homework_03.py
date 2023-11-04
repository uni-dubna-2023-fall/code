import numpy as np
class Node:
    def __init__(self, idx):
        self.idx = idx
        self.edges_in = []
        self.edges_out = []
        self.fi = None
    def get_phi(self):
        return self.fi
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
        node.edges_in.append(self)
    def attach_tail(self, node):
        self.tail_node = node
        node.edges_out.append(self)


class Circuit:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.A = None
        self.b = None
    def add_node(self, node: Node):
        self.nodes.append(node)
    def add_edge(self, edge: Edge):
        self.edges.append(edge)
    def setup_equations(self):
        n = len(self.nodes)
        m = len(self.edges)
        self.A = np.zeros((n + m, n + m))
        self.b = np.zeros(n + m)
        for i, node in enumerate(self.nodes):
            self.A[i][i] = 1.0
            self.b[i] = node.fi if node.fi is not None else 0.0
        for i, edge in enumerate(self.edges):
            idx = n + i
            if edge.tip_node is not None:
                self.A[idx][edge.tip_node.idx] = 1.0
            if edge.tail_node is not None:
                self.A[idx][edge.tail_node.idx] = -1.0
            self.A[idx][idx] = edge.r
            self.b[idx] = edge.e - edge.j
    def solve_equations(self):
        x = np.linalg.solve(self.A, self.b)
        for i, node in enumerate(self.nodes):
            node.fi = x[i]
        return x[:len(self.nodes)]
    def solve(self):
        self.setup_equations()
        print("Equations A*x = b before solving:")
        print(self.A)
        print(self.b)
        solution = self.solve_equations()
        print("Equations A*x = b after solving:")
        print(self.A)
        print(self.b)
        print("Node potentials:")
        for i, node in enumerate(self.nodes):
            print(f"Node {node.idx}: Phi = {node.fi}")
        return solution
circuit = Circuit()
node1 = Node(0)
node2 = Node(1)
node3 = Node(2)
edge1 = Edge(0, 1.0)
edge2 = Edge(1, 2.0)
edge3 = Edge(2, 3.0)

edge1.attach_tip(node1)
edge1.attach_tail(node2)
edge2.attach_tip(node2)
edge2.attach_tail(node3)
edge3.attach_tip(node3)
edge3.attach_tail(node1)

circuit.add_node(node1)
circuit.add_node(node2)
circuit.add_node(node3)
circuit.add_edge(edge1)
circuit.add_edge(edge2)
circuit.add_edge(edge3)
solution = circuit.solve()
print("Solution:", solution)