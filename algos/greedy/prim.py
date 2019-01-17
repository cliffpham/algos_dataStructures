from heapq import heappop, heappush

def prim(G, s):
  P = {}
  Q = [(0, None, s)]
  
  while Q:
    _, p, c = heappop(Q) # _ = weight, p = previous vertex, c = current vertex
    if c in P: continue
    P[c] = p
    for v, w in G[c].items(): # v = vertex, w = weight
      heappush(Q,(w,c,v)) 
  return P

# test case

# a, b, c, d, e,f, g, h = range(8)

# graph2 = {
# a: {b:1, c:10, f:7},
# b: {c:3},
# c: {d:4, e:11},
# d: {e:5},
# e: {f:8, h:6},
# f: {g:2},
# g: {h:9},
# h: {}
# }
 

# print(prim(graph2, a))