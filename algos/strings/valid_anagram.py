import unittest

class test_valid_anagram(unittest.TestCase):
    def test1_valid_anagram(self):
        self.assertTrue(
            valid_anagram('anagram', 'nagrama')
        )

    def test2_valid_anagram(self):
        self.assertFalse(
            valid_anagram('anagram', 'nagramas')
        )

    def test3_valid_anagram(self):
        self.assertFalse(
            valid_anagram('aa', 'a')
        )

def valid_anagram(s, t):
    seen = {}

    for i in range(len(s)):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1

    for i in range(len(t)):
        if t[i] in seen:
            seen[t[i]] -= 1
            
            if seen[t[i]] == 0:
                del seen[t[i]]

        else:
            seen[t[i]] = 1
    
    return len(seen) == 0

if __name__ == "__main__":
    unittest.main()