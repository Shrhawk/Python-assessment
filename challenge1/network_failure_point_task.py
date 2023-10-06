"""
Time complexity to build the graph: O(n), space complexity: O(n)
Time complexity to find the max num of conn: O(n), space complexity: O(1)
"""


class Graph:
    def __init__(self, num_of_nodes: int, directed: bool = True):
        """
        Initialize a graph with a given number of nodes.

        Args:
            num_of_nodes (int): The number of nodes in the graph.
            directed (bool): True if the graph is directed, False for undirected.

        Returns:
            None
        """
        self.num_of_nodes = num_of_nodes

        # Define the type of a graph
        self.m_directed = directed
        self.adj_hash = {}

    def add_edge(self, node1):
        """
        Add an edge between two nodes.

        Args:
            node1: The first node.

        Returns:
            None
        """
        if node1 not in self.adj_hash:
            self.adj_hash[node1] = 1
        else:
            self.adj_hash[node1] += 1

    def print_adj_list(self):
        """
        Print the adjacency list of the graph.

        Returns:
            None
        """
        for node in self.adj_hash:
            print(node)

    def print_node_with_highest_conn(self):
        """
        Print the node(s) with the highest number of connections.

        Returns:
            int: The maximum number of connections.
        """
        self.max_conn = 0
        for node in self.adj_hash:
            self.max_conn = max(self.max_conn, self.adj_hash[node])
        return self.max_conn


directed_graph = Graph(6)
directed_graph.add_edge(1)
directed_graph.add_edge(2)
directed_graph.add_edge(3)
directed_graph.add_edge(5)
directed_graph.add_edge(2)

if __name__ == '__main__':
    print("Expected router with highest connection: 2")
    print(f"Actual router with highest connection: {directed_graph.print_node_with_highest_conn()}")

# Test case
try:
    assert directed_graph.print_node_with_highest_conn() == 2
except AssertionError:
    print("Assertion failed for test case")
