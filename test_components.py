from friendsbalt.acs import Graph
from components import Components

def test_component_of():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    cmp = Components(g)

    assert cmp.component_of(0) == cmp.component_of(1)
    assert cmp.component_of(1) == cmp.component_of(3)
    assert cmp.component_of(3) == cmp.component_of(4)
    assert cmp.component_of(2) != cmp.component_of(0)

def test_connected():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    cmp = Components(g)

    assert cmp.connected(0, 1) is True
    assert cmp.connected(1, 4) is True
    assert cmp.connected(0, 4) is True
    assert cmp.connected(0, 2) is False
    assert cmp.connected(2, 3) is False

def test_disconnected_graph():
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    cmp = Components(g)

    assert cmp.component_of(0) == cmp.component_of(1)
    assert cmp.component_of(2) == cmp.component_of(3)
    assert cmp.component_of(4) == cmp.component_of(5)
    assert cmp.component_of(0) != cmp.component_of(2)
    assert cmp.component_of(2) != cmp.component_of(4)

    assert cmp.connected(0, 1) is True
    assert cmp.connected(2, 3) is True
    assert cmp.connected(4, 5) is True
    assert cmp.connected(0, 2) is False
    assert cmp.connected(1, 4) is False

def test_no_edges():
    g = Graph(5)
    cmp = Components(g)

    for v in range(5):
        assert cmp.component_of(v) == v
        for u in range(5):
            if u != v:
                assert cmp.connected(u, v) is False

def test_fully_connected_graph():
    g = Graph(4)
    for i in range(4):
        for j in range(i + 1, 4):
            g.add_edge(i, j)
    cmp = Components(g)

    for v in range(4):
        assert cmp.component_of(v) == cmp.component_of(0)
        for u in range(4):
            assert cmp.connected(u, v) is True

def test_single_vertex_graph():
    g = Graph(1)
    cmp = Components(g)

    assert cmp.component_of(0) == 0
    assert cmp.connected(0, 0) is True
