import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            findMaxConsecutiveOnes([1,0,1,1,0,1,0]),
            2
        )
    def test2(self):
        self.assertEqual(
            findMaxConsecutiveOnes([1]),
            1
        )

def findMaxConsecutiveOnes(nums):
    max_n = 0
    counter = 0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            counter += 1
            max_n = max(max_n, counter)
        else:
            counter = 0

    return max_n

if __name__ == "__main__":
    unittest.main()