import unittest

# necessary components: traversal method, graph structure, a dictionary to hold visited vertexes
# and marking the previous vertex you came from
# marking previous vertex is the caveat in this traversal question
# why?: to retrace our steps, preventing us from looping unnecessarily
# i.e. 0 -> 1
#      0 <- 1

class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(
            cycle_detect({0:[1,5], 1:[2,4], 2:[3], 3:[4], 4:[1]}, 0)
        ),
    def test2(self):
        self.assertFalse(
            cycle_detect({0:[1,2], 1:[0], 2:[0]}, 0)
        )

def recur_dfs(graph, cur, prev, visited):
    if cur in visited:
        return True
        
    visited.add(cur)

    for vertex in graph[cur]:
        if vertex != prev:
            if (recur_dfs(graph, vertex, cur, visited)):
                return True
    return False


def cycle_detect(graph, source):
    visited = set()
    return recur_dfs(graph, source, None, visited)

if __name__ == "__main__":
    unittest.main()
