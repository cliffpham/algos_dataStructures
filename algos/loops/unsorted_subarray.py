import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([2, 6, 4, 8, 10, 9, 15]),
            5
        ),
    def test2(self):
        self.assertEqual(
            solve([1,2,3,3,3,3]),
            0
        )

def solve(nums):
    nums_sorted = nums[:]
    nums_sorted.sort()
    
    start = 0
    end = 0
    
    for i in range(0,len(nums)):
        if nums[i] != nums_sorted[i]:
            start = i
            break
    
    for n in range(len(nums)-1,-1,-1):
        if nums[n] != nums_sorted[n]:
            end = n
            break
    
    if (start == 0)&(end == 0):
        return 0
    
    else:
        return end-start+1

if __name__ == "__main__":
    unittest.main()