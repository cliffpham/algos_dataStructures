#Given an array of integers, find if the array contains any duplicates.

#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

import unittest

class test_duplicate(unittest.TestCase):
    def test1_duplicate(self):
        self.assertTrue(
            duplicate([1,2,3,1,4,5,6])
        )
    def test2_duplicate(self):
        self.assertFalse(
            duplicate([1,2,3,4,5])
        )


def duplicate(nums):
    hist = set()
    for i in range(len(nums)):
        if nums[i] in hist:
            return True
        hist.add(nums[i])
    return False

if __name__ == "__main__":
    unittest.main()