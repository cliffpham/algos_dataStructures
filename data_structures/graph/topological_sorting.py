from collections import defaultdict, deque

def topological_sort(G):
    edge_list = {v: set(w) for v, w in G.items()}
    to_visit = deque([v for v, w  in edge_list.items() if not w])
    result = []
    descendants = defaultdict(list)

    for v, neighbors in edge_list.items():
        for neighbor in neighbors:
            descendants[neighbor].append(v)

    while to_visit:
        cur = to_visit.popleft()
        result.append(cur)

        for v in descendants[cur]:
            edge_list[v].remove(cur)
            if not edge_list[v]:
                to_visit.append(v)
    if len(result) <  len(edge_list):
        return None

    return result


#G = {
#        '1': [],
#        '2':['1'],
#        '3':['1'],
#        '4':['2','3'],
#        '5':['4'],
#        '6':['4']
#    }
#
#topological_sort(G)

    
