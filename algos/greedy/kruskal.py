#prints are useful to determine how the union-find function and kruskal is operating

def find(C, u): 
    if C[u] != u:
      C[u] = find(C, C[u]) #recursive call to confirm that the set is directed at the proper representative
    #   print ('This is C: (*)', end='')
    #   print(C)
    return C[u]

def union(C, R, u, v):
  u, v = find(C, u), find(C, v)
#   print ('This is R (rank): ', end='')
#   print(R) 
#   print ('This is C before comparison : ', end='')
#   print(C)
#   print ('This is u: ', end='')
#   print(u)
#   print ('This is v: ', end='')
#   print(v) 
  if R[u] > R[v]:
    C[v] = u
    # print ('This is the union function if R[u] > R[v] then C[v] = u; thus the representative is: ', end='')
    # print(C[v])
    # print ('This is C after comparison : ', end='')
    # print(C) 
  else:
    C[u] = v
    # print ('NOT R[u] > R[v] then C[u] = v; thus the representative is: ', end='')
    # print(C[u])
    # print ('This is C after comparison : ', end='')
    # print(C) 
  if R[u] == R[v]:
    R[v] += 1
    # print ('This is the union function if R[u] == R[v] then R[v] += 1: ', end='')
    # print(R)

    # print ('This is R : ', end='')
    # print(R)

def kruskal(G):
#   for u in G:
    # print ('This is u : ', end='')
    # print(u)
    # for v in G[u]:
    #   print ('This is v : ', end='')
    #   print(v)

  E = [(G[u][v],u,v) for u in G for v in G[u]] #G[u][v] = weight, u = vertex1, v = vertex2

#   print ('This is sorted E : ', end='')
#   print(sorted(E))
  MST = set()
  C, R = {u:u for u in G}, {u:0 for u in G} # C. 'make' a set for each vertex | R. for path compression
#   print ('This is C : ', end='')
#   print(C)

  for _, u, v in sorted(E):
    # print('(*)')
    if find(C, u) != find(C, v): 
        MST.add((u, v))
        # print ('This is the MST after finding a new edge that does not create a cycle: ', end='')
        # print(MST)
        union(C, R, u, v) 
  
  return MST

# a, b, c, d, e, f, g, h = range(8)

# graph = {
# a: {b:1, c:10, f:7},
# b: {c:3},
# c: {d:4, e:11},
# d: {e:5},
# e: {f:8, h:6},
# f: {g:2},
# g: {h:9},
# h: {}
# }

# print(kruskal(graph))