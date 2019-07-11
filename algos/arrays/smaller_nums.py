# bisect takes up to four arguments that keeps the ordering of a sort
# (list, number, start_range, end_rage)
# traverse the array from right to left
# at each number create a sorted array using the bisect module
# the index placement of the number indicates how many values are less than the current number


import unittest
import bisect

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            solve([5,2,6,1]),
            [2,1,1,0]
        )

def solve(arr):
    seen = []
    result = []

    for num in reversed(arr):
        position = bisect.bisect_left(seen, num)
        result.append(position)
        bisect.insort(seen, num)

    return list(reversed(result))

if __name__ == "__main__":
    unittest.main()
