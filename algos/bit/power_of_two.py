import unittest

class Test(unittest.TestCase):
    def test_one(self):
        self.assertTrue(
            solve(8)
        ),
    def test_two(self):
        self.assertTrue(
            solve(1)
        ),
    def test_three(self):
        self.assertFalse(
            solve(13)
        )

def solve(n):
    return n & (n-1) == 0

if __name__ == "__main__":
    unittest.main()
