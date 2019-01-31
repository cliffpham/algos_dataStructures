import unittest

class test_fib(unittest.TestCase):
    def test1_fib(self):
        self.assertEqual(
            fib_recur(10),
            55
        )

def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)


if __name__ == "__main__":
    unittest.main()