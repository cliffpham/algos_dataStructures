# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            all_paths([[4,3,1],[3,2,4],[3],[4],[]]),
            [[0, 1, 4], [0, 1, 2, 3, 4], [0, 1, 3, 4], [0, 3, 4], [0, 4]]
        )

def all_paths(graph):
    cur_path = [0]
    output = []

    return visit_vertex(graph, 0, cur_path, output)

def visit_vertex(graph, i, cur_path, output):
    if i == len(graph)-1:
        output.append(cur_path[:])
        return
 
    origin = [v for v in graph[i]]
    
    while origin:
        vertex = origin.pop()
        cur_path.append(vertex)
        visit_vertex(graph, vertex, cur_path, output)
        cur_path.pop()

    return output

if __name__ == "__main__":
    unittest.main()