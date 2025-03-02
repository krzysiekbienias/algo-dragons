class Graph:
    def __init__(self):
        """Initialize an empty graph.

                The graph is represented as a dictionary where the keys are nodes
                and the values are sets of adjacent nodes.
        """
        self.graph = dict()

    def add_edge(self, u, v):
        """Add an edge from node u to node v in the graph.

                Parameters
                ----------
                u : node
                    The start node for the edge.
                v : node
                    The end node for the edge.

                Notes
                -----
                If node u does not exist in the graph, it is added with v as
                its adjacent node.
        """
        if u not in self.graph.keys():
            self.graph[u] = set([v])
        else:
            self.graph[u].add(v)
        if u not in self.graph.keys():
            self.graph[u] = set([v])
        else:
            self.graph[u].add(v)

    def edge_exists(self, u, v):
        """Check if an edge exists between nodes u and v.

                Parameters
                ----------
                u : node
                    The first node.
                v : node
                    The second node.

                Returns
                -------
                bool
                    True if there is an edge between u and v, False otherwise.
        """
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

    def adjacent_nodes(self, node):
        """Return a list of nodes adjacent to the given node.

                Parameters
                ----------
                node : node
                    The node for which to find adjacent nodes.

                Returns
                -------
                list
                    A list of nodes adjacent to the specified node.

                Raises
                ------
                KeyError
                    If the node is not in the graph.
        """
        return list(self.graph[node])

    def unconnected_vertices(self):
        """Find all nodes in the graph that have no edges.

                Returns
                -------
                list
                    A list of nodes that are unconnected (i.e., have no edges).
        """
        unconnected = []
        for u in self.graph.keys():
            if len(self.graph[u]) == 0:
                unconnected.append(u)
        return unconnected

    def breadth_first_search(self, v):
        """Perform a breadth-first search starting from the given node.

                Parameters
                ----------
                v : node
                    The starting node for the search.

                Returns
                -------
                list
                    A list of nodes visited during the breadth-first search.
        """
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbours = sorted(self.graph[s])
            for neighbor in sorted_neighbours:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited