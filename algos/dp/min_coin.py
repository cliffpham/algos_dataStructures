import math

def min_coin(coins, target):
    
    result = recur(coins, target, cache = {}) 
    
    if result == float('inf'):
        return -1

    return result

def recur(coins, target, cache):

    if target in cache:
        return cache[target]

    if target < 0:
        return float('inf')

    if target == 0:
        return 0

    best = float('inf')
    for c in coins:
        best = min(best, recur(coins, target - c, cache) + 1)
        cache[target] = best
    
    return cache[target]

print(min_coin([1,3,4],4))
print(min_coin([2,4],3))
print(min_coin([1,2,5],11))