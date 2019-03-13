import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([2, -1, 2, 5, -6]),
            8
        )
#DP Solution
def recur(nums,  i, took_previous=False, cache={}):
    ck = "%s:%s" % (i, took_previous)
    
    if ck in cache:
        return cache[ck]
    
    if i >= len(nums):
        if took_previous:
            return 0
        return float('-inf')
    
    l = nums[i]
    if not took_previous:
        l = recur(nums, i+1, False, cache) 
        
    r = recur(nums, i+1, True, cache ) + nums[i]
    if took_previous:
        r = max(r, 0)
    
    cache[ck] = max(l,r)
    print(cache)
    
    return max(l, r)

def solve(arr):
    
    return recur(arr, 0)

#Kadane's Algorithm
# def solve(nums):
#     temp = nums[0]
#     max_sum = nums[0]

#     for i in nums[1:]:
#         temp = max(i, temp + i)
#         max_sum = max(max_sum, temp)

#     return max_sum

if __name__ == "__main__":
    unittest.main()



