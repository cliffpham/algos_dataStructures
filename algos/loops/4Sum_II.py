import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([1, 2], [-2,-1], [-1,2], [0,2]),
            2
        ),
    def test2(self):
        self.assertEqual(
            solve([0,0], [0,0], [0,0], [0,0]),
            16
        )

def solve(A,B,C,D):
    nums = {}
    count = 0
    
    for a in A:
        for b in B:
            ab = a + b
            if ab in nums:
                nums[ab] += 1
            else:
                nums[ab] = 1
    
    for c in C:
        for d in D:
            cd = -c - d
            if cd in nums:
                count += nums[cd]

    return count

if __name__ == "__main__":
    unittest.main()