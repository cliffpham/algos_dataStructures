import unittest
import re

class valid_palindromeTest(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(
            valid_palindrome('Ra:dAr')
        )
    def test_valid_palindrome_empty(self):
        self.assertTrue(
            valid_palindrome('')
        )
    def test_valid_plaindrome_false(self):
        self.assertFalse(
            valid_palindrome('race a car')
        )

def valid_palindrome(s):
    s = re.sub('[^A-Za-z0-9]+', '', s).lower()
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__ == "__main__":
    unittest.main()