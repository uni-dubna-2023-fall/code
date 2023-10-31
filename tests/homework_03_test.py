import logging


def test_circuit(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Circuit for %s", surname)
        n0 = m.Node(0)
        n1 = m.Node(1)
        n2 = m.Node(2)

        e0 = m.Edge(0, 200.0, 5.0)
        e0.attach_tail(n0)

        e1 = m.Edge(1, 100.0)
        e1.attach_tip(n0)

        e2 = m.Edge(2, 50.0)
        e2.attach_tip(n0)
        e2.attach_tail(n1)

        e3 = m.Edge(3, 100.0)
        e3.attach_tip(n1)

        e4 = m.Edge(4, 150.0)
        e4.attach_tip(n1)
        e4.attach_tail(n2)

        e5 = m.Edge(5, 100.0)
        e5.attach_tip(n2)

        e6 = m.Edge(6, 300.0)
        e6.attach_tip(n2)

        c = m.Circuit()
        c.add_node(n0)
        c.add_node(n1)
        c.add_node(n2)
        c.add_edge(e0)
        c.add_edge(e1)
        c.add_edge(e2)
        c.add_edge(e3)
        c.add_edge(e4)
        c.add_edge(e5)
        c.add_edge(e6)
        c.solve()
        assert round(n0.get_phi(), 4) == -1.069
        assert round(n1.get_phi(), 4) == -0.6207
        assert round(n2.get_phi(), 4) == -0.2069
        logging.info("Test Circuit for %s: OK", surname)
