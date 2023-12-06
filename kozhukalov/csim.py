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
        # calculate Y
        # calculate J
        # calculate E
        # calculate AYA^T
        # calculate -A(J + YE)
        pass

    def solve(self):
        pass


n0 = Node(0)
n1 = Node(1)

e0 = Edge(0, 100.0)
e1 = Edge(1, 100.0)
e2 = Edge(2, 100.0)
e3 = Edge(3, 100.0)
e4 = Edge(4, 100.0, 5.0)

e0.attach_tip(n0)
e1.attach_tip(n0)
e2.attach_tip(n1)
e3.attach_tip(n1)
e3.attach_tail(n0)
e4.attach_tail(n1)

c = Circuit()
c.add_node(n0)
c.add_node(n1)

c.add_edge(e0)
c.add_edge(e1)
c.add_edge(e2)
c.add_edge(e3)
c.add_edge(e4)

print(c.A)
c.prepare()
print(c.A)
