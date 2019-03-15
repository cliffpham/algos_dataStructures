import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve(4,[[1,0],[2,0],[3,1],[3,2]]),
            [0,1,2,3]
        ),
    def test2(self):
        self.assertEqual(
            solve(2,[[0,1]]),
            [1,0]
        )

def solve(numCourses, prerequisites):
    #initialize all nodes as unchecked (white)
    visit = [0 for _ in range(numCourses)]

    #create graph from edge list
    graph = [[] for _ in range(numCourses)]

    result = []

    for x, y in prerequisites:
        graph[x].append(y)
    
    # print(graph)
    # traverse through each vertex and search for any cycles
    # if cycle is detected - course schedule isn't possible return empty arr
    # otherwise, after visiting all vertexes return the schedule order
    for i in range(numCourses):
        if not dfs(i, visit, graph, result):
            return []

    return result

def dfs(i, visit, graph, result):
    #exit case 'cycle has been detected' grey 
    if visit[i] == -1:
        return False
    
    #exit case 'finished traversing graph' black
    if visit[i] == 1:
        return True
    
    #mark vertex grey
    visit[i] = -1
    
    #check neighbors
    for j in graph[i]:
        if not dfs(j, visit, graph, result):
            return False
    
    #black
    visit[i] = 1

    #only after all vertexs has been visited, do we add the course to the result list
    result.append(i)
    
    return result

if __name__ == "__main__":
    unittest.main()