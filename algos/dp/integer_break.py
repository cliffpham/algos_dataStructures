def integer_break(c):
    """
    >>> integer_break(10)
    36

    >>> integer_break(2)
    1

    """
    v = []
    for i in range(1,c):
        v.append(i)
    
    def recur(v, c, i, cache):
        ck = "%s:%s" % (c, i)

        if ck in cache:
            return cache[ck]

        if c == 0:
            return 1

        if c < 0:
            return 0
        
        if i == len(v):
            return 1
        
        l = recur(v, c, i+1, cache) #go down the left branch
        r = recur(v, c - v[i], i, cache) * v[i]
        cache[ck] = max(l,r)
    
        return max(l,r)

    return recur(v, c, i = 0, cache={})
