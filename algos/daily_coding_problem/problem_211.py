# This problem was asked by Microsoft.

# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
# For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].


import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            find_pattern("abracadabra", "abr"),
            [0,7]
        ),
    def test2(self):
        self.assertEqual(
            find_pattern("bcaabcbacabc", "abc"),
            [3,9]
        )
def find_pattern(s, p):
    find = len(p)
    result = []

    for i in range(len(s)):
        if s[i:find] == p:
            result.append(i)
        find+=1

    return result

if __name__ == "__main__":
    unittest.main()