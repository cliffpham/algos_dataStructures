def cycle_detect(G): 
    """
    >>> cycle_detect({0:[1], 1:[2], 2:[3], 3:[1]})
    True

    >>> cycle_detect({0:[1], 1:[2], 2:[3], 3:[]})
    False
    """                  
    color = { u : "white" for u in G  }  
    found_cycle = [False]                # - Define found_cycle as a list so we can change

    for u in G:                          
        if color[u] == "white":
            dfs_visit(G, u, color, found_cycle)
        if found_cycle[0]:
            break
    return found_cycle[0]
 
def dfs_visit(G, u, color, found_cycle):
    if found_cycle[0]:                         
        return
    color[u] = "gray"                           
    for v in G[u]:                              
        if color[v] == "gray":                    
            found_cycle[0] = True       
            return
        if color[v] == "white":                  
            dfs_visit(G, v, color, found_cycle)
    color[u] = "black" 