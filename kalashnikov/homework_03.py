class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.phi = 0.0

    def get_phi(self):
        return self.phi


class Edge:
    def __init__(self, edge_id, resistance=0.0):
        self.edge_id = edge_id
        self.resistance = resistance
        self.tip = None
        self.tail = None

    def attach_tip(self, node):
        self.tip = node

    def attach_tail(self, node):
        self.tail = node

    def get_current(self):
        return (self.tip.get_phi() - self.tail.get_phi()) / self.resistance

    def get_emf(self):
        return self.get_current() * self.resistance


class Circuit:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        for edge in self.edges:
            edge.tip.phi = edge.tail.phi + edge.get_emf()

    def print_node_potentials(self):
        for node in self.nodes:
            print(f"\u03C6_{node.node_id} = {node.get_phi()}")
