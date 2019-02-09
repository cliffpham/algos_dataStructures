#brute force n(factorial)

from itertools import product

def combo(nums):
    return [[num * mul for num, mul in zip(nums, combo)] for combo in product([1, -1], repeat=len(nums))]

def target_sum(nums, S):
    combos = combo(nums)
    counter = 0

    for i in combos:
        if sum(i) == S:
            counter += 1
    
    return counter

def target_sums(nums, target, i):
    
    if target == 0:
        return 1

    if target < 0:
        return 0
    
    if i >= len(nums):
        return 0

    l = target_sums(nums, target, i+1)
    r = target_sums(nums, target - nums[i], i+1)
 
    return l+r

# print(target_sum([1, 1, 1, 1, 1], 3))
print(target_sum([1, 2, 3, 4, 5], 3))
print(target_sum([10, 6, 4, 2, 5], 5))

print(target_sums([1, 2, 3, 4, 5], 3, 0))
print(target_sums([10, 6, 4, 2, 5], 5, 0))


