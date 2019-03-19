import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([[ 1,  5,  9],[10, 11, 13],[12, 13, 15]], 8),
            13
        ),
    def test2(self):
        self.assertEqual(
            solve([[1,2],[1,3]], 2),
            1
        )

def solve(matrix, k):
    order = []

    for row in matrix:
        for item in row:
            order.append(item)
    
    order.sort()

    return order[k-1]

if __name__ == "__main__":
    unittest.main()