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

def longest_substring(s):
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1

    max_s = 0
    cur_unique_char = [s[0]]

    for i in range(1, len(s)):
        if s[i] not in cur_unique_char:
            cur_unique_char.append(s[i])
    
        # if existing char is found: compare max and reset cur values
        else:
            max_s = max(max_s, len(cur_unique_char))
            del cur_unique_char[:]
            cur_unique_char.append(s[i])
  
    max_s = max(max_s, len(cur_unique_char))
    return max_s

if __name__ == "__main__":
    unittest.main()