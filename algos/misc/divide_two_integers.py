import math
import unittest

# determine if either the dividend or the divisor is less than 0 and create a flag for it
# get the absolute values for the dividend and the divisor
# division can also be seen as subtracting the logs of the dividend and the divisor and then using math.exp as a log table look up
# handle integer overflow

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
        solve(10,3),
        3
        ),
    def test2(self):
        self.assertEqual(
        solve(-7, 3),
        -2
        ),
    def test3(self):
        self.assertEqual(
        solve(-10, -3),
        3
        ),
    def test4(self):
        self.assertEqual(
        solve(0,1),
        0
        )

def solve(dividend, divisor):
    is_negative = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    a = abs(dividend)
    b = abs(divisor)
    
    if dividend == 0:
        return 0
    
    quotient = is_negative * math.trunc(math.floor(math.exp(math.log(a)- math.log(b))))
    
    return max(min(quotient, 2**31 - 1), -2**31)

if __name__ == "__main__":
    unittest.main()
