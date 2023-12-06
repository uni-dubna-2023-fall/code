class Node:
    def __init__(self, idx):
        self.idx = idx  # Индекс узла
        self.edges = []  # Список связанных компонентов цепи

    def get_phi(self):
        phi = 0.0
        for edge in self.edges:
            if edge.tip_node == self:
                phi += edge.e
            elif edge.tail_node == self:
                phi -= edge.e
        return phi / len(self.edges)



class Edge:
    def __init__(self, idx, r, e=0.0, j=0.0):
        self.idx = idx  # Индекс компонента цепи
        self.r = r  # Сопротивление
        self.e = e  # Источник ЭДС
        self.j = j  # Источник тока
        self.tip_node = None  # Входящий узел
        self.tail_node = None  # Выходящий узел

    def attach_tip(self, node):
        self.tip_node = node
        node.edges.append(self)

    def attach_tail(self, node):
        self.tail_node = node
        node.edges.append(self)


class Circuit:
    def __init__(self):
        self.nodes = []  # Список узлов цепи
        self.edges = []  # Список компонентов цепи

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def solve(self):
        n = len(self.nodes)
        matrix = [[0.0] * n for _ in range(n)]
        vector = [0.0] * n

        for i, node in enumerate(self.nodes):
            for edge in node.edges:
                if edge.tip_node == node:
                    matrix[i][i] += 1.0 / edge.r
                    if edge.tail_node:
                        matrix[i][edge.tail_node.idx] -= 1.0 / edge.r
                    vector[i] += edge.j
                elif edge.tail_node == node:
                    matrix[i][i] += 1.0 / edge.r
                    if edge.tip_node:
                        matrix[i][edge.tip_node.idx] -= 1.0 / edge.r
                    vector[i] -= edge.j

        # Реализация метода Гаусса с выбором главного элемента
        for i in range(n):
            max_row = i
            for j in range(i + 1, n):
                if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                    max_row = j
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            vector[i], vector[max_row] = vector[max_row], vector[i]
            for j in range(i + 1, n):
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(i, n):
                    matrix[j][k] -= ratio * matrix[i][k]
                vector[j] -= ratio * vector[i]

        potentials = [0.0] * n

        for i in range(n - 1, -1, -1):
            potentials[i] = vector[i]
            for j in range(i + 1, n):
                potentials[i] -= matrix[i][j] * potentials[j]
            potentials[i] /= matrix[i][i]

        for i, node in enumerate(self.nodes):
            node.phi = potentials[i]


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
print(f"\u03C6_0 = {n0.get_phi()}")
print(f"\u03C6_1 = {n1.get_phi()}")
