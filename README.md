# Graph Components Assignment

In this assignment, you will demonstrate your understanding of Depth First Search (DFS) and the Graph API. Using the provided `Graph` class, you will implement a function to find all connected components in an undirected graph.

## Task
Complete the class `Components` with the following methods:
- `__init__(self, graph: Graph)`: Initializes the `Components` class with a given graph by "labeling" all of its vertices according to their connected components.
- `component_of(self, vertex: int)`: Returns the component number of the given vertex.
- `connected(self, vertex1: int, vertex2: int)`: Returns `True` if the two vertices are in the same connected component, and `False` otherwise.

## Strategy
Write a helper function to perform a DFS traversal from a given vertex. Since DFS traverses all vertices in a connected component, you can label all vertices in that component with the same number. Then, perform DFS for the next unvisited vertex until all vertices are labeled.

This should be done in `__init__` method. The `component_of` and `connected` methods can be implemented using the labels assigned during the initialization.
