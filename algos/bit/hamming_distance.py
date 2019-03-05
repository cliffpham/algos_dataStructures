import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve(9,14),
            3
        )

def solve(n1, n2):
    x = n1 ^ n2
    count = 0

    while x > 0:
        # x & 1 produces a value that is either 1 or 0, depending on the least significant bit of x: 
        # if the last bit is 1, the result of x & 1 is 1; otherwise, it is 0. 
        # This is a bitwise AND operation.
        count += x & 1

        # x >>= 1 means "set x to itself shifted by one bit to the right". 
        # The expression evaluates to the new value of x after the shif
        x >>= 1
    
    return count

if __name__ == "__main__":
    unittest.main()