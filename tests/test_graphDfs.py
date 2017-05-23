from unittest import TestCase
from results import Results


class TestGraphDfs(TestCase):
    def test_dfs(self):
        try:
            from build import GraphDfs
        except ImportError:
            self.assertFalse("no class found")

        self.results = Results()

        nodes = []
        graph = GraphDfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.dfs(nodes[0], self.results.add_result)
        self.assertEqual(str(self.results), "[0, 1, 3, 2, 4, 5]")
