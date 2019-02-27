# This problem was asked by Stripe.

# Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

# For example, given 156, you should return 3.

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            count_consecutive(156),
            3
        ),
    def test2(self):
        self.assertEqual(
            count_consecutive(55),
            3
        )

def count_consecutive(n):
    max_count = 0
    cur_count = 0
    bit = bin(n)

    for i in range(len(bit)):
        if bit[i] == '1':
            j = i
            while j < len(bit):
                if bit[j] == '1':
                    cur_count += 1
                    if cur_count > max_count:
                        max_count = cur_count
                    j += 1
                else:
                    break   
        cur_count = 0

    return max_count

if __name__ == "__main__":
    unittest.main()