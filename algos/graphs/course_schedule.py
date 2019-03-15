import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            canFinish(4, [[1,0],[2,0],[3,1],[3,2]]),
            True
        ),
    def test2(self):
        self.assertEqual(
            canFinish(3, [[1,0],[2,0]]),
            True
        ),
    def test3(self):
        self.assertEqual(
            canFinish(2, [[1,0],[0,1]]),
            False
        )

def canFinish(numCourses, prerequisites):
    #initialize all nodes as unchecked (white)
    visit = [0 for _ in range(numCourses)]

    #create graph from edge list
    graph = [[] for _ in range(numCourses)]

    for x, y in prerequisites:
        graph[x].append(y)
    
    # traverse through each vertex and search for any cycles
    # if cycle is detected - schedule is not possible
    # otherwise, schedule is possible
    for i in range(numCourses):
        if not dfs(i, visit, graph):
            return False

    return True

def dfs(i, visit, graph):
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
        if not dfs(j, visit, graph):
            return False
    
    #black
    visit[i] = 1
    
    return True

if __name__ == "__main__":
    unittest.main()

# def convert(edgelist):
#     adj_list = {}
#     for edge in edgelist:
#         u = edge[0]
#         v = edge[1]
#         if u in adj_list:
#             adj_list[u].append(v)
#             adj_list[v] = []
#         else:
#             adj_list[u] = [v]
#     return adj_list

# def check(G):
#     if len(G) <= 1:
#         return True

#     color = {u: 'white' for u in G}
#     conflict = [False]

#     for u in G:
#         if color[u] == 'white':
#             dfs_visit(G, u, color, conflict)
#         if conflict[0]:
#             break
    
#     #if there is a conflict return false
#     if conflict[0]:
#         return False
#     return True

# def dfs_visit(G, u, color, conflict):
#     if conflict[0]:
#         return
#     color[u] = 'gray'
#     for v in G[u]:
#         if color[v] == 'gray':
#             conflict[0] = True
#             return
#         if color[v] == 'white':
#             dfs_visit(G, v,color,conflict)
#     color[u] = 'black'

    
# graph = [
#     [1,0],
#     [0,1]
# ]


# graph2 = [
#     [1,0]
# ]
# graph = convert(graph)

# print(check(graph))
# print(check(graph2))