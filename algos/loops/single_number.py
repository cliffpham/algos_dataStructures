# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

import unittest

class test_single_number(unittest.TestCase):
    def test1_single_number(self):
        self.assertEqual(
            single_number([2,3,1,3,2]),
            1
        )
    def test2_single_number(self):
        self.assertEqual(
            single_number([4,1,2,1,2]),
            4
    )

def single_number(nums):
    hist = {}
    for i in range(len(nums)):
        if nums[i] in hist: 
            hist[nums[i]] += 1
        else:
            hist[nums[i]] = 1
    
    for k, v in hist.items():
        if v == 1:
            return k

print(single_number([4,1,2,1,2]))

if __name__ == "__main__":
    unittest.main()