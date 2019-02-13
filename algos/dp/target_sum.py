import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            target_sum([1, 1, 1, 1, 1], 3, 0, {}),
            5
        )
    def test2(self):
        self.assertEqual(
            target_sum([10,6,4,2,5],5,0,{}),
            2
        )

def target_sum(nums, target, i, cache):
    ck = "%s:%s" % (target, i)
    
    if ck in cache:
        return cache[ck]

    if i >= len(nums):
        if target == 0:
            return 1
        return 0

    l = target_sum(nums, target + nums[i], i+1, cache)
    r = target_sum(nums, target - nums[i], i+1, cache)
    cache[ck] = l+r
 
    return l+r

#brute force n(factorial)

# from itertools import product

# def combo(nums):
#     return [[num * mul for num, mul in zip(nums, combo)] for combo in product([1, -1], repeat=len(nums))]

# def target_sum(nums, S):
#     combos = combo(nums)
#     counter = 0

#     for i in combos:
#         if sum(i) == S:
#             counter += 1
    
#     return counter

if __name__ == "__main__":
    unittest.main()




