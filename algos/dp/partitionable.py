# [1, 5, 11, 5] true [5,5,1] [11]

# [1, 2, 3, 5]  false

# [6,2,4,4] true [6,2] [4,4]

def partitionable(arr):
    total = sum(arr)

    if total % 2 == 1:
        return False

    target = int(total / 2)

    def recur(arr, target, i, cache):
        ck = "%s:%s" % (target, i)
        
        if ck in cache:
            cache[ck]
        
        if target < 0:
            return False
        
        if target == 0:
            return True

        if i >= len(arr):
            return 

        l = recur(arr, target, i+1,cache)
        r = recur(arr, target - arr[i], i+1, cache)
        cache[ck] = l or r
        
        return l or r

    return recur(arr, target, 0, {})

print(partitionable([1,5,11,5]))
print(partitionable([1,2,3,5]))
print(partitionable([6,2,4,4]))
