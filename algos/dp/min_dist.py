def min_dist(s1,s2):
    """
    >>> min_dist('saturday','sunday')
    3

    >>> min_dist('horse', 'ros')
    3

    >>> min_dist("","")
    0

    """

    i = 0
    j = 0
    
    if len(s1) <= 1:
        i = len(s1)
    else:
        i = len(s1) - 1

    if len(s2) <= 1:
        j = len(s2)
    else:
        j = len(s2) - 1

    def recur(s1,s2,i,j, cache):
        ck = "%s:%s" % (i,j)

        if ck in cache:
            return cache[ck]

        if i == 0 or j == 0:
            # print("this is i: %s: this is j: %s" % (i,j))
            return max(i,j)
        
        a = recur(s1,s2,i-1,j, cache) + 1
        
        b = recur(s1,s2,i,j-1, cache) + 1
        
        k = 1 if s1[i-1] != s2[j-1] else 0
        c = recur(s1,s2,i-1,j-1, cache) + k
        cache[ck] = min(a,b,c)
        print(cache)
        return min(a,b,c)

    return recur(s1,s2,i,j,{})







# print(min_dist('intention', 'execution'))

# def	edDistRecursive(x,y):
#     if len(x) == 0:
#         return len(y)
    
#     if len(y) == 0:
#         return len(x)
    
#     k = 1 if x[-1] != y[-1] else 0
#     a = edDistRecursive(x[:-1], y[:-1]) + k
#     b = edDistRecursive(x[:-1], y) + 1
#     c = edDistRecursive(x,y[:-1]) + 1

#     return min(a,b,c)

# print(edDistRecursive('intention', 'execution'))