import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([7,1,5,3,6,4]),
            5
        )

def solve(stocks):
    max_prof = 0
    cur = float('inf')

    for i in stocks:
        if i < cur:
            cur = i
        max_prof = max(i - cur, max_prof)
    
    return max_prof

if __name__ == "__main__":
    unittest.main()