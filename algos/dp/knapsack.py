def brute_knapsack(w,v,c,i):
    if  i >= len(w):
        return 0

    l = 0
    r = 0
    if c >= w[i]:
        r = brute_knapsack(w,v,c-w[i], i) + v[i]
    l = brute_knapsack(w,v,c, i+1)

    return max(l,r)

w = [5,3,4,2]
v = [60,50,70,30]
c = 5

w2 = [4,3,6,2]
v2 = [70,50,80,30]
c2 = 6

print(brute_knapsack(w,v,c, i = 0))
print(brute_knapsack(w2,v2,c2, i = 0))

# def knapsack(w,v,c):
#     def m(r):
#         print(r)
#         if r == 0:
#             print('0 go back up')
#             return 0
#         val = m(r-1)
#         print(val)
#         for i, wi in enumerate(w):
#             print(str(i) + ',' + str(wi))
#             if wi > r: 
#                 print('hit')
#                 continue
#             val = max(val, v[i] + m(r-wi))
#             print('updated val', end='')
#             print(val)
#         return val
#     return m(c)

# w = [5,3,4,2]
# v = [60,50,70,30]
# c = 5

# print(knapsack(w,v,c))