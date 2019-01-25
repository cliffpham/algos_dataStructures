def rec_dfs(G, s, visited=None):
    if visited is None:
        S = set()
    visited.add(s)
    for u in G[s]:              #loop through all neighbors
        if u in visited: continue
        rec_dfs(G,u,S)
    return 

def iter_dfs(G, s):
    visited = set()
    to_visit = []
    to_visit.append(s)
    
    while to_visit:
        v = to_visit.pop()
        if v in visited: continue
        visited.add(v)
        for neighbor in G[v]:
            to_visit.append(neighbor)
    return 