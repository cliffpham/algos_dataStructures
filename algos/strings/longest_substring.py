import unittest

class Tests(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(
            longest_substring('abcabc'),
            3
        )
    def test_longest_substring_prior(self):
        self.assertEqual(
            longest_substring('dvdf'),
            3
        )
    def test_longest_substring_single(self):
        self.assertEqual(
            longest_substring('bbbbbbbb'),
            1
        )
    def test_longest_substring_leetcode(self):
        self.assertEqual(
            longest_substring('pwwkew'),
            3
        )
    def test_longest_substring_nostring(self):
        self.assertEqual(
            longest_substring(''),
            0
        )
    def test_longest_substring_onlyspace(self):
        self.assertEqual(
            longest_substring('qu'),
            2
        )

def recur(str, cur_str, i):
    count = len(cur_str)

    if i >= len(str):
        return count

    if str[i] in cur_str:
        return count

    return recur(str, cur_str + str[i], i+1)

def longest_substring(str):
    max_val = 0
    for i in range(len(str)):
        cur_char = str[i];
        cur_str = '' + cur_char
        res = recur(str, cur_str, i+1)
        if max_val < res:
            max_val = res
    return max_val

if __name__ == "__main__":
    unittest.main()
