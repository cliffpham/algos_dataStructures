import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            next_perm([1,2,3,4]),
            [1,2,4,3]
        ),
    def test2(self):
        self.assertEqual(
            next_perm([1,3,2]),
            [2,1,3]
        ),
    def test3(self):
        self.assertEqual(
            next_perm([1,2,3]),
            [1,3,2]
        ),
    def test4(self):
        self.assertEqual(
            next_perm([1,2,3]),
            [1,3,2]
        )
    def test5(self):
        self.assertEqual(
            next_perm([1,2]),
            [2,1]
        )

def next_perm(nums):
    left = 0
    right = len(nums) - 1
    k = -1
    l = -1

    # 1. Find the largest index k such that a[k] < a[k + 1]. 
    # If no such index exists, the permutation is the last permutation.

    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            k = i
    # 2. Find the largest index l greater than k such that a[k] < a[l].

    if k != -1:
        for j in range(len(nums)):
            if nums[k] < nums[j]:
                l = j
    # 3. Swap the value of a[k] with that of a[l].
    if l != -1:
        temp = nums[k]
        nums[k] = nums[l]
        nums[l] = temp
  
    # 4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
    left = k+1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1

    return nums
        
if __name__ == "__main__":
    unittest.main()
    
