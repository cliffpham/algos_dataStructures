import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([1,2,2,1], [2,2]),
            [2]
        ),
    def test2(self):
        self.assertEqual(
            solve([3,1,2], [1,1]),
            [1]
        ),
    def test3(self):
        self.assertEqual(
            solve([6,6,4,4,0,0,8,1,2], [6]),
            [6]
        )

def solve(nums1, nums2):
    result = []
    
    if len(nums1) > len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp
    
    search_for = set(nums1)
    used = set()
    
    for num in nums2:
        if num in search_for and num not in used:
            used.add(num)
            result.append(num)
    
    return result


if __name__ == "__main__":
    unittest.main()