from friendsbalt.acs import Graph

class Components:
    
    # Initialize the search object and determine all the components
    def __init__(self, g: Graph):
        pass

    # Get the id of the connected component of v
    def component_of(self, v):
        pass
    
    # Are vertices u and v connected?
    def connected(self, u, v):
        pass
    


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(3, 4)

cmp = Components(g)

print(cmp.component_of(1))
print(cmp.component_of(2))

print(cmp.connected(1, 4))
print(cmp.connected(0, 2))