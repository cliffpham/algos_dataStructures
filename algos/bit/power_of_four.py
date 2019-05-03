import unittest

class Test(unittest.TestCase):
    def test_one(self):
        self.assertTrue(
            solve(16)
        ),
    def test_two(self):
        self.assertFalse(
            solve(8)
        )

def solve(n):
    count = 0
    #enter conditional only if there is a num and it is to the power of two
    if (n and n & (n-1) == 0):
        # shift one to the right in order to reduce num by 2  until num == 1
        # while also increasing the counter by 1 as a way of counting 0 bit
        while (n > 1):
            n >>= 1
            count += 1
        if count % 2 == 0:
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    unittest.main()

