def knapsack(w,v,c,i, cache):
    """
    >>> knapsack([5,3,4,2], [60,50,70,30], 5, 0, {})
    80

    >>> knapsack([4,3,6,2], [70,50,80,30], 6, 0, {})
    100

    """
    ck = "%s:%s" % (c, i)

    if ck in cache:
        return cache[ck]

    if  i >= len(w):
        return 0

    l = 0
    r = 0
    
    if c >= w[i]:
        r = knapsack(w,v,c-w[i], i, cache) + v[i]
    
    l = knapsack(w,v,c, i+1, cache)
    cache[ck] = max(l,r)

    return max(l,r)



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