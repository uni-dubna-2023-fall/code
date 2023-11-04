class Node:
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.phi = 0.0

    def attach_edge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, index, resistance, current=0.0):
        self.index = index
        self.resistance = resistance
        self.current = current
        self.tip = None
        self.tail = None

    def attach_tip(self, node):
        self.tip = node
        node.attach_edge(self)

    def attach_tail(self, node):
        self.tail = node
        node.attach_edge(self)

class Circuit:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        # Initialize potentials at each node
        for node in self.nodes:
            node.phi = 0.0

        # Iterate until convergence
        max_iterations = 1000
        tolerance = 1e-6
        for iteration in range(max_iterations):
            max_error = 0.0
            
            # Update potentials at each node
            for node in self.nodes:
                prev_phi = node.phi
                if len(node.edges) > 0:
                    total_current = sum(edge.current for edge in node.edges)
                    total_resistance = sum(edge.resistance for edge in node.edges)
                    if total_resistance > 0:
                        node.phi = total_current / total_resistance
                error = abs(node.phi - prev_phi)
                max_error = max(max_error, error)
            
            # Check for convergence
            if max_error < tolerance:
                break

    def get_phi(self):
        return [node.phi for node in self.nodes]
        
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

c.solve()

print(f"\u03C6_0 = {c.get_phi()[0]}")
print(f"\u03C6_1 = {c.get_phi()[1]}")