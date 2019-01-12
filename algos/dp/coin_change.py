def all_change(amount, coins):

    def recur(amount, coins, i, cache):
        ck = "%s:%s"(amount, i)

        if ck in cache:
            return cache[ck]

        if amount < 0:
            return 0

        if amount == 0:
            return 1
        
        if i >= len(coins):
            return 0

        l = recur(amount, coins, i+1, cache)
        r = recur(amount - coins[i], coins,i, cache)
        
        cache[ck] = l+r

        return l+r

    return recur(amount, coins, i=0, cache={})

print(all_change(500, [3,5,7,8,9,10,11]))
print(all_change(5, [1,3,4]))