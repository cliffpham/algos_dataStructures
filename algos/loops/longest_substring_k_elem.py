import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve('ababbc', 2),
            5
        ),
    def test2(self):
        self.assertEqual(
            solve('ababacb', 3),
            0
        )

def solve(s, k):
    #base case
    if len(s) < k:
        return 0

    for c in set(s):
        # print(c, s.count(c))
        if s.count(c) < k:
            # print(s.split(c))
            return max(solve(t, k) for t in s.split(c))
    return len(s)


if __name__ == "__main__":
    unittest.main()