import unittest

class test(unittest.TestCase):
    def test(self):
        self.assertEqual(
            find_dups([4,3,2,7,8,2,3,1,1,1]),
            [3,2]
        )
    def test2(self):
        self.assertEqual(
            find_dups([1,1]),
            [1]
        )

def find_dups(nums):
    seen = {}
    result = []

    for i in range(len(nums)-1, -1, -1):
        if nums[i] in seen:
            seen[nums[i]] += 1
        else:
            seen[nums[i]] = 1

    for i in seen:
        if seen[i] == 2:
            result.append(i)
 
    return result

if __name__ == "__main__":
    unittest.main()