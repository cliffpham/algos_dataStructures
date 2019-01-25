def convert(edgelist):
    adj_list = {}
    for edge in edgelist:
        u = edge[0]
        v = edge[1]
        if u in adj_list:
            adj_list[u].append(v)
            adj_list[v] = []
        else:
            adj_list[u] = [v]
    return adj_list

def check(G):
    color = {u: 'white' for u in G}
    conflict = [False]

    for u in G:
        if color[u] == 'white':
            dfs_visit(G, u, color, conflict)
        if conflict[0]:
            break
    
    #if there is a conflict return false
    if conflict[0]:
        return False
    return True

def dfs_visit(G, u, color, conflict):
    if conflict[0]:
        return
    color[u] = 'gray'
    for v in G[u]:
        if color[v] == 'gray':
            conflict[0] = True
            return
        if color[v] == 'white':
            dfs_visit(G, v,color,conflict)
    color[u] = 'black'

    
graph = [
    [1,0],
    [0,1]
]

graph = convert(graph)

print(check(graph))