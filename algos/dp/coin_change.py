def all_change(coins, amount):
    """
    >>> all_change([1,3,4], 5)
    3

    >>> all_change([10,25], 11)
    0
    
    """

    def recur(coins, amount, i, cache):
        ck = "%s:%s" % (amount, i)

        if ck in cache:
            return cache[ck]

        if amount < 0:
            return 0

        if amount == 0:
            return 1
        
        if i >= len(coins):
            return 0

        l = recur(coins, amount, i+1, cache)
        r = recur(coins, amount - coins[i],i, cache)
        
        cache[ck] = l+r

        return l+r

    return recur(coins, amount, i=0, cache={})

