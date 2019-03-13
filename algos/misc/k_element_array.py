import unittest
import heapq

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([3,2,1,5,6,4], 2),
            5
        ),
    def test2(self):
        self.assertEqual(
            solve([3,2,3,1,2,4,5,5,6], 4),
            4
        )

def solve(arr, k):
    heapq.heapify(arr)

    result = heapq.nlargest(k, arr)
    
    return result[len(result)-1]

if __name__ == "__main__":
    unittest.main()