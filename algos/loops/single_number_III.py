# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            singleNumber([1,2,1,3,2,5]),
            [3,5]
        )

def singleNumber(nums):
    hist = {}
    result = []
    
    for i in range(len(nums)):
        if nums[i] in hist:
            hist[nums[i]] += 1
        else:
            hist[nums[i]] = 1
    
    for k, v in hist.items():
        if v == 1:
            result.append(k)
    
    return result

if __name__ == "__main__":
    unittest.main()