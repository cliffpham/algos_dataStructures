import math

def min_coin(coins, target):

    """
    >>> min_coin([1,3,5], 11)
    3

    >>> min_coin([5,3], 4)
    -1

    >>> min_coin([1,2,4], 5)
    2
    """
    
    result = recur(coins, target, 0, cache = {}) 
    
    if result == float('inf'):
        return -1

    return result

def recur(coins, target, i, cache):
    ck = "%s:%s" % (target, i)

    if target in cache:
        return cache[target]

    if target < 0:
        return float('inf')

    if target == 0:
        return 0
    
    if i >= len(coins):
        return float('inf')

    l = recur(coins, target, i+1, cache)
    r = recur(coins, target - coins[i], i, cache) + 1
    
    cache[ck] = min(l,r)
    
    return min(l,r)

