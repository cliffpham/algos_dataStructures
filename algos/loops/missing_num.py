import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            missingnum([9,6,4,2,3,5,7,0,1]),
            8
        )
    def test2(self):
        self.assertEqual(
            missingnum([0,1]),
            None
        )

def missingnum(nums):
    nums.sort()
    res = None

    for i in range(len(nums)):
        if abs(nums[i] - nums[i-1]) != 1:
            res = nums[i]
    
    if res != None:
        res = res-1

    return res

#leetcode solution
# def missingnum(nums):
#     # print(len(nums)*(len(nums)+1)//2 )
#     # print(sum(nums))

#     return len(nums)*(len(nums)+1)//2 - sum(nums)

if __name__ == "__main__":
    unittest.main()
